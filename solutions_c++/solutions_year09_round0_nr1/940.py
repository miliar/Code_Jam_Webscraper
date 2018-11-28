#include <algorithm>
#include <vector>
#include <string>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int MAXL = 17;
const int MAXD = 5100;
const int MAXN = 410;

int L, D, Q;
char dict[ MAXD ][ MAXL ];

int n;
char expr[ MAXN ];
int choose[ MAXN ];

int main( void )
{
    scanf( "%d %d %d", &L, &D, &Q );

    for( int i = 0; i < D; ++i )
        scanf( "%s", dict[i] );

    for( int t = 0; t < Q; ++t ) {
        scanf( "%s", expr );
        n = strlen( expr );

        int pos = 0;

        for( int i = 0; i < L; ++i, ++pos ) {
            if( expr[pos] != '(' )
                choose[i] = 1 << ( expr[pos]-'a' );
            else {
                choose[i] = 0;

                for( ++pos; expr[pos] != ')'; ++pos )
                    choose[i] |= 1 << ( expr[pos]-'a' );
            }
        }

        int cnt = 0;

        for( int i = 0; i < D; ++i ) {
            int match = 0;

            for( int j = 0; j < L; ++j )
                match += ( choose[j] >> (dict[i][j]-'a') ) & 1;

            if( match == L ) ++cnt;
        }

        printf( "Case #%d: %d\n", t+1, cnt );
    }

    return 0;
}

