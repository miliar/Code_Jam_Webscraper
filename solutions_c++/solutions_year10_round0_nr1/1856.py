#include <stdio.h>

int T;
int N, K;
int base[31];
int step[31];
int i;
int c;

int main() {

    for (i = 1; i <= 30; i++) {
        base[i] = (1 << i) - 1;
        step[i] = (1 << i);
    }

    scanf("%d", &T);

    c = 0;
    while (T--) {
        scanf("%d %d", &N, &K);

        c++;
        if ((K - base[N]) % step[N] == 0)
            printf("Case #%d: ON\n", c);
        else
            printf("Case #%d: OFF\n", c);
    }

    return 0;
}