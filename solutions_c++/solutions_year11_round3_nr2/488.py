// B CZM1.0
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

#define PI acos(-1.0)
#define eps 1e-5
#define oo 10000000000000000LL
const static int maxN = 10000;
typedef long long INT64;

INT64 a[maxN];

INT64 dp[1001][3];
INT64 DP(INT64 L, INT64 t, INT64 N, INT64 C)
{
    INT64 ret = oo;
    int i, j;
    for (i = 0; i <= L; i++)
    {
        dp[0][i] = oo;
    }
    dp[0][0] = 0;
    for (i = 1; i <= N; i++)
    {
        for (j = 0; j <= L; j++)
        {
            dp[i][j] = dp[i-1][j] + a[(i - 1) % C] * 2;
        }
        for (j = 1; j <= L; j++)
        {
            if (dp[i-1][j-1] >= t)
            {
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + a[(i - 1) % C]);
            }
            else if (a[(i - 1) % C] * 2 > t - dp[i-1][j-1])
            {
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + (t - dp[i-1][j-1]) + (a[(i - 1) % C] - (t - dp[i-1][j-1]) / 2));
            }
        }
    }
    for (i = 0; i <= L; i++)
    {
        ret = min(ret, dp[N][i]);
    }
    return ret;
}

int main()
{
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0.out", "w", stdout);
    int T;
    int cas = 1;
    INT64 L, t, N, C;
    int i;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%I64d%I64d%I64d%I64d", &L, &t, &N, &C);
        for (i = 0; i < C; i++)
        {
            scanf("%I64d", &a[i]);
        }
        printf("Case #%d: %I64d\n", cas++, DP(L, t, N, C));
    }
    return 0;
}
