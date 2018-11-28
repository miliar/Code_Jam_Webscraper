#include <cstdio>

void Solve(int testId, long n, long k)
{
	printf("Case #%d: ", testId);
	long p2 = 1 << n;
	if (k % p2 == p2-1)
		printf("ON\n");
	else
		printf("OFF\n");
}

void Solve()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		long n, k;
		scanf("%ld%ld", &n, &k);
		Solve(i, n, k);
	}
}

void OpenFiles()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

int main()
{
	OpenFiles();
	Solve();
	return 0;
}