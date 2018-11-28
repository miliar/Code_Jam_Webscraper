#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_H 111
#define MAX_W 111

int g[3][MAX_H][MAX_W];
int b[4][2] = { { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 } };
int c[4][2] = { { 1, 0 }, { 0, 1 }, { 0, -1 }, { -1, 0 } };
int st[MAX_H*MAX_W][2];
int t, h, w;
int ind;

void Bfs( int x, int y )
{
    while( g[1][x][y] >= 0 ) x += b[g[1][x][y]][0], y += b[g[1][x][y]][1];  
    int s = 0;
    int e = 0;
    st[s][0] = x;
    st[s][1] = y;
    ++s;
    while( e < s )
    {
        int x0 = st[e][0];
        int y0 = st[e][1];
        g[2][x0][y0] = ind;
        ++e;
        for( int i = 0; i < 4; ++i )
        {
            int x1 = x0 + c[i][0];
            int y1 = y0 + c[i][1];
            if( g[1][x1][y1] == i )
                st[s][0] = x1, st[s][1] = y1, ++s;
        }
    }
    ind++;
}
void Solve( )
{
    memset( g[1], 0xff, sizeof( g[1] ) * 2 );
    for( int i = 0; i < h; ++i )
        for( int j = 0; j < w; ++j )
        {
            int min = g[0][i][j];
            for( int k = 0; k < 4; ++k )
            {
                int x = i + b[k][0];
                int y = j + b[k][1];
                if( x >= 0 && x < h && y >= 0 && y < w )
                    if( g[0][x][y] < min )
                    {
                        min = g[0][x][y];
                        g[1][i][j] = k;
                    }  
            }
        }
    ind = 0;
    for( int i = 0; i < h; ++i )
        for( int j = 0; j < w; ++j )
            if( g[2][i][j] < 0 )
                Bfs( i, j );
    for( int i = 0; i < h; ++i )
    {
        for( int j = 0; j < w - 1; ++j )
            printf( "%c ", g[2][i][j] + 'a' );
        printf( "%c\n", g[2][i][w-1] + 'a' );
    }
}
int main( )
{
    freopen( "in.in", "r", stdin );
    freopen( "out.txt", "w", stdout );
    scanf( "%d", &t );
    for( int i = 1; i <= t; ++i )
    {
        printf( "Case #%d:\n", i );
        scanf( "%d %d", &h, &w );
        for( int j = 0; j < h; ++j )
            for( int k = 0; k < w; ++k )
                scanf( "%d", &g[0][j][k] );
        Solve( );
    }
    return 0;
}
