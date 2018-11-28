#include <stdio.h>
#include <string.h>

#define MAXT 64

//char m[MAXT][MAXT];
int max[MAXT];
int t;

int procuraPrimeiroETroca(int m)
{
	int i;
	int trocas;

	for ( i = m ; i < t ; i++ )
	{
		if ( max[i] <= m )
			break;
	}

	trocas = 0;

	for (int j = i ; j > m ; j-- )
	{
		int temp;
		temp = max[j];
		max[j] = max[j-1];
		max[j-1] = temp;

		trocas ++;
	}

	return trocas;
}

int faz()
{
	int trocas = 0;
	int m = 0;
	while ( 1 )
	{
		if ( m >= t ) 
			break;
	
//		printf("[%d]\n",max[m]);
		if ( !( max[m] <= m ) )
		{
			trocas += procuraPrimeiroETroca(m);
		}
		m++;
	}

	return trocas;
}

int main (void)
{
	int n;

	scanf("%d",&n);

	for ( int i = 0 ; i < n ; i++ )
	{
		scanf("%d",&t);

		memset(max, 0, sizeof(max));

		for ( int j = 0 ; j < t ; j++ )
		{
			for ( int k = 0 ; k < t ; k++ )
			{
				char temp;
//				scanf(" %c",&m[j][k]);
				scanf(" %c",&temp);
//				if ( m[j][k] == '1' && k > max[j] )
				if ( temp == '1' && k > max[j] )
					max[j] = k;
			}
		}

		printf("Case #%d: ",i+1);
		printf("%d\n",faz());
	}

	return 0;
}

