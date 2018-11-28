#include <stdio.h>
#include <string.h>

char w[5000][16], s[1000], c[15][256], st[1000];

int main( void )
{
	int n, l, d, t, i, j, sz, ans;
	char ch;
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	scanf( "%d%d%d", &l, &d, &n );
	for ( i = 0; i < d; i++ )
	{
		scanf( "%s", w[i] );
	}
	for ( t = 1; t <= n; t++ )
	{
		scanf( "%s", s );		
		memset( c, 0, sizeof(c) );
		sz = -1;
		for ( i = 0, j = 0; s[i]; i++ )
		{
			ch = s[i];
			if ( ch == ')' )
			{
				while ( st[sz] != '(' )
				{
					c[ j ][ st[sz] ] = 1;
					--sz;
				}
				--sz;
				j++;
			}
			else
			{
				if ( sz == -1 && ch != '(' )
				{
					c[ j++ ][ ch ] = 1;					
				}
				else 
				{
					st[ ++sz ] = ch;					
				}
			}			
		}	
		ans = 0;	
		for ( i = 0; i < d; i++ )
		{
			for ( j = 0; j < l && c[j][ w[i][j] ] == 1; j++ );
			if ( j == l )
			{
				++ans;
			}			
		}
		printf( "Case #%d: %d\n", t, ans );
	}	
	return 0;
}