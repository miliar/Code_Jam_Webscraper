/*
	author: AmazingCaddy
	time: 2011/5/7  13:48
*/
#include <cstdio>
#include <complex>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <vector>
#include <map>
#include <queue>
using namespace std;

const int maxn = 204;
const int maxm = 20000;

struct node
{
	char buf[ 3 ];
	int num;
};
node op[ maxn ];

int Max( int a, int b ) { return ( a > b ? a : b ); }

int main(int argc, char *argv[])
{
	int cas, n;
	//freopen( "A-large.in", "r", stdin );
	//freopen( "A_large.out", "w", stdout );
	scanf( "%d", &cas );
	int orange, blue, sumo, sumb, tmp, ans;
	for( int t = 1; t <= cas; t++ )
	{
		scanf( "%d", &n );
		for( int i = 0; i < n; i++ )
			scanf( "%s%d", op[ i ].buf, &op[ i ].num );
		orange = 1, blue = 1, sumo = 0, sumb = 0;
		ans = 0;
		for( int i = 0; i < n; i++ )
		{
			if( op[ i ].buf[ 0 ] == 'O' )
			{
				tmp = abs( op[ i ].num - orange );
				if( tmp < sumo )
				{
					ans += 1;
					sumb += 1;
				}
				else
				{
					ans += tmp - sumo + 1;
					sumb += tmp - sumo + 1;
				}
				sumo = 0;
				orange = op[ i ].num;
			}
			else
			{
				tmp = abs( op[ i ].num - blue );
				if( tmp < sumb )
				{
					ans += 1;
					sumo += 1;
				}
				else
				{
					ans += tmp - sumb + 1;
					sumo += tmp - sumb + 1;
				}
				sumb = 0;
				blue = op[ i ].num;
			}
		}
		printf( "Case #%d: %d\n", t, ans );
	}
	return 0;
}
