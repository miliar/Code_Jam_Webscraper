# include <iostream>

using namespace std;

const int mod = 10000;
const int len = 25;
const int maxlen = 500;
const string welcome = "welcome to code jam";

int n;
char ch;

int dp[ 2 ][ len ];

int main()
{
    scanf( "%d\n", &n );
    for ( int test = 1; test <= n; test++ )
    {
        int nxt = 1;
        memset( dp, 0, sizeof( dp ) );

        dp[ 0 ][ 0 ] = 1;

        for ( ch = getchar(); ( ch >= 'a' && ch <= 'z' ) || ch == ' ' || ch == '\t'; ch = getchar() )
        {
            for ( int i = 0; i <= 19; i++ )
                dp[ nxt ][ i ] = dp[ !nxt ][ i ];

            for ( int i = 0; i < 19; i++ )
                if ( welcome[ i ] == ch )
                {
                    dp[ nxt ][ i + 1 ] += dp[ !nxt ][ i ];

                    if ( dp[ nxt ][ i + 1 ] >= mod )
                        dp[ nxt ][ i + 1 ] -= mod;
                }

            nxt = !nxt;
        }

        printf( "Case #%d: ", test );

        int x = dp[ !nxt ][ 19 ];
        if ( x < 1000 )
            printf( "0" );
        if ( x < 100 )
            printf( "0" );
        if ( x < 10 )
            printf( "0" );
        printf( "%d\n", x );
    }

    return 0;
}
