#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define MAXN 10010

int d[MAXN], l[MAXN], dp[MAXN];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		int n, D;
		scanf("%d", &n);
		for(int i = 0; i < n; ++i) scanf("%d%d", d + i, l + i);
		scanf("%d", &D);
		memset(dp, -1, sizeof(dp));
		dp[0] = min(d[0], l[0]);
		for(int i = 0; i + 1 < n; ++i) if(dp[i] != -1) {
			for(int j = i + 1; j < n; ++j) if(d[i] + dp[i] >= d[j]) {
				int t = min(d[j] - d[i], l[j]);
				dp[j] = max(dp[j], t);
			}
		}

//		for(int i = 0; i < n; ++i) printf("%d ", dp[i]);puts("");
		bool ok = false;
		for(int i = 0; i < n && !ok; ++i)
			if(dp[i] != -1 && d[i] + dp[i] >= D) ok = true;
		printf("Case #%d: %s\n", cas, ok? "YES": "NO");
	}
	return 0;
}
