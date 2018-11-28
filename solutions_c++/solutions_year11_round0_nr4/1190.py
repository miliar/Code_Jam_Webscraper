#include <cstdio>

int main() {
 //   freopen("d.in", "r", stdin);
 //   freopen("d.out", "w", stdout);
    int T, n, cas = 1, x;
    scanf("%d", &T);
    while (T--) {
        double ans = 0;
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i) {
            scanf("%d", &x);
            ans += (x != i);
        }
        printf("Case #%d: %.6lf\n", cas++, ans);
    }
    return 0;
}
