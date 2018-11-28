#include <stdio.h>

int cnt[32];

int main()
{
	freopen( "A.in", "r", stdin );
	freopen( "A.out", "w", stdout );

	int t;
	int n, k;
	int i;
	bool res;

	cnt[1] = 1;
	for( i = 2; i <= 30; ++i )
		{
		cnt[i] = 1 + (cnt[i-1]<<1);
		}//end for

	scanf( "%d", &t );

	for( i = 1; i <= t; ++i )
		{
		scanf( "%d%d", &n, &k );
		if( k < cnt[n] )
			{
			res = false;
			}
		else if( k % (cnt[n] + 1) == cnt[n] )
			{
			res = true;
			}
		else{
			res = false;
			}//end if
		printf( "Case #%d: %s\n", i, (res) ? "ON" : "OFF" );
		}//end for


	return 0;
}
