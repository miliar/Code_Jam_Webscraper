#include <stdio.h>
#include <string.h>

int ABS( int p )
{
	return ( p < 0  ? -p : p);
}

int main()
{

	int N, T, C, min, i, I, x, total;
	char ob[5];
	int pos;
	scanf("%d",&N);
	int last_b, last_o, min_b, min_o, p;
	char last;
	for(I=0; I<N; ++I)
	{
		// T steps
		scanf("%d",&T);
		int match = 0;
		for(i=0; i<T; ++i)
		{
			scanf("%d",&p);
			if ( p == i + 1) ++match;
		}
		printf("Case #%d: ", I+1);
		printf("%d.000000\n", T-match);
	}
	return 0;
}