#include <stdio.h>
#include <cstring>

int g[200][200], n, k;
int lik[200], vis[200], p[200][200];

bool check(int a, int b)
{
    for(int i=1; i<=k; ++i)
        if(p[a][i] <= p[b][i]) return 0;
    return 1;
}

void init()
{
    scanf("%d%d", &n, &k);
    for(int i=1; i<=n; ++i)
    {
        for(int j=1; j<=k; ++j) scanf("%d", &p[i][j]);
    }

    memset(g, 0, sizeof g);
    for(int i=1; i<=n; ++i)
    {
        for(int j=1; j<=n; ++j)
            if(check(i, j)) g[i][j] = 1;
    }
}

bool can(int now)
{
    for(int i=1; i<=n; ++i)
    {
        if(!g[now][i]) continue;

        if(!vis[i])
        {
            vis[i] = 1;
            if(lik[i] == -1 || can(lik[i]))
            {
                lik[i] = now;
                return 1;
            }
        }
    }
    return 0;
}

void solve()
{
    int ans = 0;
    memset(lik, -1, sizeof lik);

    for(int i=1; i<=n; ++i)
    {
        memset(vis, 0, sizeof vis);
        if(can(i)) ans++;
    }
    printf("%d\n", n - ans);
}

int main()
{
    int t, tc = 0;
    scanf("%d", &t);
    while(t--)
    {
        init();
        printf("Case #%d: ", ++tc);
        solve();
    }
    return 0;
}

