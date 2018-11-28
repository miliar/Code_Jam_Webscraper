// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;

#define MAXN 100000

int g[MAXN], c[MAXN];
int dp[MAXN][2];

void update(int &x, int y) {
	if (x < 0 || y < x)
		x = y;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int m, v, val;
		scanf("%d %d", &m, &v);
		memset(dp, -1, sizeof(dp));
		for (int i=1; i<=(m-1)/2; ++i)
			scanf("%d %d", &g[i], &c[i]);
		for (int i=(m-1)/2+1; i<=m; ++i) {
			scanf("%d", &val);
			dp[i][val] = 0;
		}
		for (int i=(m-1)/2; i>0; --i) {
			for (int a=0; a<=1; ++a) {
				if (dp[i*2][a] < 0)
					continue;
				for (int b=0; b<=1; ++b) {
					if (dp[i*2+1][b] < 0)
						continue;
					int x = dp[i*2][a] + dp[i*2+1][b];
					assert(x >= 0);
					if (g[i]) {
						update(dp[i][a&b], x);
						if (c[i])
							update(dp[i][a|b], x+1);
					}
					else {
						update(dp[i][a|b], x);
						if (c[i])
							update(dp[i][a&b], x+1);
					}
				}
			}
		}
		if (dp[1][v] < 0)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", dp[1][v]);
	}
	return 0;
}
