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

const int MAXN = 64, MAXL = 36, INF = 0x3f3f3f3f;
const Ll INFL = 0x3f3f3f3f3f3f3f3fLL;
const double EPS = 1e-9;
int n;
char ln[MAXN];
int dd[MAXL], digs[MAXL];
    
int main( )
{
    int it, nt;
    for( it = 2 ; it < MAXL ; it++ )
        digs[it] = it;
    digs[0] = 1, digs[1] = 0;

    scanf( "%d\n", &nt );
    for( it = 1 ; it <= nt ; it++ )
    {
        int i, lln, nval, ndig = 0;
        fgets( ln, MAXN - 2, stdin );

        lln = strlen( ln );
        memset( dd, -1, sizeof( dd ) );
        for( i = 0 ; i < lln ; i++ )
        {
            nval = -1;
            if( isdigit( ln[i] ) )
                nval = (ln[i] - '0');
            if( isalpha( ln[i] ) )
                nval = 10 + (ln[i] - 'a');

            if( nval != -1 && dd[nval] == -1 )
                dd[nval] = ndig++;
        }

        if( ndig < 2 )
            ndig = 2;

        Ll res = 0;
        for( i = 0 ; i < lln ; i++ )
        {
            nval = -1;
            if( isdigit( ln[i] ) )
                nval = (ln[i] - '0');
            if( isalpha( ln[i] ) )
                nval = 10 + (ln[i] - 'a');

            if( nval != -1 )
                res = res * ndig + digs[dd[nval]];
        }
        printf( "Case #%d: %lld\n", it, res );
    }
    return 0;    
}
