#include <stdio.h>

int	main()
{
	int	T , t = 0;
	scanf("%d" , &T);
	while (T)
	{
		t ++;
		printf("Case #%d: " , t);
		int	N , K;
		scanf("%d%d" , &N , &K);
		int	M = (1 << N);
		if (K % M == M - 1) printf("ON\n");
			else printf("OFF\n");
		T --;
	}
}
