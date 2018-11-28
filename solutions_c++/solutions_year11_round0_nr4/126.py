#include <stdio.h>

//double d[1010], fac[1010], a[1010], f[1010];

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
//    d[0] = 1.0; fac[0] = 1.0;
//    for (int i = 1; i <= 1000; ++i) {
//        fac[i] = fac[i-1] * i;
//        if (i&1) d[i] = d[i-1] - 1/fac[i];
//        else d[i] = d[i-1] + 1/fac[i];
//    }
//    f[0] = f[1] = 0.0;
//    for (int i = 2; i <= 1000; ++i) {
//        double sum = 0.0, tot = 0.0;
//        for (int j = 0; j <= i; ++j) {
//            a[j] = d[j] / fac[i-j];
//            sum += a[j];
//            if (j != i) tot += a[j] * f[j];
//        }
//        f[i] = (sum + tot) / (1 - a[i]);
//    }
//    for (int i = 0; i <= 100; ++i) printf("%.6f\n", f[i]);

    int T, n, t;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d", &n);
        int cnt = 0;
        for (int i = 1; i <= n; ++i) {
            scanf("%d", &t);
            cnt += (t != i);
        }
        printf("Case #%d: %.6f\n", cas, (double)cnt);
    }
    return 0;
}
