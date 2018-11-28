#include <stdio.h>
#include <stdlib.h>

int compare( const void *a, const void *b)
{
	return (*(int*)b) - (*(int*)a);
}


int main(){
	int T, Ti;
	int P, K, L;
	int Ls[1000];
	int impossible;
	int sum;
	int i, p;

	scanf("%d", &T);

	for ( Ti = 0; Ti < T; Ti++ )
	{
		printf("Case #%d: ", Ti+1);

		scanf("%d%d%d", &P, &K, &L);

		for ( i = 0 ; i < L ; i++ )
		{
			scanf("%d", &(Ls[i]));
		}

		qsort(Ls, L, sizeof(int), compare);


		sum = 0;
		p = 0;
		impossible = 0;
		for ( i = 0 ; i < L ; i++ )
		{
			if ( i%K == 0 ) {
				p++;
				if ( p > P ) {
					impossible = 1;
					break;
				}
			}
			
			sum += Ls[i] * p;
		}

		if ( impossible )
		{
			printf("Impossible\n");
		}
		else
		{
			printf("%d\n", sum);
		}

	}

	return 0;
}

