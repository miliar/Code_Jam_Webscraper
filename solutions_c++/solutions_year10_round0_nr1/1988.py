#include <cstdio>

int main()
{
	int T, N, K, i;

	scanf("%d", &T);
	for (i = 1 ; i <= T ; i++)
	{
		scanf("%d", &N);
		scanf("%d", &K);

		printf("Case #%d: %s\n", i, (((K+1) % (1 << N) == 0) && K) ? "ON" : "OFF");
	}

	return 0;
}
