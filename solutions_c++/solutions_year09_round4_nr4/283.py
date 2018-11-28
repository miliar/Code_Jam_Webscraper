
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAX_N = 40 + 5;

int N;
int x[MAX_N];
int y[MAX_N];
int r[MAX_N];

double run() {
    if (N == 1)
        return 0.0 + r[0];
    if (N == 2)
        return 0.0 + max(r[0], r[1]);
    if (N == 3) {
        double res = 1e10;
        for (int i = 0; i < N; ++i)
            for (int j = i + 1; j < N; ++j) {
                double crnt = 0.0;
                for (int k = 0; k < N; ++k)
                    if (i != k && j != k)
                        crnt = 0.0 + r[k];
                double dist = sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]));
                dist += r[i] + r[j];
                dist /= 2.0;
                if (crnt < dist)
                    crnt = dist;
                if (res > dist)
                    res = dist;
            }
        return res;
    }
    return -1.0;
}

int main() {
    int tst;
    scanf("%d", &tst);
    for (int cas = 0; cas < tst; ++cas) {
        scanf("%d", &N);
        for (int i = 0; i < N; ++i)
            scanf("%d %d %d", &x[i], &y[i], &r[i]);
        printf("Case #%d: %.6lf\n", cas + 1, run());
    }
    return 0;
}