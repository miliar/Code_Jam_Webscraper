#include <stdio.h>

int main()
{
	freopen( "C.in", "r", stdin );
	freopen( "C.out", "w", stdout );

	int t, i;
	int n, j;
	int c;
	int sum;
	int xsum;
	int min;

	for( scanf( "%d", &t ), i = 1; i <= t; ++i )
		{
		xsum = sum = 0;
		min = 0x7fffffff;
		for( scanf( "%d", &n ), j = 0; j < n; ++j )
			{
			scanf( "%d", &c );
			sum += c;
			xsum ^= c;
			if( c < min )
				{
				min = c;
				}//end if
			}//end for
		printf( "Case #%d: ", i );
		if( xsum == 0 )
			{
			printf( "%d", sum - min );
			}
		else{
			printf( "NO" );
			}//end if
		putchar( '\n' );
		}//end for

	return 0;
}
