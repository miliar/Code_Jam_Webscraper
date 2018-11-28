#include <stdio.h>

#define min(a,b) ((a)<(b)?(a):(b))
int main()
{
	freopen( "B-small-attempt0.in", "r", stdin );
	freopen( "qr_b_small_0.out", "w", stdout );

	int T, N, nSurprise, bestMin, totalPoint, bestMinCount, nSingle;

	scanf( "%d", &T );

	for( int kase = 1; kase <= T; kase++ )
	{
		nSingle = bestMinCount = 0;

		scanf( "%d%d%d", &N, &nSurprise, &bestMin );

		for( int i = 1; i <= N; i++ )
		{
			scanf( "%d", &totalPoint );
			
			if( bestMin == 0 || 3*bestMin-2 <= totalPoint )
			{
				bestMinCount++;
			}
			if( bestMin >= 2 && ( 3*bestMin-4 == totalPoint || totalPoint == 3*bestMin-3 ))
			{
				nSingle++;
			}
		}
		
		bestMinCount += min( nSurprise, nSingle );

		printf( "Case #%d: %d\n", kase, bestMinCount );
	}
	return 0;
}

