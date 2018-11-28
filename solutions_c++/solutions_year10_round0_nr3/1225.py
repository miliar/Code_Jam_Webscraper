#include<stdio.h>
#include<string.h>
FILE	*fin = fopen( "xxx.in" , "r" );
FILE	*fout = fopen( "xxx.out" , "w" );
int T;
int	main()
{
	fscanf( fin , "%d" , &T );
	for ( int wyf = 1 ; wyf <= T ; ++ wyf )
	{
		int r , k , n;
		fscanf( fin , "%d%d%d" , &r , &k , &n );
		int a[ 2000 ] , b[ 2000 ];
		memset( a , sizeof(a) , 0 );
		memset( b , sizeof(b) , 0 );
		for ( int i = 1 ; i <= n ; ++ i )
			fscanf( fin , "%d" , a + i );
		for ( int i = 1 ; i <= n ; ++ i )
		{
			b[i] = a[i];
			b[i] += b[ i - 1 ];
		}
		long long tot = 0;
		int mark = 1;
		if ( k > b[n] )
		{
			fprintf( fout , "Case #%d: %lld\n" , wyf , ( long long )b[n] * ( long long )r );
			continue;
		}
		for ( int i = 1 ; i <= r ; ++ i )
		{
			int temp = 0;
			while ( temp + a[mark] <= k )
			{
				tot += a[mark];
				temp += a[mark];
				mark ++;
				if ( mark > n )	mark = 1;
			}
		}
		fprintf( fout , "Case #%d: %lld\n" , wyf , tot );
	}
	return 0;
}
