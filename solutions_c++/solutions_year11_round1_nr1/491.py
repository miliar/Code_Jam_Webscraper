#include <cstdio>

int main (void)
{
    int T, t;
    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        long long int N, PD, PG;
        scanf("%lld %lld %lld", &N, &PD, &PG);
        bool possible = true;
        if (N < 100) {
            possible = false;
            for (long long int n = 1; n <= N; n++) {
                if ((n * PD) % 100 == 0) {
                    possible = true;
                    break;
                }
            }
        }
        if (PG == 100 && PD < 100) {
            possible = false;
        }
        if (PG == 0 && PD > 0) {
            possible = false;
        }
        printf("Case #%d: ", t);
        if (possible) {
            printf("Possible\n");
        } else {
            printf("Broken\n");
        }
    }
    return 0;
}
