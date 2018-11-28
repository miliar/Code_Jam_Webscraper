#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int   maxn = 1000 + 10;
int         n, m, a[maxn], p[maxn], pos[maxn];

bool cmp(int x, int y)
{
    if (p[x] != p[y])
        return p[x] > p[y];
    if (a[x] != a[y])
        return a[x] > a[y];
    return x < y;
}

void solve()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i)
        scanf("%d", &a[i]);
    for (int i = 1; i <= n; ++i)
        scanf("%d", &p[i]);
    for (int i = 1; i <= n; ++i)
        pos[i] = i;
    sort(pos + 1, pos + n + 1, cmp);
    for (int i = 1; i <= n; ++i)
        printf(" %d", pos[i] - 1);
    printf("\n");
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int times;
    scanf("%d", &times);
    for (int i = 1; i <= times; ++i)
    {
        printf("Case #%d:", i);
        solve();
    }
    return 0;
}
