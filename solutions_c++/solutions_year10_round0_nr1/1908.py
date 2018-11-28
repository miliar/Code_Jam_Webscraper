#include <stdio.h>

int main() {
    int caseSize, n, k;
    scanf("%d", &caseSize);
    for (int T = 1; T <= caseSize; T++) {
        scanf("%d%d", &n, &k);
        printf("Case #%d: ", T);
        if ((k % (1 << n)) == (1 << n) - 1) {
            puts("ON");
        } else {
            puts("OFF");
        }
    }
    return 0;
}
