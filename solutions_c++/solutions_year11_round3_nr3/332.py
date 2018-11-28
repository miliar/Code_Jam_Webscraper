#include <cstdio>

int f[123];

int main() {
    int nt, cases = 1;
    scanf(" %d", &nt);
    while (nt--) {
        int n, L, H;
        scanf(" %d%d%d", &n, &L, &H);
        for (int i = 0; i < n; i++)
            scanf(" %d", &f[i]);
        int res = -1;
        for (int i = L; i <= H; i++) {
            bool ok = true;
            for (int j = 0; j < n; j++)
                if (i % f[j] && f[j] % i) {
                    ok = false;
                    break;
                }
            if (ok) {
                res = i;
                break;
            }
        }
        printf("Case #%d: ", cases++);
        if (res == -1)
            printf("NO\n");
        else printf("%d\n", res);
        
    }

    return 0;
}
