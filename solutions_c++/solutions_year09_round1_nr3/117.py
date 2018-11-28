#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

typedef unsigned long long u64;

u64 ncr[41][41];
double a[2][41];

inline u64 gcd(u64 a, u64 b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

inline double prob(u64 den, u64 num) {
    u64 g = gcd(den, num);
    den /= g; num /= g;
    return (double)num / den;
}

double go(int c, int n) {
    int curr = 0, next = 1;

    a[curr][0] = 0;
    for (int i = 1; i <= c; i++) a[curr][i] = 0x7fffffff / 3;

    u64 all = ncr[c][n];

    while (true) {
        double maxDiff = 1e100;

        a[next][0] = 0;
        for (int need = 1; need <= c; need++) {
            a[next][need] = 1;

            int neededInBox = need; if (neededInBox > n) neededInBox = n;
            int notWanted = c - need;

            u64 rem = all;
            for (int whatWeGet = 1; whatWeGet <= neededInBox; whatWeGet++) {
                int notWantedSlots = n - whatWeGet;
                int remNeed = need - whatWeGet; if (remNeed < 0) remNeed = 0;
                if (neededInBox < whatWeGet || notWanted < notWantedSlots) continue;
                u64 poss = ncr[need][whatWeGet] * ncr[notWanted][notWantedSlots];

                a[next][need] += prob(all, poss) * a[curr][remNeed];
                rem -= poss;
            }
            a[next][need] += prob(all, rem) * a[curr][need];

            double diff = a[next][need] - a[curr][need]; if (diff < 0) diff = -diff;
            if (diff < maxDiff) maxDiff = diff;
        }

        curr = 1-curr; next = 1-next;
        if (maxDiff < 1e-9) break;
    }

    return a[curr][c];
}

int main() {
    ncr[0][0] = 1;
    for (int i = 0; i <= 40; i++) {
        ncr[i][0] = 1; ncr[i][i] = 1;
        for (int j = 1; j < i; j++) {
            ncr[i][j] = ncr[i-1][j-1] + ncr[i-1][j];
        }
    }

    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        int c, n; cin >> c >> n;
        printf("Case #%d: %.9lf\n", tt, go(c, n));
    }

    return 0;
}

