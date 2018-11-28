#include <cstdio>
#include <cstring>
#include <cstdlib>

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++)
    {
        int n, s, p, ti, ca = 0, cb = 0, cc = 0, ans = 0;
        scanf("%d%d%d", &n, &s, &p);
        for (int i = 1; i <= n; i++)
        {
            scanf("%d", &ti);
            if (p == 0)
                    ca++;
            else
            if (p == 1)
            {
                    if (ti == 0)
                        cc++;
                    else
                        ca++;
            }
            else
            if (ti >= 3 * p - 2)
                ca++;
            else
            if (ti >= 3 * p - 4)
                cb++;
            else
                cc++;
        }
        ans += ca;
        if (cb >= s)
            ans += s;
        else
            ans += cb;
        printf("Case #%d: %d\n", cases, ans);
    }

    return 0;
}
