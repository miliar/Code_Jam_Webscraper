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

#define FORD(k,b,e) for(LET(k,e); (b) <= (--k);) // (e-1 -> b)
#define REPD(x,n) for(int x = (n - 1); x >= 0; ++x) // (n-1 -> 0)

#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i,c) for(LET(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

const int INF = 1000000001;
const double EPS = 10e-9;

typedef long long ll;

int f(ll s, ll e, int c) {
    int r = 0;
    while (c * s < e) {
//        printf("s=%d e=%d\n", s, e);
        ll x = s, y = e;
        while (x < y) {
            x *= c;
            int t = y % c;
            if (t != 0) {
                y += c - t;
            }
            y /= c;
        }
        ++r;
//        printf("%d %d\n", x, y);
//        x = ((x + y) >> 1) + ((x+y) % 2);
        e = x;
    }
    return r;
}

int main() {
    int T, l, p, c;
    scanf("%d\n", &T);

    REP(i, T) {
        scanf("%d %d %d\n", &l, &p, &c);
        printf("Case #%d: %d\n", (i+1), f(l, p, c));
    }
    return 0;
}
