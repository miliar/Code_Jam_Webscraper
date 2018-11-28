#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;
inline int max(int a, int b) { return a > b ? a : b; }
inline int min(int a, int b) { return a < b ? a : b; }
int tests, n, m[2048], f[2048], price[2048];

int dfs(int now, int x) {
	if (now >= (1 << n)) {
		if (x >= n - m[now - (1 << n)]) return 0;
		else return -1;
	}
	int p = dfs(now << 1, x), q = dfs((now << 1) + 1, x);
	int tmp = 0x7FFFFFFF;
	if (p != -1 && q != -1) tmp = p + q;
	p = dfs(now << 1, x + 1), q = dfs((now << 1) + 1, x + 1);
	if (p != -1 && q != -1) tmp = min(tmp, p + q + price[now]);
	if (tmp == 0x7FFFFFFF) return -1;
	else return tmp;
}

int main(int argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tests);
	for (int cases = 1; cases <= tests; ++ cases) {
		scanf("%d", &n);
		for (int i = 0; i < (1 << n); ++ i)
			scanf("%d", &m[i]);
		for (int i = n - 1; i >= 0; -- i) {
			for (int j = 0; j < (1 << i); ++ j) {
				scanf("%d", &price[(1 << (i + 1)) - (1 << i) + j]);
			}
		}
		printf("Case #%d: %d\n", cases, dfs(1, 0));
	}
	return 0;
}
