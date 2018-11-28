#include <stdio.h>

int main (  ) {

    freopen ( "C:\\A-large.in", "r", stdin );
    freopen ( "C:\\A-large.out", "w", stdout );
    int N, p;
    int T, K;
    scanf ( "%d", &T );
    for ( p = 1; p <= T; p++ )
    {
        scanf ( "%d%d", &N, &K );
        printf ( "Case #%d: ", p );
        int x = 1 << N;
        if ( K % x == x - 1 )
            printf ( "ON\n" );
        else
            printf ( "OFF\n" );
    }
    return 0;
}
