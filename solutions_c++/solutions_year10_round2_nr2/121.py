#include <cstdio>
#include <algorithm>
#include <vector>

#define REP(i, n) for ( int i = 0; i < (n); i++ ) 
#define FOR(i, a, b) for ( int i = (a); i < (b); i++ ) 

using namespace std;

const int MAX_N = 110;

int n, k;
long long t, b;

long long X[MAX_N];
long long V[MAX_N];

void fun(int cs) {
    scanf("%d %d %lld %lld", &n, &k, &b, &t);

    REP(i, n) scanf("%lld", &X[i]);
    REP(i, n) scanf("%lld", &V[i]);

    int ok = 0;
    int imp = 0;
    long long res = 0;

    if ( k == 0 ) {
        printf("Case #%d: %lld\n", cs, res);
        return;
    }

    for ( int i = n - 1; i >= 0; i -- ) {
        long long x = X[i];
        long long v = V[i];

        if ( x + v * t >= b ) {
            ok += 1;
            res += imp;

            if ( ok == k ) {
                printf("Case #%d: %lld\n", cs, res);
                return;
            }
        } else {
            imp += 1;
//            printf("%lld %lld nie da rady\n", x, v);
        }
    }

    printf("Case #%d: IMPOSSIBLE\n", cs);
}

int main() {
    int C;
    scanf("%d", &C);
    REP(i, C) fun(i+1);

    return 0;
}
