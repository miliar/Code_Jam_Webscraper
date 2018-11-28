#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 128;
int x[maxn], v[maxn], ok[maxn];
int n, k, b, t;

int solve() {
	int cnt = 0;
	for (int i = 0; i < n; ++i) {
		ok[i] = (v[i] * t >= b - x[i]);
		cnt += ok[i];
	}
	if (cnt < k) return -1;

	int res = 0;
	
	for (int i = 0; i < k; ++i) {
		for (int j = n - i - 1; j >= 0; --j) 
			if (ok[j]) {
				swap(ok[n-i-1], ok[j]);
				res += n - i - 1 - j;
				break;
			}
	}
	return res;
}

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T, tc = 0;
	scanf("%d",&T);
	while (T --) {
		scanf("%d%d%d%d", &n, &k, &b, &t);
		for (int i = 0; i < n; ++i)
			scanf("%d", x+i);
		for (int i = 0; i < n; ++i)
			scanf("%d", v+i);
		int ans = solve();
		if (ans == -1) 
			printf("Case #%d: IMPOSSIBLE\n", ++tc);
		else
			printf("Case #%d: %d\n", ++tc, ans);

	}
	return 0;
}

