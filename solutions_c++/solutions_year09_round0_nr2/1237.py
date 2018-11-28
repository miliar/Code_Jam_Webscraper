#include <stdio.h>
#include <memory.h>

int const MAXH = 600;
int const MAXW = 600;

int H, W;
int height[ MAXH ][ MAXW ];
char bassein[ MAXH ][ MAXW ];
char current;

char Fill( int i, int j )
{
    if( bassein[i][j] != 0 )
        return bassein[i][j];

    int vi = 0, vj = 0, min = height[ i ][ j ];
    if( i>0 && height[i-1][j] < min )
    {
        vi = -1; vj = 0; min = height[i-1][j];
    }
    if( j>0 && height[i][j-1] < min )
    {
        vi = 0; vj = -1; min = height[i][j-1];
    }
    if( j<W-1 && height[i][j+1] < min )
    {
        vi = 0; vj = 1; min = height[i][j+1];
    }
    if( i<H-1 && height[i+1][j] < min )
    {
        vi = 1; vj = 0; min = height[i+1][j];
    }

    if( vi != 0 || vj != 0 )
    {
        bassein[i][j] = Fill( i + vi, j + vj );
    }
    else
    {
        bassein[i][j] = current++;
    }

    return bassein[i][j];
}

int main()
{
    int testCount;
    scanf( "%d", &testCount );
    for( int test = 1; test <= testCount; ++ test )
    {
        scanf( "%d %d", &H, &W );
        for( int i = 0; i != H; ++ i )
        {
            for( int j = 0; j != W; ++ j )
                scanf( "%d", &height[ i ][ j ] );
        }

        memset( bassein, 0, sizeof( bassein ) ); 
        current = 'a';
        for( int i = 0; i != H; ++ i )
        {
            for( int j = 0; j != W; ++ j )
            {
                if( bassein[i][j] == 0 ) Fill( i, j );
            }
        }
        printf( "Case #%d:\n", test );
        for( int i = 0; i != H; ++ i )
        {
            for( int j = 0; j != W; ++ j )
            {
                if( j > 0 ) printf( " " );
                printf( "%c", bassein[i][j] );
            }
            printf( "\n" );
        }
    }
    return 0;
}