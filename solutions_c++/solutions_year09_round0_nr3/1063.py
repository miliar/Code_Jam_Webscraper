#include <stdio.h>
#include <string.h>

char s1[501];
char s2[] = "welcome to code jam";
int n, m;

int d1[500], d2[500];

int main( void )
{
	int nt, t, i, j, k, ans;
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	scanf( "%d\n", &nt );		
	for ( t = 1; t <= nt; t++ )
	{
		gets(s1);
		n = strlen( s1 );
		m = strlen( s2 );
		memset( d1, 0, sizeof(d1) );
		for ( i = 0; i < n; i++ )
		{
			if ( s1[i] == s2[0] )
			{
				d1[i] = 1;
			}
		}
		for ( j = 1; j < m; j++ )
		{
			memset( d2, 0, sizeof(d2) );
			for ( i = 0; i < n; i++ )
			{
				if ( s1[i] == s2[j] )
				{
					for ( k = 0; k < i; k++ )
					{
						d2[i] += d1[k];
						d2[i] %= 10000;
					}										
				}
			}
			for ( i = 0; i < n; i++ )		
			{
				d1[i] = d2[i];		
			}
		}	
		ans = 0;
		for ( i = 0; i < n; i++ )
		{
			ans += d1[i];
			ans %= 10000;				
		}			
		printf( "Case #%d: ", t );
		if ( ans < 1000 )
		{
			printf("0");
		}
		if ( ans < 100 )
		{
			printf("0");
		}
		if ( ans < 10 )
		{
			printf("0");
		}
		printf( "%d\n", ans );
	}	
	return 0;
}