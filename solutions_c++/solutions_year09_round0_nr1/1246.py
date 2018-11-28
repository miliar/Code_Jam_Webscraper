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

const int MAXL = 20, MAXD = 5000, MAXN = 500, INF = 0x3f3f3f3f;
const Ll INFL = 0x3f3f3f3f3f3f3f3fLL;
const double EPS = 1e-9;
int l, d, n;
char cd[MAXD][MAXL + 4];
unsigned cword[MAXL];
    
int main( )
{
    int t, i, j;
    scanf( "%d%d%d\n", &l, &d, &n );
    for( i = 0 ; i < d ; i++ )
        fgets( cd[i], MAXL, stdin );
    for( t = 1 ; t <= n ; t++ )
    {
        char ch = 0;
        memset( cword, 0, sizeof( cword ) );
        for( i = 0 ; i < l ; i++ )
        {
            ch = fgetc( stdin );
            if( ch == '(' )
            {
                cword[i] = 1;
                for( ;; )
                {
                    ch = fgetc( stdin );
                    if( ch == ')' || ch == '\n' )
                        break;
                    cword[i] |= 1U << (1 + (ch - 'a'));
                }
            }
            else
                cword[i] = (ch - 'a') << 1;
        }
        for( ; ch != '\n' ; ch = fgetc( stdin ) );

        int res = 0;
        for( i = 0 ; i < d ; i++ )
        {
            for( j = 0 ; j < l ; j++ )
            {
                if( (cword[j] & 1) == 0 &&
                    cd[i][j] != (char)('a' + (cword[j] >> 1)) )
                    break;
                if( (cword[j] & 1) == 1 &&
                    (cword[j] & (1 << (1 + (cd[i][j] - 'a')))) == 0 )
                    break;
            }
            if( j == l )
                res++;
        }
        printf( "Case #%d: %d\n", t, res );
    }
    return 0;    
}
