#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>


using namespace std;

const int maxn = 1000;
const int maxd = 8000;
const int maxl = 32;
const int maxp = 1000000;

int l, d, n;
char dir[ maxd ][ maxl ], ptn[ maxp], ace[ maxl ];

int solve( )
{
    if( !( cin >> l >> d >> n ) )
	return 0;
    for( int i = 0; i < d; ++i )
	scanf( "%s", dir[i] );
    for( int __t = 1; __t <= n; ++__t )
    {
	scanf( "%s", ptn );
	int m = strlen( ptn ), cnt = 0;
	for( int i = 0; i < d; ++i )
	{
	    memset( ace, 0, sizeof ace );
	    for( int j = 0, k = 0, brc = 0; j < m; ++j )
	    {
		if( ptn[j] == '(' ) ++brc;
		else if( ptn[j] == ')' )
		{
		    --brc;
		    if( ace[k] ) ++k;
		    else break;
		}
		else
		{
		    if( brc )
		    {
			if( ace[k] ) continue;
			if( ptn[j] == dir[i][k] )
			    ace[k] = 1;
		    }
		    else
		    {
			if( ptn[j] != dir[i][k] )
			    break;
			ace[k++] = 1;
		    }
		}
	    }
	    cnt += ace[l-1];
	}
	printf( "Case #%d: %d\n", __t, cnt );
    }
    return 1;
}

int main( void )
{
    //freopen( "A-large.in", "r", stdin );
    while( solve( ) );
    return 0;
}
