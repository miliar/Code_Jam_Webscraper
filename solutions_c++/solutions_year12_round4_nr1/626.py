#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int T, D, n;
int d[100000], l[100000];
int dp[100001];

bool gao() {
	memset(dp, -1, sizeof(dp));
	dp[0] = d[0] + min(d[0], l[0]);
	for (int i = 0; i < n; ++i) {
		if (dp[i] == -1) {
			continue;
		}
		for (int j = i + 1; j < n && dp[i] >= d[j]; ++j) {
			int t = min(l[j], d[j] - d[i]);
			dp[j] = max(dp[j], d[j] + t);
		}
	}
	for (int i = 0; i < n; ++i) {
		if (dp[i] >= D) {
			return true;
		}
	}
	return false;
}

int main() {
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &D);
		printf("Case #%d: %s\n", caseNum, gao() ? "YES" : "NO");
	}
	return 0;
}
