#include <stdio.h>
#include <string.h>

int tab[110][110];
char ans[110][110];

int n,m;

char search( int x, int y, char c )
{
	int min = -9999;
	int minx, miny;
	if( x - 1 >= 0 && tab[x][y] > tab[x-1][y] )
	{
		if( min == -9999 || tab[x-1][y] < min )
		{
			min = tab[x-1][y];
			minx = x-1;
			miny = y;
		}
	}
	if( y-1 >= 0 && tab[x][y] > tab[x][y-1] )
	{
		if( min == -9999 || tab[x][y-1] < min )
		{
			min = tab[x][y-1];
			minx = x;
			miny = y-1;
		}
	}
	if( y+1 < m && tab[x][y] > tab[x][y+1] )
	{
		if( min == -9999 || tab[x][y+1] < min )
		{
			min = tab[x][y+1];
			minx = x;
			miny = y+1;
		}
	}
	if( x + 1 < n && tab[x][y] > tab[x+1][y] )
	{
		if( min == -9999 || tab[x+1][y] < min )
		{
			min = tab[x+1][y];
			minx = x+1;
			miny = y;
		}
	}
	if( ans[x][y] != 0 )
	{
		return ans[x][y];
	}
	if( min == -9999 )
	{
		ans[x][y] = c;
		return c;
	}
	else
	{
		ans[x][y] = search( minx, miny, c);
		return ans[x][y];
	}
}	

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("2.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int ca;
	int i,j;
	for( ca = 1; ca <= T; ca ++ )
	{
		memset( ans, 0, sizeof(ans));
		scanf("%d%d", &n, &m);
		for( i = 0; i < n; i ++ )
		{
			for( j = 0; j < m; j ++ )
			{
				scanf("%d", &tab[i][j]);
			}
		}
		char c = 'a';
		for( i = 0; i < n; i ++ )
		{
			for( j = 0; j < m; j ++ )
			{
				if( ans[i][j] != 0 )
					continue;
				if( search( i, j, c) == c )
				{
					c ++;
				}
			}
		}
		printf("Case #%d:\n", ca);
		for( i = 0; i < n; i ++ )
		{
			for( j = 0; j < m-1; j ++ )
			{
				printf("%c ", ans[i][j]);
			}
			printf("%c\n", ans[i][j]);
		}
	}
	return 0;
}	