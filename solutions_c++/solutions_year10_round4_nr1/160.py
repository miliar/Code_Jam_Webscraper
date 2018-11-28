#include <iostream>
using namespace std;

const int maxn = 200 + 10;

int tcase, n, len, s[maxn][maxn], t[maxn][maxn];

void init() {
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i)
		for (int j = 1, k = i; j <= i; ++j, --k)
			scanf("%d", &s[k][j]);
	for (int i = 2; i <= n; ++i)
		for (int j = i, k = n; j <= n; ++j, --k)
			scanf("%d", &s[k][j]);
}

bool same(int &a, int &b) {
	if (a == -1 || b == -1) return 1;
	return a == b;
}

bool check(int sx, int sy) {
	memset(t, -1, sizeof(t));
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j)
			t[sx + i - 1][sy + j - 1] = s[i][j];

	for (int i = 1; i <= len; ++i)
		for (int x1 = i, y1 = 1, x2 = 1, y2 = i; x1 > x2; --x1, ++y1, ++x2, --y2)
			if (!same(t[x1][y1], t[x2][y2])) return 0;
	for (int i = 1; i <= len; ++i)
		for (int x1 = len, y1 = i, x2 = i, y2 = len; x1 > x2; --x1, ++y1, ++x2, --y2)
			if (!same(t[x1][y1], t[x2][y2])) return 0;

	for (int i = 1; i <= len; ++i)
		for (int x1 = len, y1 = i, x2 = len - i + 1, y2 = 1; x1 > x2; --x1, --y1, ++x2, ++y2)
			if (!same(t[x1][y1], t[x2][y2])) return 0;
	for (int i = 1; i <= len; ++i)
		for (int x1 = len - i + 1, y1 = len, x2 = 1, y2 = i; x1 > x2; --x1, --y1, ++x2, ++y2)
			if (!same(t[x1][y1], t[x2][y2])) return 0;

	return 1;
}

int solve() {
	int res;
	for (len = n; ; ++len)
		for (int i = 1; i + n - 1 <= len; ++i) {
			res = len * len - n * n;
			if (check(i, 1)) return res;
			if (check(1, i)) return res;
			if (check(i, len - n + 1)) return res;
			if (check(len - n + 1, i)) return res;
		}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcase);
	for (int c = 1; c <= tcase; ++c) {
		init();
		printf("Case #%d: %d\n", c, solve());
	}
	return 0;
}
