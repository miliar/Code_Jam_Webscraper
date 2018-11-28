#define INF 100000000

#include <cstdio>

int main() {
    int t, n, a, ret, m, tot, i;

//    freopen("C-large.in", "r", stdin);
//    freopen("C-large.out", "w", stdout);

    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        scanf("%d", &n);
        ret = tot = 0;
        m = INF;
        while (n--) {
            scanf("%d", &a);
            ret ^= a;
            tot += a;
            if (a < m) m = a;
        }
        printf("Case #%d: ", i + 1);
        if (ret) {
            printf("NO\n");
        }
        else {
            printf("%d\n", tot - m);
        }
    }

    return 0;
}
