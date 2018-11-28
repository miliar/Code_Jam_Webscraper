#include <stdio.h>

int x[50];
int v[50];
int f[50];

int main()
{
	freopen( "B.in", "r", stdin );
	freopen( "B.out", "w", stdout );

	int c;
	int n, k, b, t;
	int i, j, m;
	int num;
	int cnt;

	scanf( "%d", &c );

	for( i = 1; i <= c; ++i )
		{
		scanf( "%d%d%d%d", &n, &k, &b, &t );
		for( j = 0; j < n; ++j )
			{
			scanf( "%d", &x[j] );
			}//end for
		for( j = 0; j < n; ++j )
			{
			scanf( "%d", &v[j] );
			}//end for
		num = 0;
		for( j = 0; j < n; ++j )
			{
			f[j] = x[j] + v[j] * t;
			if( f[j] >= b )
				{
				++num;
				}//end if
			}//end for
		if( num < k )
			{
			printf( "Case #%d: IMPOSSIBLE\n", i );
			}
		else{
			num = 0;
			cnt = 0;
			for( j = n-1; num < k; --j )
				{
				if( f[j] >= b )
					{
					++num;
					for( m = j + 1; m < n; ++m )
						{
						if( f[m] < b )
							{
							++cnt;
							}//end if
						}//end for
					}//end if
				}//end for
			printf( "Case #%d: %d\n", i, cnt );
			}//end if
		}//end for

	return 0;
}
