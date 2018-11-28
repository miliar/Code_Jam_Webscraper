#include <algorithm>
#include <functional>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>

using namespace std;

const int MAXN = 100;

string S[ MAXN ];
char buffer[ 1000 ];
int last[ MAXN ];

int main( void )
{
    int T; scanf( "%d", &T );

    for( int counter = 0; counter < T; ++counter ) {
        int n; scanf( "%d", &n );

        for( int i = 0; i < n; ++i ) {
            scanf( "%s", buffer );
            S[i] = buffer;
            last[i] = -1;

            for( int j = 0; j < ( int )S[i].size(); ++j )
                if( S[i][j] == '1' )
                    last[i] = j;
        }

        int cnt = 0;
        for( int i = 0; i < n; ++i ) { 

            for( int j = i; j < n; ++j )
                if( last[j] <= i ) {
                    while( j != i ) {
                        swap( last[j], last[j-1] );
                        swap( S[j], S[j-1] );
                        --j; ++cnt;                        
                    }
                    break;
                }
        }

        printf( "Case #%d: %d\n", counter + 1, cnt );
    }

    return (0-0);
}
