#include <cstdio>
void solve()
{
	int min = 1e9;
	int sum = 0;
	int N;
	scanf ("%d", &N);
	int t;
	int x[30];
	for (int i = 0; i < N; ++i)
	{
		scanf ("%d", &t);
		if (t < min) min = t;
		sum += t;
		for (int j = 0; j < 30; ++j)
		{
			if (t & (1 << j))
			{
				++x[j];
			}
		}
	}
	for (int i = 0; i < 30; ++i)
	{
		if (x[i] & 1)
		{
			printf ("NO\n");
			return;
		}
	}
	printf("%d\n", sum - min);
}
int main()
{
	freopen("test.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf ("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}