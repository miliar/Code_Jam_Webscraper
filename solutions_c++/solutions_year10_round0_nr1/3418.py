#include <cstdio>

void main()
{
	unsigned int T, N, K, M;

	scanf("%u\n",&T);
	for (unsigned int i=1;i<=T;++i)
	{
		scanf("%u %u\n",&N, &K);
		M = (1 << N)- 1;
		printf("Case #%u: %s\n", i, ((K&M)==M) ? "ON" : "OFF");
	}
	return;
}
