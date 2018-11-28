#include<stdio.h>
#include<string.h>

int array[11][101];

void main()	{
	int i, j, k, n, min;
	int s, q;
	char list[11][101];
	char str[101];

	FILE *in = fopen ( "INPUT.TXT", "r" );
	FILE *out = fopen ( "OUTPUT.TXT", "w" );

	fscanf ( in, "%d", &n );

	for ( i = 1 ; i <= n ; i++ )	{
		fscanf ( in, "%d ", &s );

		for ( j = 1 ; j <= s ; j++ )
			fgets ( list[j], 101, in );

		fscanf ( in, "%d ", &q );

		for ( j = 1 ; j <= q ; j++ )	{
			fgets ( str, 101, in );

			for ( k = 1 ; k <= s ; k++ )	{
				if ( strcmp ( str, list[k] ) == 0 )
					array[k][j] = -1;
				else if ( array[k][j-1] == -1 )	{
					min = 100;

					for ( int ii = 1 ; ii <= s ; ii++ )	{
						if ( array[ii][j-1] < min && array[ii][j-1] != -1 )
							min = array[ii][j-1];
					}

					array[k][j] = min + 1;
				}
				else
					array[k][j] = array[k][j-1];
			}
		}

		min = 100;
		for ( j = 1 ; j <= s ; j++ )	{
			if ( array[j][q] < min && array[j][q] != -1 )
				min = array[j][q];
		}

		fprintf ( out, "Case #%d: %d\n", i, min );
	}

	fcloseall();
}