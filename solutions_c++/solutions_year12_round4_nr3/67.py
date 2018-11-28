#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<string>
#include<cctype>
#include<climits>
#include<algorithm>
#include<complex>
#include<vector>
#include<queue>
#include<set>
#include<map>

using namespace std;

typedef long long LL;

const int MaxN = 2000 + 5;

bool flag;
int T, N, MaxLel, MinHei;
int after[MaxN], level[MaxN], h[MaxN];

bool noSol() {
    for (int i = 1; i < N; ++i) if (after[i] <= i) return true;
    for (int i = 1; i < N; ++i) 
        for (int j = i + 1; j < N; ++j)
            if (after[i] > j && after[i] < after[j]) return true;
    return false;
}

void getLevel() {
   MaxLel = 0;
   memset(level, 0, sizeof(level)); 
   for (int i = 1; i < N; ++i) {
       for (int j = i - 1; j >= 1; --j)
           if (after[j] > i) {
               level[i] = level[j];
               break;
           }
       level[i]++;
   }
   for (int i = 1; i < N; ++i) MaxLel = max(MaxLel, level[i]);
}

void solve() {
    for (int i = 1; i <= N; ++i) h[i] = i;
    for (int L = 1; L <= MaxLel; ++L)
        for (int i = N - 1; i >= 1; --i) if (level[i] == L) {
            h[i] = h[after[i]] - (after[i] - i) * L;
            for (int k = i + 1; k <= after[i] - 1; ++k)
                h[k] = h[i] + (k - i) * L - 1;
        }
    MinHei = 0x7fffffff;
    for (int i = 1; i <= N; ++i) MinHei = min(MinHei, h[i]);
    for (int i = 1; i <= N; ++i) h[i] -= MinHei;
}

int main() {

    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    scanf("%d", &T);
    for (int te = 1; te <= T; ++te) {
        scanf("%d", &N);
        for (int i = 1; i < N; ++i) scanf("%d", after + i);
        printf("Case #%d:", te);
        if (noSol()) {printf(" Impossible\n"); continue;}
        getLevel();
        solve();
        for (int i = 1; i <= N; ++i) printf(" %d", h[i]);
        puts("");
    }

    return 0;

}

