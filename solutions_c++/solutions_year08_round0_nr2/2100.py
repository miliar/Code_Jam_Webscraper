#include<stdio.h>

int array[2][21][2];

void main()	{
	int i, j, m, k, t;
	int n[2];

	FILE *in = fopen ( "INPUT.TXT", "r" );
	FILE *out = fopen ( "OUTPUT.TXT", "w" );

	fscanf ( in, "%d", &m );

	for ( i = 1 ; i <= m ; i++ )	{
		int cnt[2] = {0}, sta[2] = {0};

		fscanf ( in, "%d", &t );
		fscanf ( in, "%d%d", &n[0], &n[1] );

		for ( j = 0 ; j < 2 ; j++ )	{
			for ( k = 0 ; k < n[j] ; k++ )	{
				int min, sec;

				fscanf ( in, "%d:%d", &min, &sec );
				array[j][k][0] = min * 60 + sec;
				fscanf ( in, "%d:%d", &min, &sec );
				array[j][k][1] = min * 60 + sec + t;
			}
		}

		for ( t = 0 ; t < 1440 ; t++ )	{
			for ( j = 0 ; j < 2 ; j++ )	{
				for ( k = 0 ; k < n[j] ; k++ )	{
					if ( array[j][k][1] == t )	{
						if ( j == 0 )
							sta[1]++;
						else
							sta[0]++;
					}
				}
			}
			for ( j = 0 ; j < 2 ; j++ )	{
				for ( k = 0 ; k < n[j] ; k++ )	{
					if ( array[j][k][0] == t )	{
						if ( sta[j] == 0 )
							cnt[j]++;
						else
							sta[j]--;
					}
				}
			}
		}

		fprintf ( out, "Case #%d: %d %d\n", i, cnt[0], cnt[1] );
	}

	fcloseall();
}