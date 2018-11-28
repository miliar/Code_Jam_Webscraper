#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

char lin[60000];
char first[60000], last[18][1<<15];

int nr, n, K, N, best;
int ok[20];

int Cost(int lev, int poz){
    int tot = N;
    for (int i=0; i<N; i++){
        char c = lin[i*K+poz];
        if (lev){
           if (c == last[lev-1][i]) tot--;
           if (lev == K-1 && c == first[i+1]) tot--;
        } else first[i] = c;
        last[lev][i] = c;
    }
    return tot;
}

void back(int lev, int cost){
//     printf("%d %d\n", lev, cost);
//     if (cost+N >= best) return;
     if (lev == K){
        if (cost < best) best = cost;
        return;
     }
     for (int i=0; i<K; i++)
         if (!ok[i]){
            ok[i] = 1;
            back(lev+1, cost+Cost(lev, i));
            ok[i] = 0;
         }
}

void solve(){
     scanf("%d\n", &K);
     scanf("%s\n", lin);
     n = strlen(lin);
     N = n/K;
     first[N] = 0;
     best = n;
     back(0, 0);
     nr++;
     printf("Case #%d: %d\n", nr, best);
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int tst;
    scanf("%d", &tst);
    while (tst--)
          solve();
    return 0;
}
