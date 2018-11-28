#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
const int MAXN = 1007;
int g[MAXN];

int main() {
	//freopen("in", "r", stdin);
	//freopen("out", "w", stdout);
	int t, n, var = 0, x;
	scanf("%d", &t);
	while (t -- ) {
		scanf("%d", &n);
		for (int i = 1 ; i <= n ; i ++ ) {
			scanf("%d", &g[i]);
		}
		int ans = 0;
		for (int i = 1 ; i <= n ; i ++ ) {
			if (g[i] == 0 || g[i] == i) continue;
			int cur = i;
			int cnt = 0;
			while (g[cur]) {
				int d = cur;
				cur = g[cur];
				g[d] = 0;
				cnt ++;
			}
			ans += cnt;
		}
		printf("Case #%d: %d.000000\n", ++var, ans);

	}
	return 0;
}