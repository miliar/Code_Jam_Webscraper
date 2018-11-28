#include <cstdio>

int cT, nT, n, k;

int main() {
    scanf("%d", &nT);
    for (int cT = 1; cT <= nT; ++cT) {
        printf("Case #%d: ", cT);
        scanf("%d%d", &n, &k);
        ++k;
        if (k % (1 << n) == 0) puts("ON"); else puts("OFF");
    }
}
