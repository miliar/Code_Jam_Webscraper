# include <iostream>

using namespace std;

const int maxh = 105;

int t;

int h, w;
int map[ maxh ][ maxh ];

int nxt;
char res[ maxh ][ maxh ];
bool was[ maxh ][ maxh ];

const int dx[] = { -1,  0, 0, 1 };
const int dy[] = {  0, -1, 1, 0 };

char go( int r, int c )
{
    if ( was[ r ][ c ] )
        return res[ r ][ c ];

    was[ r ][ c ] = true;

    int t = 987654321;
    for ( int dir = 0; dir < 4; dir++ )
    {
        int nr = r + dx[ dir ];
        int nc = c + dy[ dir ];

        if ( nr < 0 || nr >= h || nc < 0 || nc >= w )
            continue;

        t = min( t, map[ nr ][ nc ] );
    }

    if ( t < map[ r ][ c ] )
    {
        for ( int dir = 0; dir < 4; dir++ )
        {
            int nr = r + dx[ dir ];
            int nc = c + dy[ dir ];

            if ( nr < 0 || nr >= h || nc < 0 || nc >= w )
                continue;

            if ( map[ nr ][ nc ] != t )
                continue;

            return res[ r ][ c ] = go( nr, nc );
        }
    }

    return res[ r ][ c ] = char( 'a' + nxt++ );
}

int main()
{
    scanf( "%d", &t );
    for ( int test = 1; test <= t; test++ )
    {
        scanf( "%d %d", &h, &w );
        for ( int i = 0; i < h; i++ )
            for ( int j = 0; j < w; j++ )
                scanf( "%d", &map[ i ][ j ] );

        nxt = 0;
        memset( was, 0, sizeof( was ) );

        for ( int i = 0; i < h; i++ )
            for ( int j = 0; j < w; j++ )
                go( i, j );

        printf( "Case #%d:\n", test );
        for ( int i = 0; i < h; i++ )
        {
            printf( "%c", res[ i ][ 0 ] );

            for ( int j = 1; j < w; j++ )
                printf( " %c", res[ i ][ j ] );

            printf( "\n" );
        }
    }

    return 0;
}
