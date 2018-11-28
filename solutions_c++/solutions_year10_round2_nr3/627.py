#include <iostream>
#include <cstring>
using namespace std;

const int MOD = 100003;

int f[512];

int n;
int dp[512][512];
int cp[512][512];

int comb( int chisla, int pos )
{
    if ( pos < 0 )
        return 0;
    if ( chisla < pos )
        return 0;
    if ( cp[chisla][pos] != -1 )
        return cp[chisla][pos];
    cp[chisla][pos] = ( comb( chisla-1, pos-1 ) + comb( chisla-1, pos ) ) % MOD;

    return cp[chisla][pos];

/*    int i, k = 1, j, l;
    memset( f, 0, sizeof( f ) );
    for ( i = chisla - pos + 1; i <= chisla; i++ )
    {
        l = i;
        for ( j = 1; j <= pos; j++ )
        {
            if ( ( f[j] == 0 ) && ( l % j == 0 ) )
            {
                l = l / j;
                f[j] = 1;
            }
        }
        k = ( k * l ) % MOD;
    }
    cp[chisla][pos] = k;
    return k;*/
}

int getDP( int x, int p )
{
    if ( dp[x][p] != -1 )
        return dp[x][p];
    int i, j, k, sol = 0;
    if ( x <= p )
    {
        dp[x][p] = 0;
        return 0;
    }

    for ( k = 1; k < p; k++ )
    {
        if ( p - k <= x - p )
            sol = ( sol + getDP( p, k ) * comb( x-p-1, p-k-1 ) ) % MOD;
    }

    dp[x][p] = sol;
    return dp[x][p];
}

int main()
{
    int i, j, k;
    int T;

    memset( cp, -1, sizeof( cp ) );
    cp[0][0] = 1;
    cp[1][0] = 1;
    cp[1][1] = 1;

    scanf( "%d", &T );

    memset( dp, -1, sizeof( dp ) );
    for ( i = 1; i <= 500; i++ )
    {
        dp[i][1] = 1;
    }

    for ( int tt = 1; tt <= T; tt++ )
    {
        scanf( "%d", &n );
        k = 0;
        for ( i = 1; i < n; i++ )
        {
            k = ( k + getDP( n, i ) ) %MOD;
        }
        printf( "Case #%d: %d\n", tt, k );
    }
    return 0;
}
