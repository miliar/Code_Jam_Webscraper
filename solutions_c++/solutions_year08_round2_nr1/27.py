#include <cstdio>

#define Nmax 1028
#define ll long long

int n;
ll a, b, c, d, m;
ll X[Nmax], Y[Nmax];

void citire()
{
	scanf("%d %lld %lld %lld %lld %lld %lld %lld\n", &n, &a, &b, &c, &d, &X[1], &Y[1], &m);
}

void solve()
{
	int i, j, k, sol = 0;

	for (i = 2; i <= n; ++i)
	{
		X[i] = (a * X[i - 1] + b) % m;
		Y[i] = (c * Y[i - 1] + d) % m;
	}

	for (i = 1; i <= n; ++i)
		for (j = i + 1; j <= n; ++j)
			for (k = j + 1; k <= n; ++k)
				if ((X[i] + X[j] + X[k]) % 3 == 0 && (Y[i] + Y[j] + Y[k]) % 3 == 0)
					++sol;

	printf("%d\n", sol);
}

int main()
{
	freopen("date.in", "r", stdin);
	freopen("date.out", "w", stdout);

	int t;

	scanf("%d\n", &t);
	for (int i = 1; i <= t; ++i)
	{
		citire();
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
