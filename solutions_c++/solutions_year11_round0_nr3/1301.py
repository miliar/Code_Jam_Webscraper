#include <cstdio>

int main() {
    int T;
    freopen("C-large.in", "r", stdin);
    freopen("c.out", "w", stdout);
    
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int n, sg = 0, x, m = 1000001, sum = 0;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &x);
            sg ^= x;
            sum += x;
            m = (m < x ? m : x);
        }
        if (sg == 0) {
            printf("Case #%d: %d\n", t, sum - m);
        } else {
            printf("Case #%d: NO\n", t);
        }
    }
}
