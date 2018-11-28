#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 10086;

int dp[MAXN];
int d[MAXN], L[MAXN];

int main() {
	int i, j, k;
	int m, n;
	int tc, D, cn(0);

	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &tc);
	while (tc--) {
		scanf("%d", &n);
		for (i=0; i<n; ++i) scanf("%d%d", d+i, L+i);
		scanf("%d", &D);
		memset(dp, -1, sizeof(dp));
		dp[0] = d[0];
		for (i=0; i<n; ++i) {
			for (j=i+1; j<n; ++j) {
				if (dp[i] + d[i] < d[j]) break;
				k = min(L[j], d[j]-d[i]);
				if (dp[j] == -1) dp[j] = k;
				else dp[j] = max(dp[j], k);
			}
		}
		printf("Case #%d: ", ++cn);
		for (i=0; i<n; ++i) if (dp[i] + d[i] >= D) break;
		if (i < n) puts("YES");
		else puts("NO");
	}

	return 0;
}