#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SIZE(t) ((int)((t).size()))

long long gcd(long long a, long long b) {
    if (a < b) {
        swap(a, b);
    }
    while (a % b != 0) {
        long long t = a;
        a = b;
        b = t % b;
    }
    return b;
}

typedef struct {
    long long son, mon;
}FF;

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int bb = 1;
    while (T--) {
        long long N, PD, PG;
        scanf("%lld%lld%lld", &N, &PD, &PG);
        printf("Case #%d: ", bb++);
        if (PD == 0 && PG == 0) {
            puts("Possible");
        } else if (PD == 0) {
            puts("Broken");
        } else if (PG == 0) { 
            puts("Broken");
        } else if (PG == 100 && PD != 100) {
            puts("Broken");
        } else {
            long long ga = gcd(PD, 100);
            long long gb = gcd(PG, 100);
            FF pd, pg;
            pd.mon = 100 / ga;
            pd.son = PD / ga;
            pg.mon = 100 / gb;
            pg.son = PG / gb;

            if (pd.mon > N) {
                puts("Broken");
            } else {
                puts("Possible");
            }
        }
    }
    return 0;
}