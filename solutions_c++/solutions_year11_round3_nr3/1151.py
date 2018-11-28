#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

typedef unsigned long long ull;

const int MAXN = 1 << 14;

ull x[MAXN];
ull numDigits[MAXN];
ull n;
ull l , r;

void read() {
        scanf ( "%llu%llu%llu" , &n , &l , &r );

        int i;
        for (i = 0; i < n; ++i)
                scanf ( "%llu" , x + i );
}

ull gcd ( ull a , ull b ) {
        if ( b == 0 ) return a;
        return gcd ( b , a % b );
}

void print1 ( int testNumber , ull ans ) {
        printf ( "Case #%d: %llu\n" , testNumber , ans );
}
void print2 ( int testNumber ) {
        printf ( "Case #%d: NO\n" , testNumber );
}

bool ok ( ull t ) {
        for (int i = 0; i < n; ++i)
                if ( (x[i] % t != 0) && (t % x[i] != 0) )
                        return 0;
        return 1;
}

void solve ( int testNumber ) {
        ull t;
        for (t = l; t <= r; ++t)
                if ( ok ( t ) ) {
                        print1 ( testNumber , t );
                        return;
                }
        print2 ( testNumber );
}

int main() {
        int tests;
        scanf ( "%d" , &tests );
        for (int i = 1; i <= tests; ++i) {
                read();
                solve ( i );
        }
        return 0;
}

