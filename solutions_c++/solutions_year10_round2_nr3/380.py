#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

typedef long long ll;
const ll MOD = 100003;

ll cf[512];
ll csf[512][512];
ll pascal[512][512];

ll sf(int n, int m);
ll f(int n)
{
	if (cf[n] != -1) return cf[n];
	ll res = 1;
	for (int m = 2; m < n; m++) res = (res + sf(n, m)) % MOD;
	cf[n] = res;
	return res;
}

ll sf(int n, int m)
{
	ll& dp = csf[n][m];
	if (dp != -1) return dp;
	if (m == 1) return 1;
	dp = 0;
	for (int k = 1; k < m; k++) {
		int N = n - m - 1;
		int K = m - k - 1;
		dp = (dp  + sf(m, k) * pascal[N][K]) % MOD;
	}
	return dp;
}


void precalc(void)
{
	pascal[0][0] = pascal[1][0] = pascal[1][1] = 1;
	for (int n = 2; n < 512; n++)
		for (int k = 0; k <= n; k++) {
			pascal[n][k] = pascal[n - 1][k];
			if (k) pascal[n][k] += pascal[n - 1][k - 1];
		}
	memset(cf, 0xff, sizeof(cf));
	memset(csf, 0xff, sizeof(csf));
	for (int i = 2; i <= 500; i++)
		f(i);
}

int main(void)
{
	precalc();
// 	printf("--prcalced\n");
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: %d\n", i + 1, (int) cf[n]);
	}
	return 0;
}
