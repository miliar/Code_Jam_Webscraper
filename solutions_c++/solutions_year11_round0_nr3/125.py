#include <stdio.h>

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, n, t;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d", &n);
        int v = 0, sum = 0, minv = 1000000000;
        while (n--) {
            scanf("%d", &t);
            v ^= t;
            sum += t;
            if (t < minv) minv = t;
        }
        printf("Case #%d: ", cas);
        if (v) puts("NO");
        else printf("%d\n", sum - minv);
    }
    return 0;
}
