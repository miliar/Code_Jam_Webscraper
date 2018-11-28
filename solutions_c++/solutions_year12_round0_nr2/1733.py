#include <cstdio>
#include <cstring>

int n, s, p, t, T, ans;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("solve.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    { 
        scanf("%d%d%d", &n, &s, &p);
        ans = 0;
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &t);
            if (p - 1 < 0 && p * 3 <= t) ans++;
            else if (p - 1 >= 0 && p * 3 - 2 <= t) ans++;
            else if (p - 2 >= 0 && p * 3 - 4 <= t && s)
            {
                 ans++;
                 s--;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
