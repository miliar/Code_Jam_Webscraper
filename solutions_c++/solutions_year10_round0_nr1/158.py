#include <cstdio>
#include <cmath>

int	main()
{
	int	T , now = 0;
	scanf("%d" , &T);
	while (T)
	{
		now ++;
		printf("Case #%d: " , now);
		int	N , K;
		scanf("%d%d" , &N , &K);
		int	M = (1 << N);
		if (K % M == M - 1) printf("ON\n");
			else printf("OFF\n");
		T --;
	}
}
