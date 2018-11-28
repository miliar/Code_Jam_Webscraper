#include <cstdio>
#include <cstring>

const int limitSize = 1024 + 10;

int P, n;

int cost[limitSize][limitSize];
int M[limitSize];

void init()
{
    scanf("%d", &P);

    memset(cost, 0, sizeof(cost));
    n = 1 << P;

    for (int i = 0; i < n; i ++)
        scanf("%d", M + i);

    for (int w = 2; w <= n; w *= 2)
    {
        for (int i = 0; i < n; i += w)
            scanf("%d", &cost[i][i + w]);
    }
}

int opt[limitSize][limitSize][11];

int dp(int p, int r, int x)
{
    if (opt[p][r][x] >= 0)
        return opt[p][r][x];

    int mx = 123456;
    for (int i = p; i < r; i ++)
        if (M[i] < mx) mx = M[i];

    if (p + 2 == r)
    {
        if (mx == x)
            opt[p][r][x] = cost[p][r];
        else
            opt[p][r][x] = 0;
    }
    else
    {
        int m = (p + r) / 2;
        opt[p][r][x] = dp(p, m, x) + dp(m, r, x) + cost[p][r];

        if (mx > x)
        {
            int tmp = dp(p, m, x + 1) + dp(m, r, x + 1);
            if (tmp < opt[p][r][x])
                opt[p][r][x] = tmp;
        }
    }

    return opt[p][r][x];
}

void solve()
{
    memset(opt, 0xff, sizeof(opt));

    printf("%d\n", dp(0, n, 0));
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T, t;
    scanf("%d", &T);

    for (t = 1; t <= T; t ++)
    {
        init();
        printf("Case #%d: ", t);

        solve();
    }

    return 0;
}
