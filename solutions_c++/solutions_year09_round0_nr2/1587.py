#include <iostream>
#include <vector>

void flood_it( char **M, char l, int x, int y, int rows, int cols );
void find_sink( char **M, int x, int y, int &s_x, int &s_y );

int main()
{
    freopen("in", "r", stdin );
    freopen("out", "w", stdout );
    int casos, t = 0;
    scanf("%d", &casos );
    while( t++ < casos )
    {
        int rows, cols;
        scanf("%d%d", &rows, &cols );
        int *M[rows];
        char *S[rows];
        for( int i = 0; i < rows; ++i )
        {
            M[i] = new int[ cols ];
            S[i] = new char[ cols ];
            for( int j = 0; j < cols; ++j )
                scanf("%d", &M[i][j] );
        }
        for( int i = 0; i < rows; ++i )
        {
            for( int j = 0; j < cols; ++j )
            {
                char temp = 'S'; /* default S - sink, U - up, L - left, R - right, D - down */
                int t_val = 99999;
                if( i > 0 && M[i][j] > M[i-1][j] && M[i-1][j] < t_val )
                {
                    temp = 'U';
                    t_val = M[i-1][j];
                }
                if( j > 0 && M[i][j] > M[i][j-1] && M[i][j-1] < t_val )
                {
                    temp = 'L';
                    t_val = M[i][j-1];
                }
                if( j < cols - 1 && M[i][j] > M[i][j+1] && M[i][j+1] < t_val )
                {
                    temp = 'R';
                    t_val = M[i][j+1];
                }
                if( i < rows - 1 && M[i][j] > M[i+1][j] && M[i+1][j] < t_val )
                {
                    temp = 'D';
                    t_val = M[i+1][j];
                }
                S[i][j] = temp;
            }
        }
        printf("Case #%d:\n", t);
        char basin = 'a';
        for( int i = 0; i < rows; ++i )
        {
            for( int j = 0; j < cols; ++j )
            {
                if( S[i][j] < 'a' )
                {
                    int x, y;
                    find_sink( S, i, j, x, y );
                    flood_it( S, basin, x, y, rows, cols );
                    ++basin;
                }
                if( j > 0 )
                    printf(" ");
                printf("%c", S[i][j] );
            }
            printf("\n");
        }
    }
    return 0;
}

void find_sink( char **M, int x, int y, int &s_x, int &s_y )
{
    if( M[x][y] == 'U' )
        find_sink( M, x-1, y, s_x, s_y );
    else if( M[x][y] == 'L' )
        find_sink( M, x, y-1, s_x, s_y );
    else if( M[x][y] == 'R' )
        find_sink( M, x, y+1, s_x, s_y );
    else if( M[x][y] == 'D' )
        find_sink( M, x+1, y, s_x, s_y );
    else if( M[x][y] == 'S' )
    {
        s_x = x, s_y = y;
    }
}

void flood_it( char **M, char l, int x, int y, int rows, int cols )
{
    M[x][y] = l;
    if( x > 0 && M[x-1][y] == 'D' )
        flood_it( M, l, x-1, y, rows, cols );
    if( x < rows-1 && M[x+1][y] == 'U' )
        flood_it( M, l, x+1, y, rows, cols );
    if( y > 0 && M[x][y-1] == 'R' )
        flood_it( M, l, x, y-1, rows, cols );
    if( y < cols-1 && M[x][y+1] == 'L' )
        flood_it( M, l, x, y+1, rows, cols );
}
