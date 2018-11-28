#include <cstdio>
#include <cstring>

const int MAXN = 100000;
const int MAXC = 42;

typedef long long LL;

double dp[MAXN][MAXC];
LL C[MAXC][MAXC];

void Init()
{
    C[0][0] = 1;
    for (int i = 1; i < MAXC; i++)
    {
        C[i][0] = C[i][i] = 1;
        for (int j = 1; j < i; j++)
            C[i][j] = C[i - 1][j] + C[i - 1][j - 1];
    }
}

int main()
{
    Init();
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int n, c;
        scanf("%d%d", &c, &n);
        if (c == n)
        {
            printf("Case #%d: 1.000000\n", cas);
            continue;
        }
        for (int i = 0; i < MAXC; i++)
            dp[1][i] = 0.0;
        dp[1][n] = 1.0;
        double res = 0.0;
        for (int i = 2; i < MAXN; i++)
        {
            for (int j = n; j <= c; j++)
            {
                dp[i][j] = 0.0;
                for (int k = n; k <= j; k++)
                {
                    if (j == c && k == c)
                        continue;
                    int d = j - k;
                    if (n < d)
                        continue;
//printf("i = %d, j = %d, k  =%d, d = %d, n = %d, %d * %d / %d\n", i, j, k, d, n, C[k][n - d], C[c - k][d], C[c][n]);
                    dp[i][j] += dp[i - 1][k] * C[k][n - d] * C[c - k][d] / C[c][n];
                }
//printf("dp[%d][%d] = %lf\n", i, j, dp[i][j]);
            }
//printf("dp[%d][%d] = %lf\n", i, c, dp[i][c]);
            res += dp[i][c] * i;
        }
        printf("Case #%d: %lf\n", cas, res);
    }
    return 0;
}
