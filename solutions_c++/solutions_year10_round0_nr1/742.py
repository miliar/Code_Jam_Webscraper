#include <cstdio>

int T;
int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t ++)
	{
		int N, K;
		scanf("%d %d", &N, &K);
		int mod = 1 << N;
		K %= mod;
		printf("Case #%d: %s\n", t, K == (1 << N) - 1 ? "ON" : "OFF");
	}
}
