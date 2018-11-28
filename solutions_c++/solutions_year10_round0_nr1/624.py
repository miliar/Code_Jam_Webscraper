#include <cstdio>

int N, K;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int cases;

	scanf("%d", &cases);
	for (int cas = 0; cas < cases; ++cas)
	{
		scanf("%d%d", &N, &K);
		printf("Case #%d: %s\n", cas + 1, (K % (1 << N)) == ((1 << N) - 1) ? "ON" : "OFF");
	}

	return 0;
}
