#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
struct data
{
    int d, l;
}d[10010];
int n, s;
int f[10010];
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca)
    {
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i)
            scanf("%d%d", &d[i].d, &d[i].l);
        scanf("%d", &s);
        memset(f, 0, sizeof(f));
        f[1] = d[1].d + min(d[1].d, d[1].l);
        for (int i = 2; i <= n; ++i)
            for (int j = 1; j < i; ++j)
                if ((f[j] >= d[i].d))
                    f[i] = max(f[i], d[i].d + min(d[i].l, d[i].d - d[j].d));
        bool flag = false;
        for (int i = 1; i <= n; ++i)
            if (f[i] >= s)
            {
                flag = true;
                break;
            }
        printf("Case #%d: %s\n", ca, (flag) ? "YES" : "NO");
    }
    return 0;
}
