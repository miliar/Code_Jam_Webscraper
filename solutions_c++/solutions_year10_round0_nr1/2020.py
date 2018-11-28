#include <stdio.h>

int main()
{
	int T, test;
	scanf("%d", &T);
	for (test=0;test<T;test++)
	{
		int N, K, pow2;
		scanf("%d %d", &N, &K);
		pow2 = 1<<N;
		K%=pow2;

		if (K==pow2-1) printf("Case #%d: ON\n", test+1);
		else printf("Case #%d: OFF\n", test+1);
	}

	return 0;
}