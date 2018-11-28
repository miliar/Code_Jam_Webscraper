
#include <algorithm>
#include <cstdio>

using namespace std;

int B[1000], E[1000], w[1000];
int order[1000];

bool cmp(int i, int j) {
    return w[i] < w[j];
}

double solve() {
    int X, S, R;
    double t;
    int N;
    scanf("%d%d%d%lf%d", &X, &S, &R, &t, &N);
    for(int i = 0; i < N; i++) {
        scanf("%d%d%d", &B[i], &E[i], &w[i]);
    }

    for(int i = 0; i < N; i++) {
        order[i] = i;
        X -= E[i] - B[i];
    }
    sort(order, order + N, cmp);

    double total = 0;
    double dist = min(1.0 * X, t * R);
    total += 1.0 * dist / R + 1.0 * (X - dist) / S;
    t -= dist / R;

    for(int j = 0; j < N; j++) {
        int i = order[j];
        dist = min(1.0 * (E[i] - B[i]), t * (R + w[i]));
        total += 1.0 * dist / (R + w[i]) + 1.0 * (E[i] - B[i] - dist) / (S + w[i]);
        t -= dist / (R + w[i]);
    }

    return total;
}

int main() {
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++)
        printf("Case #%d: %.10lf\n", i, solve());
}
