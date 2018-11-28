#include <string.h>
#include <stdio.h>
#include <algorithm>

using namespace std;

int a[1024];
int sa[1024];

int main()
{
	freopen( "D.in", "r", stdin );
	freopen( "D.out", "w", stdout );

	int t, i;
	int n, j;
	int num;

	for( scanf( "%d", &t ), i = 1; i <= t; ++i )
		{
		for( scanf( "%d", &n ), j = 0; j < n; ++j )
			{
			scanf( "%d", &a[j] );
			}//end for
		memcpy( sa, a, sizeof(a[0]) * n );
		sort( sa, sa + n );
		num = 0;
		for( j = 0; j < n; ++j )
			{
			if( sa[j] != a[j] ) ++num;
			}//end for
		printf( "Case #%d: %d\n", i, num );
		}//end for

	return 0;
}
