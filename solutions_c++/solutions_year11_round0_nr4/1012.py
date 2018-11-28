#include <cstdio>
#include <limits>
#include <algorithm>

using namespace std;

double prob[1001][1001];
double invfact[1001];
double expected[1001];

int main() {
    invfact[0] = 1;
    for(int i = 1; i <= 1000; i++)
        invfact[i] = invfact[i-1]/i;

    for(int i = 1; i <= 1000; i++) {
        prob[i][i] = invfact[i];
        for(int j = i-1; j >= 0; j--)
            prob[i][j] = invfact[j] - prob[i][j+1]/(j+1);
    }

    expected[0] = 0;
    for(int i = 1; i <= 1001; i++) {
        expected[i] = numeric_limits<double>::infinity();
        for(int k = 1; k <= i; k++) {
            double strategy = 1;
            for(int j = 1; j <= k; j++)
                strategy += prob[k][j] * expected[i-j];
            strategy /= (1-prob[k][0]);
            expected[i] = min(strategy, expected[i]);
        }
    }

    int t;
    scanf("%d", &t);
    for(int z = 1; z <= t; z++) {
        int n, right = 0, tmp;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            scanf("%d", &tmp);
            right += i == tmp-1;
        }

        printf("Case #%d: %.6lf\n", z, expected[n-right]);
    }
}
