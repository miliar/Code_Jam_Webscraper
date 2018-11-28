#include <stdio.h>

const int M = 100;
const int N = 500010;
const int MOD = 1000000007;

typedef long long LL;

int n, m, X, Y, Z;
int A[M], S[N];
LL dp[N];

void generate() {
	int i;
	for(i = 0; i < n; ++i) {
		S[i] = A[i%m];
		A[i%m] = ((LL)X*A[i%m]+(LL)Y*(i+1))%Z;
	}
}

void solve() {
	int i, j, k;
	for(i = 0; i < n; ++i) dp[i] = 1;
	for(i = 1; i < n; ++i) {
		for(j = 0; j < i; ++j) {
			if(S[j] < S[i]) {
				dp[i] += dp[j];
				dp[i] %= MOD;
			}
		}
	}
	LL sum = 0;
	for(i = 0; i < n; ++i) {
		sum += dp[i];
		sum %= MOD;
	}
	printf("%I64d\n", sum);
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small.txt", "w", stdout);

	int ntc, i, j, k, tc=0;
	scanf("%d", &ntc);
	while(ntc--) {
		printf("Case #%d: ", ++tc);
		scanf("%d%d%d%d%d", &n, &m, &X, &Y, &Z);
		for(i = 0; i < m; ++i) scanf("%d", A+i);
		generate();
//		for(i = 0; i < n; ++i) printf("%d ", S[i]); printf("\n");

		solve();
	}
	return 0;
}
