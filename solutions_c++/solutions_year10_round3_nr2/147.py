#include <iostream>
#include <cstring>
using namespace std;

int d[1024][1024];

int solve( int x, int y )
{
    if ( x == y )
        return 0;
    if ( x+1 == y )
        return 1;
    if ( d[x][y] != -1 )
        return d[x][y];
    int sol = 0;
    sol = 1 + max( solve( x, (x+y)/2 ), solve( (x+y)/2, y ) );
    d[x][y] = sol;
    return sol;
}

int main()
{
    long long i, j, k;
    int T;
    int L, P, C;
    long long l, p, c;
    scanf( "%d", &T );
    memset( d, -1, sizeof( d ) );
    for ( int tt = 1; tt <= T; tt++ )
    {
        scanf( "%d %d %d", &L, &P, &C );
        l = L; p = P; c = C;
        k = L;
        j = 1;
        i = 0;
        while ( l*j < p )
        {
            i++;
            j = j * c;
        }
//        i = i+1;
//        i = 0;
//        while( solve( L, P, C, i ) == 0 )
//            i++;
        printf( "Case #%d: %d\n", tt, solve( 0, i )-1 );
    }
}
