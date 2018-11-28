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

const int MAXN = 100, MAXL = 512, INF = 0x3f3f3f3f, MODULO = 10000;
const Ll INFL = 0x3f3f3f3f3f3f3f3fLL;
const double EPS = 1e-9;
const char wtcj[] = "welcome to code jam";
int n, l;
char s[MAXL + 4];
int cnt[20];
    
int main( )
{
    int i, j, lwtcj, t;
    lwtcj = strlen( wtcj );

    scanf( "%d\n", &n );
    for( t = 1 ; t <= n ; t++ )
    {
        fgets( s, MAXL, stdin );
        l = strlen( s );

        memset( cnt, 0, sizeof( cnt ) );
        for( i = 0 ; i < l ; i++ )
            for( j = 0 ; j < lwtcj ; j++ )
            {
                if( s[i] == wtcj[j] )
                {
                    if( j == 0 )
                        cnt[j]++;
                    else
                        cnt[j] += cnt[j - 1];
                    cnt[j] %= MODULO;
                }
            }

        printf( "Case #%d: %04d\n", t, cnt[lwtcj - 1] );
    }
    return 0;    
}
