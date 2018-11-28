#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>

using namespace std;

#define sqr(a) ((a)*(a))
#define det2(a,b,c,d) ((a)*(d) - (b)*(c))

#define N 10
#define M 100

int k[M], x[M][N], y[M][N], n, m;

int bits( int x )
{
    int r= 0;
    while(x)
    {
        r++;
        x &= (x-1);
    }
    return r;
}

bool ok( int mask )
{
    int i, j;
    for ( i = 0 ; i < m ; i++ )
    {
        for ( j = 0 ; j < k[i] ; j++ )
        {
            int t = bool(mask & (1<< (x[i][j]-1) ));
            if ( t == y[i][j] )
                break;
        }
        if ( j >= k[i] )
            return 0;
    }
    return 1;
}

int main()
{
    int i, j, cas, T;

    scanf( "%d", &T );
    for ( cas = 1 ; cas <= T ; cas++ )
    {
        scanf( "%d%d", &n, &m );
        for ( i = 0 ; i < m ; i++ )
        {
            scanf( "%d", &k[i] );
            if ( k[i] > n ) printf( "botva!\n" );
            for ( j = 0 ; j < k[i] ; j++ )
                scanf( "%d%d", &x[i][j], &y[i][j] );
        }

        int res = -1;
        for ( i = 0 ; i < (1<<n) ; i++ )
        {
            if ( ok(i) && bits(i) < bits(res) )
                res = i;
        }

        printf( "Case #%d:", cas );
        if ( res == -1 )
            printf( " IMPOSSIBLE" );
        else
            for ( i = 0 ; i < n ; i++ )
                printf( " %d", bool(res & (1<<i)) );
        printf( "\n" );
    }

    return 0;
}
