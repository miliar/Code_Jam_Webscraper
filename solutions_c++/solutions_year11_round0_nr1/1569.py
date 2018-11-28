#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>

using namespace std;

namespace gcj {
	const int N = 110;

	struct Once {
		bool isO;
		int num;
		Once(bool isO = false, int num = 0) :
			isO(isO), num(num) {}
	};

	Once pushs[N];
	int dp[2][N];
	int pos[2];

	void solve() {
		int n, m, tc;
		scanf("%d", &tc);
		for (int ti = 1; ti <= tc; ti++) {
			memset(dp, 0, sizeof(dp));
			scanf("%d", &n);
			for (int i = 1; i <= n; i++) {
				char c;int k;
				scanf(" %c%d", &c, &k);
				pushs[i] = Once(c == 'O', k);
			}
			pos[0] = pos[1] = 1;
			for (int i = 1; i <= n; i++) {		
				int j = pushs[i].isO;
				dp[1 - j][i] = dp[1 - j][i - 1];
				dp[j][i] = dp[j][i - 1] + abs(pushs[i].num - pos[j]) + 1;
				pos[j] = pushs[i].num;
				if (pushs[i - 1].isO != j) {
					dp[j][i] = max(dp[j][i], dp[1 - j][i - 1] + 1);
				}
			}
			printf("Case #%d: %d\n", ti, max(dp[0][n], dp[1][n]));
		}
	}
}

int main() {
	gcj::solve();
	return 0;
}
