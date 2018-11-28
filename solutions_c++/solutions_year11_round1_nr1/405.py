#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int gcd(int a, int b) {
    if (!b) return a;
    return gcd(b, a % b);
}

int main(void) {
    int nC;
    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        int N, pD, pG;
        scanf("%d %d %d", &N, &pD, &pG);
        printf("Case #%d: ", cC + 1);

        if (pG == 100 || pG == 0) {
            if (pD == pG)
                printf("Possible\n");
            else
                printf("Broken\n");
            continue;
        } else {
            // pG doesn't matter
            int divisor = gcd(100, pD);
            int minGames = 100 / divisor;
            if (N >= minGames) printf("Possible\n");
            else printf("Broken\n");
        }
    }
    return 0;
}
