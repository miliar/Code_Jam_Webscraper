#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<cassert>

using namespace std;

int n_towers, N, C;
long long build_time;
//build_time is even
//ans is integer

long long dist[1000005];
bool check_for_ind;
int ind;
long long left_dist;
int strt_pt;

long long cdist(int k) {
    if (check_for_ind) {
        if (k == strt_pt) return left_dist;
    }
    if (k < C) return dist[k];
    else return dist[k%C];
}

void work() {
    check_for_ind = false;
    scanf("%d %lld %d %d\n", &n_towers, &build_time, &N, &C);
    for (int i = 0 ; i < C ; i++) {
        scanf("%lld", &dist[i]);
    }

    long long ans = 0, cum = 0;
    ind = 0;

    while (ind < N && cum + 2*cdist(ind) <= build_time) {
        cum += 2*cdist(ind);
        ind++;
    }

    if (ind == N) {
        printf("%lld\n", cum);
        return;
    }

    //printf("ind = %d, cum = %lld\n", ind, cum);
    
    int covered_dist = (build_time - cum);
    //printf("covered dist = %d\n", covered_dist);;
    ans = cum + covered_dist;

    strt_pt = ind;

    left_dist = cdist(ind) - covered_dist/2;
    check_for_ind = true;
    int mx = ind, mx2 = -1;
    
    //ind++;

    //printf("ind = %d, left_dist = %d, ans = %lld\n", ind, left_dist, ans);
    priority_queue<int> pq;
    //pq.clear();
    while ( ind < N) {
        pq.push(cdist(ind));
        ind++;
    }

    while(!pq.empty()) {
        int pop = pq.top();
        pq.pop();
        if(n_towers) {
            ans += (long long)pop;
            n_towers--;
        }
        else {
            ans += 2*((long long)pop);
        }
    }
    
    printf("%lld\n", ans);
}

/////////////////////////////////////////////////////////////


int main() {
    int T;
    scanf("%d\n", &T);
    for (int tt = 1 ; tt <= T ; tt++) {
        printf("Case #%d: ", tt);
        work();
    }
}
