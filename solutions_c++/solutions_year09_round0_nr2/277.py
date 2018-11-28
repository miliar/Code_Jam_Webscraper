#include "stdio.h"
#include <vector>
using namespace std;

char w[200][200];
int h[200][200];
int n, m;
int dx[] = { -1, 0, 0, 1 };
int dy[] = { 0, -1, 1, 0 };
char counter = 'a';

char get( int x, int y )
{
	if( w[x][y] != 0 )
	{
		return w[x][y];
	}

	int lowest = h[x][y], bx=-1, by=-1;
	for( int i=0; i<4; ++i )
	{
		int xx = x+dx[i], yy = y+dy[i];
		if( 0<=xx&&xx<n && 0<=yy&&yy<m && h[xx][yy] < lowest )
		{
			lowest = h[xx][yy];
			bx = xx;
			by = yy;
		}
	}

	if( bx == -1 )
	{
		w[x][y] = counter++;
		return w[x][y];
	}
	w[x][y] = get( bx, by );
	return w[x][y];
}

int main()
{
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );
	int caseNum;
	scanf( "%d", &caseNum );
	for( int ci=0; ci<caseNum; ++ci )
	{
		scanf( "%d%d", &n, &m );
		counter = 'a';
		for( int i=0; i<n; ++i )
		{
			for( int j=0; j<m; ++j )
			{
				scanf( "%d", &h[i][j] );
				w[i][j] = '\0';
			}
		}

		printf( "Case #%d:\n", ci+1 );
		for( int i=0; i<n; ++i )
		{
			for( int j=0; j<m; ++j )
			{
				printf( "%c", get( i, j ) );
				if( j < m-1 )
				{
					printf( " " );
				}
				else
				{
					printf( "\n" );
				}
			}
		}
	}
	return 0;

}