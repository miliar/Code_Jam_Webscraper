#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int INF = 0x3f3f3f3f;
int dp[105][257];
int D, I, M, N;
int a[105];

int main()
{
	int T;

	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d %d %d", &D, &I, &M, &N);
		for (int i = 1; i <= N; ++i) {
			scanf("%d", &a[i]);
		}
		memset(dp[0], 0x3f, sizeof(dp));
		dp[0][256] = 0;
		for (int i = 1; i <= N; ++i) {
			//delete
			for (int j = 0; j < 257; ++j)
				dp[i][j] = min(dp[i][j], dp[i - 1][j] + D);
			//change
			for (int j = 0; j < 256; ++j) {
				for (int k = max(0, j - M); k <= min(255, j + M); ++k) {
					dp[i][k] = min(dp[i][k], dp[i - 1][j] + abs(a[i] - k));
				}
			}
			for (int k = 0; k < 256; ++k) {
				dp[i][k] = min(dp[i][k], dp[i - 1][256] + abs(a[i] - k));
			}
			//insert
			int flag[256] = { 0 };
			for (int j = 0; j < 256; ++j) {
				int ind = -1;
				int dist = INF;
				for (int k = 0; k < 256; ++k) {
					if (flag[k] == 0 && dp[i][k] < dist) {
						dist = dp[i][k];
						ind = k;
					}
				}
				//if (ind == -1)
				//	break;
				for (int k = max(0, ind - M); k <= min(255, ind + M); ++k)
					dp[i][k] = min(dp[i][k], dist + I);
				flag[ind] = 1;
			}
		}
		int res = INF;
		for (int i = 0; i < 256; ++i)
			res = min(res, dp[N][i]);
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
