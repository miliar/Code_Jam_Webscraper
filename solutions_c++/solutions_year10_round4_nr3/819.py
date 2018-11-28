#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;
#define N 201
int r;
int mp[2][N][N], mp2[N][N];

int main( )
{
	freopen( "C-small.in", "r", stdin );
	freopen( "C-small.out", "w", stdout );
	int ca, t, cnt;
	int i, j, k, x1, y1, x2, y2;
	scanf( "%d", &ca );
	for ( t = 1; t <= ca; t++ )
	{
		scanf( "%d", &r );
		memset( mp, 0, sizeof(mp) );
		for ( i = 0; i < r; i++ )
		{
			scanf( "%d%d%d%d", &x1, &y1, &x2, &y2 );
			if ( x1 > x2 ) swap( x1, x2 );
			if ( y1 > y2 ) swap( y1, y2 );
			for ( j = y1; j <= y2; j++ )
			{
				for ( k = x1; k <= x2; k++ )
					mp[0][j][k] = 1;
			}
		}
		cnt = 0;
		int pre = 0, cur = 1;
		int mark = 0;
	/*	for ( i = 1; i <= 6; i++ )
		{
			for ( j = 1; j <= 6; j++ )printf( "%d", mp[pre][i][j] );
			puts( "" );
		}
		puts( "" );*/

		while ( 1 )
		{
			mark = 0;
			for ( i = 1; i < N; i++ )
				for ( j = 1; j < N; j++ )
					mp[cur][i][j] = 0;
			for ( i = 1; i < N; i++ )
				for ( j = 1; j < N; j++ )
					if ( mp[pre][i][j] )
						mark = 1;
			/*for ( i = 1; i <= 8; i++ )
			{
				for ( j = 1; j <= 8; j++ )printf( "%d", mp[pre][i][j] );
				puts( "" );
			}
			puts( "" );*/
			if ( !mark ) break;
			for ( i = 1; i < N; i++ )
				for ( j = 1; j < N; j++ )
				{
					if ( mp[pre][i][j] )
					{
						if ( mp[pre][i-1][j] || mp[pre][i][j-1] )
							mp[cur][i][j] = 1;
						else mp[cur][i][j] = 0;
					}
					else
					{
						if ( mp[pre][i-1][j] && mp[pre][i][j-1] )
							mp[cur][i][j] = 1;
						else mp[cur][i][j] = 0;
					}
				}
			pre ^= 1;
			cur ^= 1;
			cnt++;
		}
		printf( "Case #%d: %d\n", t, cnt );
	}
}
