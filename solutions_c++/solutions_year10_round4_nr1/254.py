#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;

int tests, n, ans;
int a[202][202];

inline int min(int a, int b) { return a > b ? b : a; }
inline int max(int a, int b) { return a > b ? a : b; }
inline int sqr(int a) { return a * a; }
inline int abs(int a) { return a > 0 ? a : -a; }
bool inrange(int x, int y) {
	if (1 <= x && x <= 2 * n - 1 && 1 + abs(x - n) <= y && y <= 2 * n - 1 - abs(x - n)) return true;
	else return false;
}
int get(int x, int y) {
	int ret = 0;
	for (int i = 1; i <= 2 * n - 1; ++ i)
		for (int j = 1 + abs(i - n); j <= 2 * n - 1 - abs(i - n); ++ j) {
			ret = max(ret, abs(i - x) + abs(j - y) + 1);
			if (inrange(x + x - i, j) && a[i][j] != a[x + x - i][j]) return 0x3FFFFFFF;
			if (inrange(i, y + y - j) && a[i][j] != a[i][y + y - j]) return 0x3FFFFFFF;
		}
	return ret;
}
int main(int argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tests);
	for (int cases = 1; cases <= tests; ++ cases) {
		scanf("%d", &n);
		for (int i = 1; i <= 2 * n - 1; ++ i)
			for(int j = 1 + abs(i - n); j <= 2 * n - 1 - abs(i - n); ++ j, ++ j)
				scanf("%d", &a[i][j]);
		int ans = 0x3FFFFFFF;
		for(int i = 1; i <= 2 * n - 1; ++ i)
			for(int j = 1; j <= 2 * n - 1; ++ j)
				ans = min(ans, get(i, j));
		printf("Case #%d: %d\n", cases, sqr(ans) - sqr(n));
	}
	return 0;
}
