#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;

long long answer(queue<pii>& q, int R, int k, int N) {
    vector<long long> profit; profit.reserve(R/10);
    int i;    
    for(i=0; i<R; ++i) {
        int in = 0;
        queue<pii> inside;
        while(in + q.front().second <= k) {
            in += q.front().second; 
            inside.push(q.front());
            q.pop();
            if(q.empty()) break;
        }
        while(!inside.empty()) {
            q.push(inside.front()); inside.pop();
        }
        profit.push_back(in);
        if(profit.size()>1) profit[profit.size()-1] += profit[profit.size()-2];
        /*if(q.front().first == 0) {
            i++;
            break;
        }*/
    }
    return profit[profit.size()-1];
    /*if(i>=R) return profit[profit.size()-1];
    else {
        long long div = profit[profit.size()-1]*(R/i);
        long long mod =  0;
        if(R%i!=0)
            mod = profit[R%i];
        return  div + mod;
    }*/
}

int main() {
    
    freopen("C-small3.in", "r", stdin);
    freopen("C-small3.out", "w", stdout);
    
    int T; scanf("%d", &T);
    for(int i=1; i<=T; ++i) {
        queue<pii> q;
        int R, k, N; scanf("%d %d %d", &R, &k, &N);
        for(int j=0; j<N; ++j) {
            int a; scanf("%d", &a);
            q.push(make_pair(j, a));
        }
        printf("Case #%d: %I64d\n", i, answer(q, R, k, N));
    }
    
    return 0;
}
