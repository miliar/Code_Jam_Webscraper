#include<stdio.h>


int main()
{
	int TT;
	//freopen("candy.in","r",stdin);
	//freopen("candy.out","w",stdout);
	scanf("%d", &TT);
	for( int ii = 1; ii <= TT; ++ii)
	{
		int N;
		scanf("%d", &N);
		
		int rez = 0, min = (1 << 20 ), sum = 0;
		for( int i = 1; i <= N; ++i)
		{
			int a;
			scanf("%d", &a);
			rez ^= a;
			sum += a;
			if( a < min ) min = a;
		}
		if( rez == 0 )
		{
			printf("Case #%d: %d\n", ii, sum - min );
		}
		else printf("Case #%d: NO\n", ii);

		
	}
	
	
	
	return 0;
}
