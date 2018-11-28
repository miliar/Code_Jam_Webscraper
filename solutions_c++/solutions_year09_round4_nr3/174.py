#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 100;
int n, m, kase, kases, a[MAXN][MAXN];
int nx, ny, g[MAXN][MAXN], sy[MAXN], cx[MAXN], cy[MAXN];

bool include(int x, int y)
{
    for (int i = 1; i <= m; ++i)
        if (a[x][i] <= a[y][i]) return false;
    return true;
}

int path(int u)
{
    for (int v = 1; v <= ny; ++v)
        if (g[u][v] && !sy[v])
        {
            sy[v] = 1;
            if (!cy[v] || path(cy[v]))
            {
                cx[u] = v;
                cy[v] = u;
                return 1;
            }
        }
    return 0;
}

int MaximumMatch()
{
    int i, ret = 0;
    nx = ny = n;
    memset(cx, 0, sizeof(cx)); memset(cy, 0, sizeof(cy));
    for (i = 1; i <= nx; ++i)
        if (!cx[i])
        {
            memset(sy, 0, sizeof(sy));
            ret += path(i);
        }
    return ret;
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    cin >> kases;
    for (kase = 1; kase <= kases; ++kase)
    {
        cin >> n >> m;
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= m; ++j)
                cin >> a[i][j];
        memset(g, 0, sizeof(g));
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j)
                if (i != j && include(i, j))
                    g[i][j] = 1;
        cout << "Case #" << kase << ": " << n - MaximumMatch() << endl;
    }

    return 0;
}
