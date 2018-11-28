#include <cstdio>
#include <memory>

const int number = 100003;
const int maxn = 500;

int casei, cases, n;
int ans[maxn + 1];
int combi[maxn + 1][maxn + 1];
int dp[maxn + 1][maxn];

inline void process() {
	memset(combi, 0, sizeof combi);
	for (int i = 0; i <= maxn; ++i) {
		combi[i][0] = 1;
		for (int j = 1; j <= i; ++j) combi[i][j] = (combi[i - 1][j - 1] + combi[i - 1][j]) % number;
	}

	memset(dp, 0, sizeof dp);
	for (int i = 2; i <= maxn; ++i) {
		dp[i][1] = 1;
		ans[i] = 1;
		for (int j = 2; j < i; ++j) {
			dp[i][j] = 0;
			for (int k = j - 1; k >= 0 && i - j >= j - k; --k) {
				long long tmp = dp[j][k];
				tmp *= combi[i - j - 1][j - k - 1];
				tmp %= number;
				dp[i][j] = ((int)tmp + dp[i][j]) % number;
			}
			ans[i] = (ans[i] + dp[i][j]) % number;
		}		
	}
}

int main() {
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	process();
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%d", &n);
		printf("Case #%d: %d\n", casei, ans[n]);
	}
	
	return 0;
}
