#include <cstdio>
#include <cstring>
#include <string>
#include <map>

using namespace std;

const int P = 100003;

long long res[501][500], c[500][500];
int n;

long long get(int n, int k)
{
	if (k > n) return 0;
	return c[n][k];
}

void solve()
{
	for (int n = 0; n < 500; ++n)
	{
		c[n][0] = 1;
		for (int k = 1; k <= n; ++k)
			c[n][k] = c[n-1][k] + c[n-1][k-1];
	}

	for (int n = 2; n <= 500; ++n)
	{
		res[n][1] = 1;

		for (int k = 2; k < n; ++k)
			for (int i = 1; i < k; ++i)
				res[n][k] = ((res[n][k] + (res[k][i] * get(n-k-1, k-i-1)) % P) % P);
	}
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	solve();

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		scanf("%d", &n);

		long long sum = 0;
		for (int k = 1; k < n; ++k) sum = (sum + res[n][k]) % P;

		printf("%lld\n", sum);
	}

	return 0;
}
