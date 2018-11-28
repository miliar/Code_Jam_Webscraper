
#include <iostream>
#include <vector>

using namespace std;

double e[1001];
double fact[1001];
double choose[1001][1001];
double derange[1001];

void init() {
    e[0] = 0;
    fact[0] = 1;
    derange[0] = 1;
    for(int i = 1; i <= 1000; i++) {
        fact[i] = 1.0 * i * fact[i-1];

        choose[i][0] = choose[i][i] = 1;
        for(int j = 1; j < i; j++)
            choose[i][j] = choose[i][j-1] * (i-j+1) / j;

        derange[i] = i * derange[i-1] + 1 - 2 * (i & 1);

        // fix 0 <= j <= i to be deranged, so i-j are correct
        // e[i] = 1 + sum c(i, j) * derange(j) * e[j]
        // e[i] * (1 - derange[i]) = 1 + sum for j < i
        e[i] = 1;
        for(int j = 0; j < i; j++)
            e[i] += choose[i][j] * derange[j] * e[j] / fact[i];
        e[i] /= (1 - derange[i] / fact[i]);

        if(i < 50) {
            printf("> %d, fact: %.0lf, e: %.5lf\n", i, fact[i], e[i]);
            /*
            printf("derange: %.0lf\n", derange[i]);
            printf("choose:");
            for(int j = 0; j <= i; j++)
                printf(" %.0lf", choose[i][j]);
            printf("\n");

            double sum = 0;
            for(int j = 0; j <= i; j++)
                sum += choose[i][j] * derange[j] / fact[i];
            printf("sum: %.4lf\n", sum); // 1.00
            */
        }
        // answer is just e[i] = i (!!!)
    }
}

double solve() {
    int N;
    scanf("%d", &N);

    int off = 0;
    for(int i = 0; i < N; i++) {
        int a;
        scanf("%d", &a);
        if(a-1 != i)
            off++;
    }
    return off;
    //return e[off];
}

int main() {
    //init();

    int T;
    scanf("%d", &T);
    for(int i = 0; i < T; i++) {
        printf("Case #%d: %.10lf\n", i+1, solve());
    }

    return 0;
}
