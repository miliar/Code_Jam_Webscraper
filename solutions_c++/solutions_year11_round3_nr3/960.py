#include <iostream>
#include <stdio.h>

using namespace std;

int a[101];

int main() {
    freopen("3.in", "r", stdin);
    freopen("3.out", "w", stdout);
    int t, tt, n, l, h, i, j;
    scanf("%d", &t);
    for (tt = 1; tt <= t; tt++) {
        printf("Case #%d: ", tt);
        scanf("%d%d%d", &n, &l, &h);
        for (i = 0; i < n; i++) scanf("%d", &a[i]);
        for (i = l; i <= h; i++) {
            bool flag = 1;
            for (j = 0; j < n; j++)
                if (a[j] % i && i % a[j]) {
                    flag = 0;
                    break;
                 }
            if (flag) break;
        }
        if (i == h + 1) printf("NO\n");
        else printf("%d\n", i);
    }
    return 0;
}
