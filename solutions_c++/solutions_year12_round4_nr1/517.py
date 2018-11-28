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
#define N 10005
int n, m, len[N], dist[N], dp[N];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 1, i, j;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        for(i = 1; i <= n; i++)
        {
            scanf("%d%d", &dist[i], &len[i]);
        }
        scanf("%d", &m);
        memset(dp, 0, sizeof(dp));
        dp[1] = min(dist[1], len[1]);
        for(i = 1; i <= n; i++)
        {
            for(j = i + 1; j <= n; j++)
            {
                if(dist[i] + dp[i] >= dist[j])
                {
                    dp[j] = max(dp[j], min(dist[j] - dist[i], len[j]));
                }
                else
                {
                    break;
                }
            }
            if(dist[i] + dp[i] >= m)
                break;
        }
        if(i <= n)
            printf("Case #%d: YES\n", cas++);
        else
            printf("Case #%d: NO\n", cas++);
    }
    return 0;
}
