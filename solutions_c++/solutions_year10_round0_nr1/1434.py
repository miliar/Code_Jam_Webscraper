#include <cstdio>

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	int T;
	scanf("%u", &T);
	for (int tc = 0; tc < T; ++tc)
	{
		int N, K;
		scanf("%u %u", &N, &K);
		printf("Case #%u: %s\n", tc + 1, (K & ((1 << N) - 1)) == (1 << N) - 1 ? "ON" : "OFF");
	}
	return 0;
}
