#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int   maxn = 10000 + 10;
int         n, m, times, a[maxn], ans[maxn], p[maxn];
int         h, t;

int find(int x)
{
    for (int i = h; i <= t; ++i)
        if (a[i] == x)
            return i;
    return maxn;
}

void solve()
{
    scanf("%d", &n);
    for (int i = 1; i < n; ++i)
        scanf("%d", p + i);
    a[h = 1] = n - 1;
    a[t = 2] = n;
    for (int i = n - 2; i; --i)
    {
        int j = find(p[i]);
        if (j > t)
        {
            printf(" Impossible\n");
            return;
        }
        for (int k = t + 1; k > j; --k)
            a[k] = a[k - 1];
        ++t;
        a[h = j] = i;
    }
    ans[n] = 0;
    for (int i = n - 1; i; --i)
        ans[a[i]] = ans[p[a[i]]] - (n - i) * (p[a[i]] - a[i]);
    int mini = 0;
    for (int i = 1; i <= n; ++i)
        mini = min(mini, ans[i]);
    for (int i = 1; i <= n; ++i)
        printf(" %d", ans[i] - mini);
    printf("\n");
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    scanf("%d", &times);
    for (int i = 1; i <= times; ++i)
    {
        printf("Case #%d:", i);
        solve();
    }
    return 0;
}
