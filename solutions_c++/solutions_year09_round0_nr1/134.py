#include <algorithm>
#include <functional>

#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>

using namespace std;

const int MAXLEN = 20;
const int MAXN = 5010;

int len, n_dict, T;

char S[ 10000 ];
char dict[ MAXN ][ MAXLEN+1 ];
char jeli[ MAXLEN ][ 256 ];

int main( void )
{
    scanf( "%d %d %d", &len, &n_dict, &T );

    for( int i = 0; i < n_dict; ++i ) 
        scanf( "%s", dict[i] );

    for( int counter = 0; counter < T; ++counter ) {
        scanf( "%s", S );
        memset( jeli, 0, sizeof jeli );

        int x = 0;
        for( int i = 0; i < len; ++i ) {
            if( isalpha( S[x] ) ) jeli[i][ (int)S[x++] ] = true;
            else {
                for( ++x; S[x] != ')'; ++x ) 
                    jeli[i][ (int)S[x] ] = true;
                ++x;
            }
        }

        int sol = 0;

        for( int i = 0; i < n_dict; ++i ) {
            int ok = true;

            for( int j = 0; j < len; ++j ) 
                if( jeli[j][ (int)dict[i][j] ] == false ) {
                    ok = false;
                }

            sol += ok;
        }

        printf( "Case #%d: %d\n", counter + 1, sol );
    }

    return (0-0);
}
