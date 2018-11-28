#include <cstdio>

int step[ 4 ][ 2 ] =
{
    { 1, 1 }, { 1, -1 }, { 1, 0 }, { 0, 1 }
};

char judge( char arr[][ 4 ], int begr, int begc, int dire )
{
    char tag = arr[ begr ][ begc ];
    if( tag == '.' ) return 'T';
    int row = begr, col = begc;
    for( int i = 1; i < 4; ++i )
    {
        row += step[ dire ][ 0 ];
        col += step[ dire ][ 1 ];
        if( arr[ row ][ col ] == '.' ) return 'T';
        if( tag == 'T' ) tag = arr[ row ][ col ];
        else if( arr[ row ][ col ] == 'T' ) continue;
        else if( tag != arr[ row ][ col ] ) return 'T';
    }
    return tag;
}

int main()
{
    int t;
    scanf( "%d", &t );
    for( int ncase = 1; ncase <= t; ++ncase )
    {
        printf( "Case #%d: ", ncase );

        bool is_fill = true;
        char status = 'T', arr[ 4 ][ 4 ];
        for( int i = 0; i < 4; ++i )
            for( int j = 0; j < 4; ++j )
            {
                scanf( " %c", &arr[ i ][ j ] );
                if( arr[ i ][ j ] == '.' ) is_fill = false;
            }

        status = judge( arr, 0, 0, 0 );
        if( status == 'T' ) status = judge( arr, 0, 3, 1 );
        for( int i = 0; i < 4 && status == 'T'; ++i )
        {
            status = judge( arr, i, 0, 3 );
            if( status == 'T' ) status = judge( arr, 0, i, 2 );
        }

        if( status == 'X' ) printf( "X won\n" );
        else if( status == 'O' ) printf( "O won\n" );
        else if( is_fill ) printf( "Draw\n" );
        else printf( "Game has not completed\n" );
    }
}
