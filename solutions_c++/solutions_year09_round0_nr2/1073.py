#include <stdio.h>
#include <string.h>

int h[100][100]; 
char label[100][100];
int n, m;

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};
int nlabel;

char rec( int i, int j )
{	
	int k, x, y, minx, miny;
	if ( label[i][j] )
	{
		return label[i][j];
	}
	minx = -1;
	for ( k = 0; k < 4; k++ )
	{
		x = i + dx[k];
		y = j + dy[k];
		if ( x < 0 || x >= n || y < 0 || y >= m )
		{
			continue;
		}
		if ( h[x][y] < h[i][j] && ( minx == -1 || h[x][y] < h[minx][miny] ) )
		{
			minx = x;
			miny = y;
		}		
	}
	if ( minx == -1 )
	{
		label[i][j] = 'a' + nlabel;
		++nlabel;
	}
	else
	{
		label[i][j] = rec( minx, miny );	
	}
	return label[i][j];
}

int main( void )
{
	int nt, t, i, j;
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	scanf( "%d", &nt );
	for ( t = 1; t <= nt; t++ )
	{				
		scanf( "%d%d", &n, &m );
		for ( i = 0; i < n; i++ )
		{
			for ( j = 0; j < m; j++ )
			{
				scanf( "%d", &h[i][j] );
			}
		}				
		nlabel = 0;
		memset( label, 0, sizeof(label) );
		for ( i = 0; i < n; i++ )
		{
			for ( j = 0; j < m; j++ )
			{
				rec( i, j );
			}
		}
		printf( "Case #%d:\n", t );
		for ( i = 0; i < n; i++ )
		{
			for ( j = 0; j < m; j++ )
			{
				if ( j )
				{
					printf(" ");
				}
				printf( "%c", label[i][j] );
			}
			printf("\n");
		}
	}
	return 0;
}