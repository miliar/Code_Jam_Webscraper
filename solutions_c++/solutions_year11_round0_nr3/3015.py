#include <cstdio>

int n;
int v[15];

int calc(int c)
{
	int x = 0, y = 0, s = 0;
	for (int i = 0; i < n; i++)
		if (c & 1<<i)
		{
			x ^= v[i];
			s += v[i];
		}
		else
			y ^= v[i];
	if (y == x)
		return s;
	return 0;
}

int solve()
{
	int total = 0, max = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &v[i]);
		total += v[i];
	}
	
	int comb;
	for (comb = 1; comb < (1<<n)-1; comb++)
	{
		int r = calc(comb);
		if (r > max)
			max = r;
	}
	return max;
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		int r = solve();
		if (r)
			printf("Case #%d: %d\n", t, r);
		else
			printf("Case #%d: NO\n", t);
	}
	return 0;
}

