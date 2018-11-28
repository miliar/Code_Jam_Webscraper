#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

const string A = "welcome to code jam";
string B = "";
char buffer[5000];
int memo[50][500];

int rec( int a, int b ) {
    if( a == (int)A.size() ) return 1;
    if( b >= (int)B.size() ) return 0;

    int &ret = memo[a][b];
    if( ret >= 0 ) return ret;

    ret = rec( a, b+1 );

    if( A[a] == B[b] ) ret += rec( a+1, b+1 );

    ret %= 10000;

    return ret;


}

int main ( void ) {

        int test; scanf( "%d", &test );
        gets( buffer );

        for( int cs = 0; cs < test; ++cs ) {

            gets(buffer); B = buffer;

            memset( memo, -1, sizeof memo );
            printf( "Case #%d: %04d\n", cs+1, rec( 0, 0 ) );

        }

return 0;
}
