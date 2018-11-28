#include <stdio.h>

int main()
{
	int N, T, C, min, i, I, x, total;
	scanf("%d",&N);
	for(I=0; I<N; ++I)
	{
		x = total = 0;
		scanf("%d",&T);
		for(i=0; i<T; ++i)
		{
			scanf("%d",&C);
			total += C;
			if( i==0 ) { min = C; }
			else if( C < min) { min = C; }
			x ^= C;
		}
		printf("Case #%d: ", I+1);
		if( x == 0 )
		{
			printf("%d\n", total-min);
		}
		else
			printf("NO\n");
	}
	return 0;
}