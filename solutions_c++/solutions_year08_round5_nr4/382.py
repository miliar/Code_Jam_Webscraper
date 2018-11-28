/*
  GCJ 2008 Round 3; D -- Endless Knight
  - sqybi's code
*/

#include <iostream>
using namespace std;

const int nn = 100;
int dp[nn+1][nn+1], cases, n, m, r, x, y;
const int MODS = 10007;
void f(int x, int y)
{
    dp[x][y] = 0;
    if (x - 1 > 0 && y - 2 > 0)
    {
        if (dp[x-1][y-2] == -1) f(x-1, y-2);
        dp[x][y] += dp[x-1][y-2];
        dp[x][y] %= MODS;
    }
    if (x - 2 > 0 && y - 1 > 0)
    {
        if (dp[x-2][y-1] == -1) f(x-2, y-1);
        dp[x][y] += dp[x-2][y-1];
        dp[x][y] %= MODS;
    }
}

int main()
{
   //freopen("d.in", "r", stdin);
    //freopen("d.out", "w", stdout);
    scanf("%d", &cases);
    for (int times = 1; times <= cases; ++ times)
    {
        scanf("%d%d%d", &n, &m, &r);
        for (int i = 1; i <= n; ++ i)
            for (int j = 1; j <= m; ++ j)
                dp[i][j] = -1;
        dp[1][1] = 1;
        for (int i = 1; i <= r; ++ i)
        {
            scanf("%d%d", &x, &y);
            dp[x][y] = 0;
        }
        if (dp[n][m] == -1) f(n, m);
        printf("Case #%d: %d\n", times, dp[n][m]);
    }
}
