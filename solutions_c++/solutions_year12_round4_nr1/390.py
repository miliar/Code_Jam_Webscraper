#include <stdio.h>
#include <cstdio>
#include <cstring>

int n, D;
int d[10001], l[10001], a[10002];

int main(int argc, char const *argv[]) {
    int T;
    scanf("%d", &T);
    for (int ti = 0; ti < T; ++ti) {
        printf("Case #%d: ", ti+1);
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d%d", d + i, l+i);
        }
        scanf("%d", &D);

        memset(a, -1, sizeof(a[0]) * (n+1));
        a[0] = d[0];

        int flag = 0;

        for (int i = 0; i < n; ++i) {
            // from i to next
            if (a[i] == -1) continue;
            if (d[i] + a[i] >= D) flag = 1;
            for (int j = i + 1; j < n; ++j) {
                if (a[i] + d[i] < d[j]) continue;
                // can catch $j
                int t1 = (d[j] - d[i]);
                int t2 = (l[j]);
                
                int x = t1 < t2 ? t1 : t2;
                // printf("x1, x2 = %d, %d\n", t1, t2);
                if (x > a[j]) {
                    a[j] = x;
                    // printf("a[%d] = %d\n", j, a[j]);
                    if (d[j] + a[j] >= D) flag = 1;
                }
            }
            if (flag) break;
        }

        printf("%s\n", flag ? "YES" :  "NO");
    }
    return 0;
}
