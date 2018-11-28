#define MAXN 1010

#include <cstdio>

int main() {
    int n, t, i, ret, cas, a;

//    freopen("D-large.in", "r", stdin);
//    freopen("D-large.out", "w", stdout);

    scanf("%d", &t);
    for (cas = 0; cas < t; cas++) {
        scanf("%d", &n);
        ret = 0;
        for (i = 0; i < n; i++) {
            scanf("%d", &a);
            if (a != i + 1) ret++;
        }
        printf("Case #%d: %d.000000\n", cas + 1, ret);
    }

    return 0;
}
