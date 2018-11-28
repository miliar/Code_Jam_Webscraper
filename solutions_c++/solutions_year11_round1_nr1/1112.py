#include <cstdlib>
#include <cstdio>

int max(int a, int b) {
    return a > b ? a : b;
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) {

        unsigned long long int N, PD, PG;
        scanf("%lld%lld%lld", &N, &PD, &PG);

        if (PG == 100) {
            if (PD == 100) {
                printf("Case #%d: Possible\n", i);
                continue;
            } else {
                printf("Case #%d: Broken\n", i);
                continue;
            }
        }

        if (PG == 0) {
            if (PD == 0) {
                printf("Case #%d: Possible\n", i);
                continue;
            } else {
                printf("Case #%d: Broken\n", i);
                continue;
            }
        }

        int wielD = 1;

        if (PD % 25 != 0) {
            wielD *= 5;
        }
        if (PD % 5 != 0) {
            wielD *= 5;
        }
        if (PD % 4 != 0) {
            wielD *= 2;
        }
        if (PD % 2 != 0) {
            wielD *= 2;
        }

        if (wielD > N) {
            printf("Case #%d: Broken\n", i);
            continue;
        }

        unsigned long long int wygrane = PD * wielD / 100;
        unsigned long long int przegrane = wielD - wygrane;

        unsigned long long int PGn = PG * max(wygrane, przegrane);
        unsigned long long int PGn1 = (100-PG)* max(wygrane, przegrane);

        if ( PGn - wielD >= 0 && PGn1 - (N-wielD) >= 0 ) {
            printf("Case #%d: Possible\n", i);
            continue;
        } else {
            printf("Case #%d: Broken\n", i);
            continue;
        }

    }
    return 0;
}

