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
Ll n;
int dd[10];
    
int main( )
{
    int nt, it;
    scanf( "%d", &nt );
    for( it = 1 ; it <= nt ; it++ )
    {
        scanf( "%lld", &n );

        int ndig, maxdig = -1;
        memset( dd, 0, sizeof( dd ) );
        for( ;; )
        {
            ndig = n % 10;
            dd[ndig]++;
            n /= 10;

            if( ndig < maxdig )
                break;
            maxdig = ndig;
        }

        for( ++ndig ; dd[ndig] == 0 ; ndig++ );
        n = n * 10 + ndig;
        dd[ndig]--;

        for( ndig = 0 ; ndig < 10 ; ndig++ )
            while( dd[ndig] > 0 )
            {
                n = n * 10 + ndig;
                dd[ndig]--;
            }

        printf( "Case #%d: %lld\n", it, n );
    }
    return 0;    
}

