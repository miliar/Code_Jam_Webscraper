#include<stdio.h>
#include<string.h>

FILE *in = fopen ( "input.txt", "r" );
FILE *out = fopen ( "output.txt", "w" );

char alien[5000][20], str[1000];

int main ( void )	{
	int i, j, k, l, d, n, cnt;

	fscanf ( in, "%d %d %d ", &l, &d, &n );

	for ( i = 0 ; i < d ; i++ )
		fgets ( alien[i], 20, in );

	for ( i = 0 ; i < n ; i++ )	{
		int chk[15][26] = {0};

		fgets ( str, 1000, in );

		for ( j = k = 0 ; j < strlen ( str ) ; j++, k++ )	{
			if ( str[j] == '(' )	{
				while ( str[++j] != ')' )
					chk[k][str[j]-'a'] = 1;
			}
			else
				chk[k][str[j]-'a'] = 1;
		}

		cnt = 0;

		for ( j = 0 ; j < d ; j++ )	{
			for ( k = 0 ; k < l ; k++ )	{
				if ( chk[k][alien[j][k]-'a'] == 0 )
					break;
			}

			if ( k == l )
				cnt++;
		}

		fprintf ( out, "Case #%d: %d\n", i + 1, cnt );
	}

	fcloseall();

	return 0;
}