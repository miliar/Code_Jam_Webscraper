#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int maxn = 128;

int g[ maxn ][ maxn ], id[ maxn ][ maxn ], f[ maxn * maxn ], r[ maxn * maxn ];
char mk[ maxn ][ maxn ], val[ maxn * maxn ];

int uf_find( int u )
{
    if( u != f[u] ) f[u] = uf_find( f[u] );
    return f[u];
}

void uf_union( int u, int v )
{
    int i = uf_find( u ), j = uf_find( v );
    if( i == j ) return;
    if( r[i] > r[j] ) f[j] = i; else f[i] = j;
    if( i == j ) ++r[j];
}

int dr[ ] = { -1, 0, 0, 1 };
int dc[ ] = {  0,-1, 1, 0 };

void solve( int __r )
{
    int h, w, n = 0;
    cin >> h >> w;
    for( int i = 0; i < h; ++i )
	for( int j = 0; j < w; ++j )
	{
	    scanf( "%d", &g[i][j] );
	    id[i][j] = n++;
	}
    for( int i = 0; i < n; ++i )
    {
	f[i] = i;
	r[i] = 0;
    }
    for( int i = 0; i < h; ++i )
	for( int j = 0; j < w; ++j )
	{
	    int dx = -1, dy = -1, d = -1;
	    for( int k = 0; k < 4; ++k )
	    {
		int nx = i + dr[k], ny = j + dc[k];
		if( nx < 0 || nx >= h || ny < 0 || ny >= w )
		    continue;
		if( g[i][j] - g[nx][ny] > d )
		{
		    dx = nx;
		    dy = ny;
		    d = g[i][j] - g[nx][ny];
		}
	    }
	    if( d > 0 ) uf_union( id[i][j], id[dx][dy] );
	}
    memset( val, -1, sizeof val );
    char kk = 'a';
    for( int i = 0; i < h; ++i )
	for( int j = 0; j < w; ++j )
	{
	    int u = uf_find( id[i][j] );
	    if( val[u] < 0 ) val[u] = kk++;
	    mk[i][j] = val[u];
	}
    printf( "Case #%d:\n", __r );
    for( int i = 0; i < h; ++i )
    {
	int wfirst = 1;
	for( int j = 0; j < w; ++j )
	{
	    if( !wfirst ) putchar( ' ' );
	    wfirst = 0;
	    putchar( mk[i][j] );
	}
	putchar( '\n' );
    }		
}

int main( void )
{
    freopen( "B-large.in", "r", stdin );
    int __t;
    cin >> __t;
    for( int i = 1; i <= __t; ++i )
	solve( i );
    return 0;
}

