#include <cstdio>

int T, n, m, cnt;
char s[8][8];
bool b[8][8], v[8][8];

void f(int &x, int &y) {
	int i = x, j = y;
	if (s[i][j] == '-') {
		if (b[i][j]) y = (y + 1)%m;
		else y = (y + m - 1)%m;
	} else if (s[i][j] == '|') {
		if (b[i][j]) x = (x + 1)%n;
		else x = (x + n - 1)%n;
	} else if (s[i][j] == '/') {
		if (b[i][j]) x = (x + 1)%n, y = (y + m - 1)%m;
		else x = (x + n - 1)%n, y = (y + 1)%m;
	} else {
		if (b[i][j]) x = (x + 1)%n, y = (y + 1)%m;
		else x = (x + n - 1)%n, y = (y + m - 1)%m;
	}
}

bool check() {
	int x, y;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			v[i][j] = 0;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j) if (!v[i][j]) {
			x = i, y = j;
			while (!v[x][y]) {
				v[x][y] = 1;
				f(x, y);
			}
			if (x != i || y != j)
				return 0;
		}
	return 1;
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d:", r);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%s", s[i]);
		cnt = 0;
		for (int i = 0; i < 1 << (n*m); ++i) {
			for (int ii = 0; ii < n; ++ii)
				for (int jj = 0; jj < m; ++jj)
					b[ii][jj] = (i >> (ii*m + jj))&1;
			cnt += check();
		}
		printf(" %d\n", cnt);
	}
	return 0;
}
