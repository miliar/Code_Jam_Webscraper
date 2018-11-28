#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int   maxn = 10000 + 10;
int f[maxn], d[maxn], a[maxn], n, m;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int times;
    scanf("%d", &times);
    for (int l = 1; l <= times; ++l)
    {
        printf("Case #%d: ", l);
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            scanf("%d%d", a + i, d + i);
        scanf("%d", &m);
        memset(f, 0, sizeof(f));
        f[0] = a[0];
        bool can = false;
        for (int i = 0; i < n; ++i)
        {
            if (a[i] + f[i] >= m)
                can = true;
            for (int j = i + 1; j < n; ++j)
                if (a[i] + f[i] >= a[j])
                    f[j] = max(f[j], min(a[j] - a[i], d[j]));
                else
                    break;
        }
        if (can)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
