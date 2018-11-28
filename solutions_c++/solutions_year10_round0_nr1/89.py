#include <cstdio>

int N, K;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		scanf("%d%d", &N, &K);
		printf("Case #%d: %s\n", Case, (K & ((1 << N) - 1)) == ((1 << N) - 1) ? "ON" : "OFF");
	}
	return 0;
}
