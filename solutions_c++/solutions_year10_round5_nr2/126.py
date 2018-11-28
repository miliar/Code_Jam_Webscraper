#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int dp[10000 + 100];
int len[128];

long long run()
{
	memset(dp, -1, sizeof(dp));
	long long l;
	scanf("%lld", &l);
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		scanf("%d", len + i);
	}
	dp[0] = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j + len[i] <= 10000; ++j) {
			if (dp[j] != -1) {
				int next = dp[j] + 1;
				if (dp[j + len[i]] == -1 || dp[j + len[i]] > next) {
					dp[j + len[i]] = next;
				}
			}
		}
	}
	long long best = -1;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j <= 10000 && j <= l; ++j) {
			if (dp[j] == -1) continue;
			if ((l - j) % len[i] == 0) {
				long long next = (l - j) / len[i] + dp[j];
				if (best == -1 || next < best) best = next;
			}
		}
	}
	return best;
}

int main()
{
	freopen("B1.in", "r", stdin);
	freopen("B1.txt", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		long long ret = run();
		printf("Case #%d: ", i);
		if (ret == -1) {
			puts("IMPOSSIBLE");
		}
		else {
			printf("%lld\n", ret);
		}
	}
	return 0;
}