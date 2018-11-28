#include <cstdio>

int T, n, d[120][120], ans;

int abs(int a) {
	return a < 0 ? -a : a;
}

bool neq(int a1, int b1, int a2, int b2, int a3, int b3, int a4, int b4) {
	int t1, t2, t3, t4;
	if (a1 < 0 || 2*n < a1 || b1 < 0 || 2*n < b1) t1 = -1; else t1 = d[a1][b1];
	if (a2 < 0 || 2*n < a2 || b2 < 0 || 2*n < b2) t2 = -1; else t2 = d[a2][b2];
	if (a3 < 0 || 2*n < a3 || b3 < 0 || 2*n < b3) t3 = -1; else t3 = d[a3][b3];
	if (a4 < 0 || 2*n < a4 || b4 < 0 || 2*n < b4) t4 = -1; else t4 = d[a4][b4];
	if (t1 == -1) {
		if (t2 == -1) {
			if (t3 == -1 || t4 == -1) return 0;
			else return t3 != t4;
		} else {
			if (t3 != -1 && t2 != t3) return 1;
			if (t4 != -1 && t2 != t4) return 1;
			return 0;
		}
	} else {
		if (t2 != -1 && t1 != t2) return 1;
		if (t3 != -1 && t1 != t3) return 1;
		if (t4 != -1 && t1 != t4) return 1;
		return 0;
	}
	return 0;
}

bool ok(int x, int y) {
	for (int i = 0; i <= 2*n; ++i)
		for (int j = 0; j <= 2*n; ++j)
			if (neq(x - i, y - j, x - i, y + j, x + i, y - j, x + i, y + j)) {
//				printf("%d %d not ok at %d %d\n", x, y, i, j);
				return 0;
			}
	return 1;
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d", &n);
		for (int i = 0; i <= 2*n; ++i)
			for (int j = 0; j <= 2*n; ++j) d[i][j] = -1;
		for (int i = 1; i <= n; ++i)
			for (int j = n - i + 1; j <= n + i - 1; j += 2) scanf("%d", d[i] + j);
		for (int i = n + 1; i <= 2*n - 1; ++i)
			for (int j = i - n + 1; j <= 3*n - i - 1; j += 2) scanf("%d", d[i] + j);
		ans = 10*n;
		for (int i = 0; i <= 2*n; ++i)
			for (int j = 0; j <= 2*n; ++j)
				if (abs(i - n) + abs(j - n) < ans && ok(i, j)) {
					ans = abs(i - n) + abs(j - n);
//					printf("%d %d %d\n", i, j, ans);
				}
		ans += n;
		printf("%d\n", ans*ans - n*n);
	}
	return 0;
}
