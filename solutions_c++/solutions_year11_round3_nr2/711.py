#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

int L, N, C;
long long t;
int a[1 << 10];
bool b[1 << 10];

long long calc() {
    double re = 0.0;

    for (int i = 0; i < N; ++i) {
        double d = a[i % C];

        if (b[i] && re >= t) {
            re += d;
        } else if (b[i] && re + 2 * d > t) {
            d -= 0.5 * (t - re);
            re = t + d;
        } else {
            re += 2 * d;
        }
    }

    return 2 * re;

/*
    long long re = 0;

    for (int i = 1; i < N; ++i) {
        long long d = a[(i - 1) % C];

        if (b[i - 1] && re + 2 * d > t) {
            d -= (t - re) / 2;
            re = t + d;
        } else {
            re += 2 * d;
        }
    }

    for (int i = 1; i < N; ++i) {
        long long d = a[(i - 1) % C];

        if (b[i - 1] && re + 4 * d > 2 * t) {
            d -= 2 * t - re;
            re = 2 * t + 2 * d;
        } else {
            re += 4 * d;
        }
    }
*/

    return re;
}

long long go() {
    memset(b, 0, sizeof b);

    long long re = calc();

    if (L >= 1) {
        for (int i = 0; i < N; ++i) {
            b[i] = true;
            re = min(re, calc());
            b[i] = false;
        }
    }

    if (L >= 2) {
        for (int i = 0; i < N; ++i) {
            b[i] = true;
            for (int j = 0; j < i; ++j) {
                b[j] = true;
                re = min(re, calc());
                b[j] = false;
            }
            b[i] = false;
        }
    }

    return re / 2;
}

int main() {
    int kases;

    scanf("%d", &kases);
    for (int kase = 1; kase <= kases; ++kase) {
        scanf("%d%lld%d%d", &L, &t, &N, &C);
        for (int i = 0; i < C; ++i) scanf("%d", a + i);

        printf("Case #%d: %lld\n", kase, go());
    }

    return 0;
}
