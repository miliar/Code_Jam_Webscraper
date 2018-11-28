#include <cctype>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <complex>

using namespace std;

#define LET(k,val) typeof(val) k = (val)

#define FOR(k,b,e) for(LET(k,b); k < (e); ++k) // (b -> e-1)
#define REP(x,n) for(int x = 0; x < (n); ++x) // (0 -> n-1)


const int INF = 1000000001;
const double EPS = 10e-9;

int tab[501];
const int MOD = 100003;

int licznik = 0;

int rank(vector<bool>& v, int k) {
    int rank = 1;
    for (int i = k - 3; i >= 0; --i) {
        if (v[i]) ++rank;
    }
    return rank;
}

void f(vector<bool>& v, int n) {
    int r = rank(v, n);
    while (true) {
        if (r == 1) {
            licznik = (licznik + 1) % MOD;
            break;
        }
        if (v[r - 2]) {
            r = rank(v, r);
        } else {
            break;
        }
    }
}

void subset(int n) {
    vector<bool> B(n, 0);
    f(B, n + 2);
    for (int i = 0, p = 0, j; p < n;) {
        for (p = 0, j = ++i; j & 1; p++) j >>= 1;
        if (p < n) {
            B[p] = !B[p];
            f(B, n + 2);
        }
    }
}

int main() {
    REP(i, 501) {
        tab[i] = -1;
    }
    int T, n;
    scanf("%d\n", &T);

    REP(i, T) {
        scanf("%d\n", &n);
        licznik = 0;
        if (tab[n] == -1) {
            if (n != 2) {
                subset(n - 2);
            }
            tab[n] = licznik;
        } else {
            licznik = tab[n];
        }
        printf("Case #%d: %d\n", (i + 1), licznik + 1);
    }
    return 0;
}

