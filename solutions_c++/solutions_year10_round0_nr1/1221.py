#include<stdio.h>
#include<string.h>
FILE	*fin = fopen( "xxx.in" , "r" );
FILE	*fout = fopen( "xxx.out" , "w" );
int n, k, m;
int	main()
{
	fscanf(fin , "%d" , &m);
	for (int i = 1; i <= m; ++ i)
	{
		fscanf(fin , "%d%d" , &n , &k);
		int temp = 1;
		for (int j = 1 ; j <= n ; ++ j)
			temp *= 2;		
		if (( k + 1 ) % temp == 0)
			fprintf( fout , "Case #%d: ON\n" , i );
		else
			fprintf( fout , "Case #%d: OFF\n" , i );
	}
	return 0;
}
