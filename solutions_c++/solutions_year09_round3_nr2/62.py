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

const int MAXN = 50, INF = 0x3f3f3f3f;
const Ll INFL = 0x3f3f3f3f3f3f3f3fLL;
const double EPS = 1e-9;
int n;
    
int main( )
{
    int it, nt;
    scanf( "%d", &nt );
    for( it = 1 ; it <= nt ; it++ )
    {
        int i, x, y, z, vx, vy, vz;
        Ll sx = 0, sy = 0, sz = 0, 
           svx = 0, svy = 0, svz = 0;
        scanf( "%d", &n );
        for( i = 0 ; i < n ; i++ )
        {
            scanf( "%d%d%d%d%d%d", &x, &y, &z,
                   &vx, &vy, &vz );
            sx += x;
            sy += y;
            sz += z;
            svx += vx;
            svy += vy;
            svz += vz;
        }

        double tmin = -1.0 * (sx * svx + sy * svy + sz * svz) /
            (svx * svx + svy * svy + svz * svz);
        if( signbit( tmin ) )
            tmin = 0.0;

        double xmin = tmin * (double)svx + (double)sx,
               ymin = tmin * (double)svy + (double)sy,
               zmin = tmin * (double)svz + (double)sz;
        double dmin = sqrt( (xmin * xmin + ymin * ymin + zmin * zmin) / (n * n) );
        printf( "Case #%d: %.8lf %.8lf\n", it, dmin, tmin );
    }
    return 0;    
}

