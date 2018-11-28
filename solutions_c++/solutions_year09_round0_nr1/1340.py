# include <iostream>

using namespace std;

const int maxl = 20;
const int maxd = 5005;

int l, d, n;

char dic[ maxd ][ maxl ];

bool mark[ maxl ][ 30 ];

int main()
{
    scanf( "%d %d %d", &l, &d, &n );
    for ( int i = 0; i < d; i++ )
        scanf( "%s", &dic[ i ] );

    for ( int test = 1; test <= n; test++ )
    {
        char str[ 1000 ];
        scanf( "%s", &str );

        memset( mark, 0, sizeof( mark ) );

        int p = 0;
        for ( int q = 0; q < l; q++ )
        {
            if ( str[ p ] == '(' )
            {
                p++;

                while ( str[ p ] != ')' )
                    mark[ q ][ str[ p++ ] - 'a' ] = true;

                p++;
            }
            else
                mark[ q ][ str[ p++ ] - 'a' ] = true;
        }

        int res = 0;
        for ( int i = 0; i < d; i++ )
        {
            bool ok = true;

            for ( int j = 0; j < l && ok; j++ )
                if ( !mark[ j ][ dic[ i ][ j ] - 'a' ] )
                    ok = false;

            if ( ok )
                res++;
        }

        printf( "Case #%d: %d\n", test, res );
    }

    return 0;
}
