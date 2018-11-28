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
int add[6] = {0, 1, 2, 1, 2, 2};
int cnt[6] = {0, 1, 2, 2, 3, 4};
int n, s, p, sc[105], dp[105][105];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cas = 1, i, j, k;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%d", &n, &s, &p);
        for(i = 1; i <= n; i++)
        {
            scanf("%d", &sc[i]);
        }
        memset(dp, -1, sizeof(dp));
        dp[0][0] = 0;
        for(i = 0; i < n; i++)
        {
            for(j = 0; j <= s; j++)
            {
                if(dp[i][j] != -1)
                {
                    for(k = 0; k < 6; k++)
                    {
                        if(sc[i + 1] >= cnt[k] && (sc[i + 1] - cnt[k]) % 3 == 0)
                        {
                            int cur = 0;
                            if((((sc[i+1] - cnt[k]) / 3) + add[k]) >= p)
                                cur++;
                            if(add[k] == 2 && j + 1 <= s)
                            {
                                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + cur);
                            }
                            if(add[k] != 2)
                                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + cur);
                        }
                    }
                }
            }
        }
        printf("Case #%d: %d\n", cas++, dp[n][s]);
    }
    return 0;
}
