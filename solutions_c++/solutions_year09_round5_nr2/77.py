#include <algorithm>
#include <vector>
#include <string>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int MAXN = 22;
const int mod = 10009;

int n, K;

char expr[ 100000 ];
char words[ MAXN ][ 52 ];

int cnt[ 26 ];

int evaluate()
{
    int last = -1;
    int suma = 0;

    for( int i = 0; ; ++i ) {
        if( expr[i] == 0 || expr[i] == '+' ) {
            int add = 1;

            for( int j = last+1; j < i; ++j )
                add = add * cnt[ expr[j]-'a' ] % mod;

            suma += add;
            suma %= mod;
            last = i;
        }

        if( expr[i] == 0 ) break;
    }

    return suma;
}

int solve( int jos )
{
    if( jos == 0 ) return evaluate();

    int ret = 0;

    for( int i = 0; i < n; ++i ) {
        for( char *c = words[i]; *c; ++c )
            ++cnt[ *c-'a' ];

        ret += solve( jos - 1 );
        if( ret >= mod ) ret -= mod;

        for( char *c = words[i]; *c; ++c )
            --cnt[ *c-'a' ];
    }

    return ret;
}

int main( void )
{
    int test; scanf( "%d", &test );

    for( int t = 0; t < test; ++t ) {
        scanf( "%s %d %d", expr, &K, &n );

        for( int i = 0; i < n; ++i )
            scanf( "%s", words[i] );

        printf( "Case #%d:", t+1 );

        for( int i = 1; i <= K; ++i )
            printf( " %d", solve( i ) );

        putchar( '\n' );
    }

    return 0;
}

