#include<stdio.h>

int modulus( int a )
{
	if( a < 0 ) return -a;
	return a;
}

int main()
{
	//freopen("bot.in","r",stdin);
	//freopen("bot.out","w",stdout);
	int T;
	scanf("%d", &T);
	for( int ii = 1; ii <= T; ++ii)
	{
		int N;
		scanf("%d", &N);
		int poz[ 2 ] = {1,1}, timp[ 2 ]= {1,1}, timpi = 1;
		for( int i = 1; i <= N; ++i)
		{
			char cine;
			int where;
			scanf(" %c %d", &cine, &where);
			int nr = 0;
			if( cine == 'O' )
				nr = 1;
			if( modulus( where - poz[ nr ]) > timpi - timp[ nr ] )
				timpi = timp[ nr ] + modulus( where - poz[ nr ] );
						
			timp[ nr ] = timpi + 1;
			poz[ nr ] = where ;
			timpi++;
			
		}
		printf("Case #%d: %d\n", ii, timpi - 1);
	}
	
	
	
	
	return 0;
}
