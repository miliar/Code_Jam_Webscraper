#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define INF 0x3fffffff
#define LL long long
#define N 100005
double pro[N], dp[N];
int n, m;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, i, cas = 0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &n, &m);
        for(i = 1; i <= n; i++)
        {
            scanf("%lf", &pro[i]);
        }
        double right = 1.0;
        dp[0] = 0;
        for(i = 1; i <= n; i++)
        {
            dp[i] = dp[i - 1] + right * (1.0 - pro[i]);
            right *= pro[i];
        }
        double ans = INF;
        ans = min(ans, dp[n] * (2 * m - n + 2) + right * (m - n + 1));
        ans = min(ans, (dp[n] + right) * (m + 2));
        for(i = 1; i <= n; i++)
        {
            double cur = 0;
            if(i < n)
            {
                cur += dp[n - i] * (2 * i + 2 * m - n + 2);
                cur += (1.0 - dp[n - i]) * (2 * i + m - n + 1);
            }
            else
            {
                cur += n + m + 1;
            }
            ans = min(ans, cur);
        }
        printf("Case #%d: %lf\n", ++cas, ans);
    }
    return 0;
}
/*
3
2 5
0.6 0.6
1 20
1
3 4
1 0.9 0.1

            double sum = 0;
            sum += dp[i] * (m - n + 1 + m + 1);
            sum += dp[i] * (1 + m + 1);
            if(i <= n)
            {
                sum += dp[i] * (n - i) * ((n - i + 1) + (m - n + 1 + m + 1));
                sum += dp[i] * i *((2 * n - i + 1) + (m - n + 1));
            }
            else
            {
                sum += dp[i] * n * ((1 + n) + (m - n + 1));
            }
            ans += sum;
*/
