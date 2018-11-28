#include <stdio.h>
#include <string.h>
#define MOD (100003LL)

long long d[510][510];
long long g[510][510];
long long get_g(long long l, long long n)
{
	long long &it = g[l][n];
	if (it != -1)
		return it;
	if (l == 1)
		return it = 1;
	if (n < l)
		return it = 0;
	if (n == l)
		return it = 1;
	it = 0;
	for (int i = 1; i < n; i++)
		it = (it + get_g(l-1, i))%MOD;
	return it;
}
long long solve(long long k, long long n)
{
	long long &it = d[k][n];
	if (it != -1)
		return it;
	if (k == 1)
		return it = 1;
	if (n == 1)
		return 0;
	if (n-1 < k)
		return it = 0;
	long long i;
	it = 0;
	for (i = 1; i < k; i++)
		it = (it + solve(i, k) * get_g(k-i, n-k))%MOD;
	return it;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long T, nt, n, i;
	scanf("%lld", &T);
	memset(d, -1, sizeof(d));
	memset(g, -1, sizeof(g));
	for (nt = 1; nt <= T; nt++)
	{
		scanf("%lld", &n);
		long long ans = 0;
		for (i = 1; i < n; i++)
			ans = (ans + solve(i, n))%MOD;
		printf("Case #%lld: %lld\n", nt, ans);
	}
	return 0;
}
