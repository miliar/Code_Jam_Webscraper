#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>

using namespace std;

const int MAXN = 105;

int i, j, k, p, cas, T, N, S, P, a[MAXN], dp[MAXN][MAXN];

void init()
 {
     memset(a, 0, sizeof(a));
     memset(dp, 0, sizeof(dp));
     scanf("%d%d%d", &N, &S, &P);
     for (i = 1; i <= N; i ++)
         scanf("%d", &a[i]);
 }

void work()
 {
     for (i = 1; i <= N; i ++)
      {
            k = a[i] / 3 + (a[i] % 3 > 0);
            p = (a[i]/3)+1+(a[i]%3>1);
            if (!a[i]) p = 0;
            dp[i][0] = dp[i-1][0] + (k >= P);
            for (j = 1; j <= i && j <= S; j ++)
                dp[i][j] = max(dp[i-1][j] + (k >= P), dp[i-1][j-1] + (p >= P));
      }
     printf("Case #%d: %d\n", cas, dp[N][S]);
 }
 
int main()
 {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    for (scanf("%d", &T), cas = 1; cas <= T; cas ++)
     {
        init();
        work();
     }
    return 0;
 }
