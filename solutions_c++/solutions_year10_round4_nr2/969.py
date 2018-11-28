#include <iostream>
#include <cstring>
using namespace std;

int p, n;
int m[1024];
int pr[1024][1024];

int solve( int l, int r )
{
    int i, j, k;
    int fl = 0;
    for ( i = l; i <= r; i++ )
    {
        if ( m[i] > 0 )
        {
            fl = 1;
            m[i] = m[i] - 1;
        }
    }
    if ( fl == 0 )
    {
        return 0;
    }
    return solve( l, (l+r)/2 ) + solve( (l+r)/2+1, r ) + 1;
}

int main()
{
    int i, j, k;
    int sol;
    int T, t;
    scanf( "%d", &T );
    for ( t = 1; t <= T; t++ )
    {
        scanf( "%d", &p );
        n = (1<<p);
        for ( i = 1; i <= (1<<p); i++ )
        {
            scanf( "%d", &m[i] );
            m[i] = p - m[i];   //kolko trqbva da gleda 100%;
        }
        for ( i = p-1; i >= 0; i-- )
        {
            for ( j = 1; j <= (1<<i); j++ )
                scanf( "%d", &pr[i][j] );
        }

        sol = solve( 1, n );

        printf( "Case #%d: %d\n", t, sol );
    }
}
