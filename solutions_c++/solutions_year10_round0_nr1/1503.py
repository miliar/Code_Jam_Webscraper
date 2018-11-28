#include <stdio.h>

int main()
{
	int nT;
	scanf("%d", &nT);
	for(int T = 1; T <= nT; T++)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		printf("Case #%d: %s\n", T, (K&(1<<(N-1)) && (K&(1<<(N-1)))!=((K+1)&(1<<(N-1))))?"ON": "OFF");
	}
	return 0;
}
