#include <stdio.h>
#include <algorithm>

const int mod = 100003, max = 500;
int P[max + 1][max + 1];
int T[max + 1][max];

void solve()
{
	int n, s = 0;
	scanf("%d", &n);
	for (int i = 1; i < n; i++)
		s = (s + T[n][i]) % mod;
	printf("%d\n", s);
}

int main()
{
	P[0][0] = 1;
	for (int i = 1; i <= max; i++)
	{
		P[i][0] = 1;
		for (int j = 1; j < i; j++)
			P[i][j] = (P[i - 1][j - 1] + P[i - 1][j]) % mod;
		P[i][i] = 1;
	}
	T[2][1] = 1;
	for (int i = 3; i <= max; i++)
	{
		T[i][1] = 1;
		for (int r = 2; r < i; r++)
			for (int rr = 1; rr < r; rr++)
				if (r - rr - 1 <= i - r - 1)
					T[i][r] = (T[i][r] + (long long)T[r][rr] * P[i - r - 1][r - rr - 1] % mod) % mod;
	}
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}