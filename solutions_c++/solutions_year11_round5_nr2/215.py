#include <cstdio>
#include <algorithm>

int start[1010];
int work() {
	int cnt[10010] = {};
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		int v;
		scanf("%d", &v);
		++cnt[v];
	}
	int f = 0, c = 0;
	int ans = n;
	for (int i = 1; i <= 10001; ++i) {
		int d = cnt[i] - cnt[i - 1];
		while (d > 0) {
			start[c++] = i;
			--d;
		}
		while (d < 0) {
			int v = i - start[f++];
			if (v < ans)
				ans = v;
			++d;
		}
	}
	return ans;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: %d\n", i + 1, work());
	}
}
