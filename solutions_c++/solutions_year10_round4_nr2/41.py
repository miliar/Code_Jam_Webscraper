#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

const int MAXP = 10;
const int INF = 0x7f7f7f7f;

int price[1 << MAXP];
int dp[1 << (MAXP + 1)][MAXP + 1];

int main() {
	int caseNum;
	scanf("%d", &caseNum);
	for (int caseIndex = 1; caseIndex <= caseNum; caseIndex++) {
		int p;
		scanf("%d", &p);
		memset(dp, 0x7f, sizeof(int) * (1 << (p + 1)) * (MAXP + 1));
		for (int i = (1 << p); i < (1 << (p + 1)); i++) {
			int m;
			scanf("%d", &m);
			dp[i][m] = 0;
		}
		for (int k = p - 1; k >= 0; k--) {
			for (int i = (1 << k); i < (1 << (k + 1)); i++) {
				scanf("%d", &price[i]);
				int l = i + i;
				int r = l + 1;
				for (int nl = 0; nl <= p; nl++) {
					if (dp[l][nl] < INF) {
						for (int nr = 0; nr <= p; nr++) {
							if (dp[r][nr] < INF) {
								int c = min(nl, nr);
								if (c > 0) {
									dp[i][c - 1] = min(dp[i][c - 1], dp[l][nl] + dp[r][nr]);
								}
								dp[i][c] = min(dp[i][c], dp[l][nl] + dp[r][nr] + price[i]);
							}
						}
					}
				}
			}
		}
		int ans = INF;
		for (int c = 0; c <= p; c++) {
			ans = min(ans, dp[1][c]);
		}
		printf("Case #%d: %d\n", caseIndex, ans);
	}
	return 0;
}
