# include <iostream>

using namespace std;

long long t;
long long n;
long long k;

int main() {
    scanf( "%d", &t );
    for ( int testId = 1; testId <= t; testId++ ) {
        scanf( "%d%d", &n, &k );

        long long p = 1;
        for ( int i = 0; i < n; i++ )
            p *= 2;

        printf( "Case #%d: ", testId );

        if ( k % p == p - 1 && k != 0 )
            printf( "ON\n" );
        else
            printf( "OFF\n" );
    }

    return 0;
}
