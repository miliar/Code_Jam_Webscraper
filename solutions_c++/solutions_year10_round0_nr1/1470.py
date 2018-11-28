#include <cstdio>

int T, N, K;

int main()
{
	scanf("%d", &T);
	for(int i = 1;i <= T;++i)
	{
		scanf("%d %d", &N, &K);
		bool lighton = (K % (1 << N) == (1 << N) - 1);
		printf("Case #%d: %s\n", i, lighton ? "ON" : "OFF");
	}
}
