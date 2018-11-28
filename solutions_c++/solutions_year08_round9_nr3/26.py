#include <cstdio>

int T, R, C, m[7][7], ans;
bool v[7][7];

bool ch(int x, int y) {
	if (x < 2 || y < 2)
		return 1;
	int t = 0;
	for (int i = x - 2; i <= x; ++i)
		for (int j = y - 2; j <= y; ++j)
			t += v[i][j];
	return t == m[x - 1][y - 1];
}

void dfs(int x, int y) {
//	printf("dfs %d %d\n", x, y);
	if (y == C + 1) {
		dfs(x + 1, 1);
		return;
	}
	if (x == R + 1) {
		for (int i = 1; i <= R; ++i)
			for (int j = 1; j <= C; ++j)
				if (!ch(i + 1, j + 1))
					return;
		/*
		for (int i = 1; i <= R; ++i) {
			for (int j = 1; j <= C; ++j)
				printf("%d", v[i][j]);
			puts("");
		}
		puts("");
		*/
		int t = 0;
		for (int j = 1; j <= C; ++j)
			t += v[R + 1 >> 1][j];
		if (ans < t)
			ans = t;
		return;
	}
	v[x][y] = 0;
	if (ch(x, y))
		dfs(x, y + 1);
	v[x][y] = 1;
	if (ch(x, y))
		dfs(x, y + 1);
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		scanf("%d%d", &R, &C);
		for (int i = 1; i <= R; ++i)
			for (int j = 1; j <= C; ++j)
				scanf("%d", m[i] + j);
		for (int i = 0; i <= R + 1; ++i)
			for (int j = 0; j <= C + 1; ++j)
				v[i][j] = 0;
		ans = 0;
		dfs(1, 1);
		printf("Case #%d: %d\n", r, ans);
	}
	return 0;
}
