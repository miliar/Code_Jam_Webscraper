#include <stdio.h>

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, cas = 0, n, s, p, t;
    scanf("%d", &T);
    while (T--)
    {
        int cnt = 0;
        scanf("%d%d%d", &n, &s, &p);
        for (int i = 0; i < n; ++i)
        {
            int v = 0;
            scanf("%d", &t);
            if (t%3 == 0) v = t / 3;
            else v = t / 3 + 1;
            if (v >= p) ++cnt;
            else if (s > 0 && t >= p && t >= 3*p - 4) ++cnt, --s;
        }
        printf("Case #%d: %d\n", ++cas, cnt);
    }
    return 0;
}
