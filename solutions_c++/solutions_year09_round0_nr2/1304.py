#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstdarg>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <utility>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

#define	REP( i, n )         for( (i) = 0 ; (i) < (n) ; (i)++ )
#define	IREP( i, n )	    for( (i) = (n) - 1 ; (i) >= 0 ; (i)-- )
#define REPV( i, a, b )     for( (i) = (a) ; (i) <= (b) ; (i)++ )
#define IREPV( i, a, b )    for( (i) = (b) ; (i) >= (a) ; (i)-- )
#define REPIT( it, x )      for( (it) = (x).begin( ) ; (it) != (x).end( ) ; (it)++ )
#define ALL( x )            (x).begin( ), (x).end( )
#define MP                  make_pair
#define PB                  push_back
#define CLR( x )            memset( (x), 0, sizeof( x ) )
#define CLRV( x, v )        memset( (x), (v), sizeof( x ) )
#define CPY( y, x )         memcpy( (y), (x), sizeof( x ) )
#define	X                   first
#define Y                   second

typedef long long Ll;
typedef pair< int, int > Pii;
typedef pair< Ll, Ll > Pll;
typedef vector< int > Vi;
typedef vector< Ll > Vl;
typedef vector< string > Vs;

const int MAXN = 100, INF = 0x3f3f3f3f;
const Ll INFL = 0x3f3f3f3f3f3f3f3fLL;
const double EPS = 1e-9;
const int ddir[4][2] = { { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 } };
int nt, h, w;
int a[MAXN][MAXN];
char c[MAXN][MAXN];
   
int walkMatrix( int io, int jo, char ltr )
{
    int res = 0;
    stack< Pii > pq;
    pq.push( MP( io, jo ) );
    while( !pq.empty( ) )
    {
        Pii cpos = pq.top( );
        pq.pop( );
        if( c[cpos.X][cpos.Y] )
            continue;

        int hmin = a[cpos.X][cpos.Y],
            dmin = -1, d, ni, nj;
        for( d = 0 ; d < 4 ; d++ )
        {
            ni = cpos.X + ddir[d][0];
            nj = cpos.Y + ddir[d][1];
            if( ni >= 0 && ni < h &&
                nj >= 0 && nj < w &&
                a[ni][nj] < hmin )
            {
                hmin = a[ni][nj];
                dmin = d;
            }
        }

        if( dmin == -1 )
        {
            c[cpos.X][cpos.Y] = ltr;
            res = 1;
        }
        else
        { 
            ni = cpos.X + ddir[dmin][0];
            nj = cpos.Y + ddir[dmin][1];
            if( !c[ni][nj] )
            {
                pq.push( cpos );
                pq.push( MP( ni, nj ) );
            }
            else
                c[cpos.X][cpos.Y] = c[ni][nj];
        }
    }
    return res;
}

int main( )
{
    int t, i, j;
    scanf( "%d", &nt );
    for( t = 1 ; t <= nt ; t++ )
    {
        scanf( "%d%d", &h, &w );
        for( i = 0 ; i < h ; i++ )
            for( j = 0 ; j < w ; j++ )
                scanf( "%d", &a[i][j] );

        char nl = 'a';
        memset( c, 0, sizeof( c ) );
        for( i = 0 ; i < h ; i++ )
            for( j = 0 ; j < w ; j++ )
                if( !c[i][j] )
                    nl += walkMatrix( i, j, nl );

        printf( "Case #%d:\n", t );
        for( i = 0 ;  i < h ; i++ )
        {
            for( j = 0 ; j < w ; j++ )
                printf( "%c ", c[i][j] );
            printf( "\n" );
        }
    }
    return 0;    
}
