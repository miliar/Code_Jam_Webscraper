#include <stdio.h>
#include <memory.h>

int d[10005] = { 0 }, v[10005] = { 0 }, z[10005] = { 0 };

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int c = 0, o = 0, i = 0, j = 0, dd = 0, now = 0, n = 0;
    scanf("%d", &c);
    for (o = 1; o <= c; o ++) {
        scanf("%d", &n);
        for (i = 0; i < n; i ++) {
            scanf("%d%d", d + i, v + i);
        }
        scanf("%d", d + n);
        v[i] = 0;
        memset(z, 0XFF, sizeof(z));

        z[0] = d[0];
        for (i = 0; i <= n; i ++) {
            for (j = i + 1; j <= n; j ++) {
                dd = d[j] - d[i];
                if (dd > z[i]) {
                    break;
                }
                if (dd > v[j]) {
                    now = v[j];
                }
                else {
                    now = dd;
                }
                if (now > z[j]) {
                    z[j] = now;
                }
            }
        }
        if (z[n] == -1) {
            printf("Case #%d: NO\n", o);
        }
        else {
            printf("Case #%d: YES\n", o);
        }
    }
    return 0;
}
                
