#include <cstdio>
using namespace std;

typedef long long LL;
LL a[1005], A[1005], dp[1005], X, Y, Z;
int n, m;
void gen() {
	for (int i = 0; i < n; ++i) {
		a[i] = A[i%m];
		A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;
	}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int nn, mod = 1000000007;

	scanf("%d", &nn);
	for (int cas = 1; cas <= nn; ++cas) {
		scanf("%d%d%lld%lld%lld", &n, &m, &X, &Y, &Z);
		for (int i = 0; i < m; ++i)
			scanf("%d", &A[i]);
		gen();
		dp[0] = 1;
		for (int i = 1; i < n; ++i) {
			dp[i] = 1;
			for (int j = 0; j < i; ++j) 
				if (a[i] > a[j])
					dp[i] = (dp[i] + dp[j]) % mod;
		}
		LL ans = 0;
		for (int i = 0; i < n; ++i)
			ans = (ans + dp[i]) % mod;
		printf("Case #%d: %lld\n", cas, ans);
	}
	return 0;
}
