#include <cstdio>
#include <cstring>
#include <iostream>
#include <ctime>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int   maxn = 1000 + 10;
int         n, m, times, r[maxn], w, l;
int         x[maxn * 10], y[maxn * 10], lx[maxn * 10], tt;
int         pos[maxn], ansx[maxn], ansy[maxn];

void doit(int p, int q)
{
    if (y[q] == 0)
        if (x[q] == 0)
        {
            ansx[p] = ansy[p] = 0;
            ++tt;
            x[tt] = r[p], y[tt] = 0, lx[tt] = lx[q] - r[p];
            x[q] = x[q], y[q] = y[q] + r[p], lx[q] = r[p];
        }
        else
        {
            ansx[p] = x[q] + r[p], ansy[p] = 0;
            ++tt;
            x[tt] = x[q] + 2 * r[p], y[tt] = 0, lx[tt] = lx[q] - r[p] * 2;
            x[q] = x[q], y[q] = y[q] + r[p], lx[q] = r[p] * 2;
        }
    else
        if (x[q] == 0)
        {
            ansx[p] = 0, ansy[p] = y[q] + r[p];
            ++tt;
            x[tt] = r[p], y[tt] = y[q], lx[tt] = lx[q] - r[p];
            x[q] = x[q], y[q] = y[q] + 2 * r[p], lx[q] = r[p];
        }
        else
        {
            ansx[p] = x[q] + r[p], ansy[p] = y[q] + r[p];
            ++tt;
            x[tt] = x[q] + 2 * r[p], y[tt] = y[q], lx[tt] = lx[q] - 2 * r[p];
            x[q] = x[q], y[q] = y[q] + 2 * r[p], lx[q] = 2 * r[p];
        }
}

bool can(int p, int q)
{
    if (y[q] == 0)
        if (x[q] == 0)
            return true;
        else
            return x[q] + r[p] <= w;
    else
        if (x[q] == 0)
            return y[q] + r[p] <= l;
        else
            return r[p] * 2 <= lx[q] && y[q] + r[p] <= l;
}

bool cmp(int a, int b)
{
    return r[a] > r[b];
}

void solve()
{
    scanf("%d%d%d", &n, &w, &l);
    for (int i = 1; i <= n; ++i)
    {
        scanf("%d", r + i);
        pos[i] = i;
    }
    sort(pos + 1, pos + n + 1, cmp);
    tt = 1;
    x[1] = y[1] = 0, lx[1] = w;
    for (int i = 1; i <= n; ++i)
    {
        int k = -1;
        for (int j = 1; j <= tt; ++j)
            if (can(pos[i], j))
                if (k == -1 || x[k] > x[j])
                    k = j;
        if (k == -1)
            printf("FAIL");
        doit(pos[i], k);
    }
    for (int i = 1; i <= n; ++i)
        printf(" %d %d", ansx[i], ansy[i]);
    printf("\n");
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    srand((unsigned)time(NULL));
    scanf("%d", &times);
    for (int i = 1; i <= times; ++i)
    {
        printf("Case #%d:", i);
        solve();
    }
    return 0;
}
