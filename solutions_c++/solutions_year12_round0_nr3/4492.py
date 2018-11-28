#include <stdio.h>

int k, t, a, b, i, j, ans, tmp;

int fun ( int x ) {
    if ( x < 10 ) return x;
    if ( 10 <= x && x <= 99 ) {
        tmp = x % 10;
        return tmp * 10 + x / 10;
    }
    if ( 100 <= x && x <= 999 ) {
        tmp = x % 100;
        return tmp * 10 + x / 100;
    }
}

int fun1 ( int x ) {
    if ( 100 <= x && x <= 999 ) {
        tmp = x % 10;
        return tmp * 100 + x / 10;
    }
    else return 0;
}

int main ( ) {
    freopen ( "C-small-attempt1.in", "r", stdin );
    freopen ( "out.out", "w", stdout );
    while ( scanf ( "%d", &t ) != EOF ) {
        for ( j = 1; j <= t; j++ ) {
            scanf ( "%d%d", &a, &b );
            ans = 0;
            for ( i = a; i <= b; i++ ) {
                k = fun ( i );
                if ( i < k && k <= b ) {
                    //printf ( "1(%d,%d)\n", i, k );
                    ans++;
                }
                k = fun1 ( i );
                if ( i < k && k <= b ) {
                    //printf ( "2(%d,%d)\n", i, k );
                    ans++;
                }
            }
            printf ( "Case #%d: %d\n", j, ans );
        }
    }
}
