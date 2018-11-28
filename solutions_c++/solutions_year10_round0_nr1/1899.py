#include <algorithm>
#include <functional>

#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <string>
#include <vector>

using namespace std;

int main( void )
{
    int T; scanf( "%d", &T );

    for( int counter = 0; counter < T; ++counter ) {
        int n, k; scanf( "%d %d", &n, &k );
        printf( "Case #%d: %s\n", counter + 1, ( k+1 ) % ( 1<<n ) ? "OFF" : "ON" );
    }

    return (0-0);
}
