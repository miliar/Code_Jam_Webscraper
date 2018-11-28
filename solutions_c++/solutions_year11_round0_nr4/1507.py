#include <cstdio>

int main() {

        int T, n;

        scanf("%d", &T);
        for (int t = 1; t <= T; t++) {
                scanf("%d", &n);
                int a;
                int m = 0;
                for (int i = 0; i < n; i++) {
                        scanf("%d", &a);
                        if (a == i+1) m++;
                }
                printf("Case #%d: %.6f\n", t, (float)(n-m));
        }
        return 0;
}

