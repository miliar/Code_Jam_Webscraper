#include <cstdio>

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, n, k, m, cas = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d %d", &n, &k);
        m = 1 << n;
        printf("Case #%d: ", ++cas);
        if (k % m == m - 1)
            puts("ON");
        else
            puts("OFF");
    }
    return 0;
}
