#include <stdio.h>

int main() {
    int T;
    scanf("%d\n", &T);
    for (int num = 1; num <= T; ++num) {
        int N;
        int C[1000];
        scanf("%d\n", &N);
        int tot = 0;
        int tot2 = 0;
        int small = 20000000;
        for (int i = 0; i < N; ++i) {
            scanf("%d", &C[i]);
            tot ^= C[i];
            if (small > C[i])
                small = C[i];
            tot2 += C[i];
        }

        printf("Case #%d: ", num);
        if (tot != 0) {
            printf("NO\n");
            continue;
        }
        printf("%d\n", tot2 - small);
    }
    return 0;
}
