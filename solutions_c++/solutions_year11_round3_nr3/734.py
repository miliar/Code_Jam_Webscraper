#include <cstdio>

int a[10010];

int main(void) {
    int test; scanf("%d", &test);

    for (int cs = 0; cs < test; ++cs) {
        int n, l, h; scanf("%d%d%d", &n, &l, &h);

        for (int i = 0; i < n; ++i) {
            scanf("%d", a+i);
        }

        int sol = -1;
        for (int i = l; i <= h; ++i) {
            int ok = 1;
            for (int j = 0; j < n; ++j) {
                if (i % a[j] == 0 || a[j] % i == 0) {

                } else {
                    ok = 0;
                    break;
                }
            }
            if (ok) {
                sol = i;
                break;
            }
        }

        printf("Case #%d: ", cs+1);
        if (sol == -1) puts("NO"); else printf("%d\n", sol);
    }
return 0;
}
