#include <cstdio>

int main() {
    int n, k;
    int nCase;
    scanf("%d", &nCase);
    for (int iCase = 1; iCase <= nCase; ++iCase) {
        scanf("%d%d", &n, &k);
        int base = (1 << n) - 1;
        printf("Case #%d: %s\n", iCase, ((k & base) == base) ? "ON" : "OFF");
    }

    return 0;
}
