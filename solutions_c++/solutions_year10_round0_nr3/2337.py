#include <cstdio>

int T;
int r, k, n;
int g[10000];

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int tt, i, cost, take, p, q, q1;
    scanf("%d", &T);
    for (tt = 1; tt <= T; tt++) {
        scanf("%d%d%d", &r, &k, &n);
        for (i = 0; i < n; i++) scanf("%d", &g[i]);
        cost = 0;
        p = 0;
        q = n;
        for (; r > 0 && p < q; r--) {
            take = 0;
            q1 = q;
            while (take + g[p] <= k && p < q1) {
                take += g[p];
                g[q] = g[p];
                p++;
                q++;
            }
            cost += take;
        }
        printf("Case #%d: %d\n", tt, cost);
    }
    return 0;
}
