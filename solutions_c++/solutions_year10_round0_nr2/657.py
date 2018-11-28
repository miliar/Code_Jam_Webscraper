#include <cstdio>

long gcd(long a, long b)
{
	if (a < b)
		return gcd(b, a);
	if (b == 0)
		return a;
	return gcd(b, a%b);
}

long abs(long a)
{
	return a < 0 ? -a : a;
}

int main()
{
	freopen("p2.in", "r", stdin);
	freopen("p2.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; caseNum++)
	{
		int N;
		long t[5];
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%ld", &t[i]);

		long g = 0;
		for (int i = 0; i < N; i++)
			for (int j = i + 1; j < N; j++)
				g = gcd(g, abs(t[i] - t[j]));
		long k = t[0] % g;
		if (k > 0)
			k = g - k;
		printf("Case #%d: %ld\n", caseNum, k);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
