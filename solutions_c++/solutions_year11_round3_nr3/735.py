#define MAXN 110

#include <cstdio>

int num[MAXN];

int main() {
    int i, j, n, l, h, t, cas;
    bool tag, tmp;

//    freopen("C-small-attempt0.in", "r", stdin);
//    freopen("C-small-attempt0.out", "w", stdout);

    scanf("%d", &t);
    for (cas = 1; cas <= t; cas++) {
        scanf("%d%d%d", &n, &l, &h);
        for (i = 0; i < n; i++) {
            scanf("%d", &num[i]);
        }
        tag = false;
        for (i = l; i <= h; i++) {
            tmp = true;
            for (j = 0; j < n; j++) {
                if ((num[j] % i) && (i % num[j])) {
                    tmp = false;
                    break;
                }
            }
            if (tmp) {
                tag = true;
                break;
            }
        }

        if (tag) printf("Case #%d: %d\n", cas, i);
        else printf("Case #%d: NO\n", cas);
    }

    return 0;
}
