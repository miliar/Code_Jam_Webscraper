#include <stdio.h>
#include <stdlib.h>

int main() {
    int T, N, K;

    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        scanf("%d %d", &N, &K);
        if (((K + 1) % (1 << N)) == 0)
            printf("Case #%d: ON\n", (i + 1));
        else
            printf("Case #%d: OFF\n", (i + 1));
    }

    return 0;
}




