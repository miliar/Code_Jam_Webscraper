#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int T, l, n, c;
int a[1000000];
 __int64 t, sum, ans;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        printf("Case #%d: ", cas);
        scanf("%d%I64d%d%d", &l, &t, &n, &c);
        t = t / 2;
        sum = ans = 0;
        for (int i = 0; i < c; i++)
        {
            scanf("%d", &a[i]);
            ans += a[i] * 2;
        }
        for (int i = c; i < n; i++)
        {
            a[i] = a[i % c];
            ans += a[i] * 2;
        }
        for (int i = 0; i < n; i++)
        {
            if (sum + a[i] >= t)
            {
                    a[i] -= t - sum;
                    sort(a + i, a + n);
                    for (int j = 1; j <= l && n - j >= i; j++)
                        ans -= a[n - j];
                    break;
            }
            else sum += a[i];
        }
        printf("%I64d\n", ans);
    }
    return 0;
}
