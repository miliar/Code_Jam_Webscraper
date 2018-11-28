#include <cstdio>

int min(int x, int y) {
	return x < y ? x : y;
}

const int dr[4][2] = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};

int T, n, m, d[30][30], b[30][30], ti, tj, cd[30][30], si, sj, ans, t, qa, qb, q[900][2];
char s[30][31];
bool p[30][30];

void add(int x, int y, int v, int r) {
	if (x < 0 || n <= x || y < 0 || m <= y || d[x][y] != -1 || s[x][y] == '.')
		return;
	q[qb][0] = x;
	q[qb][1] = y;
	++qb;
	b[x][y] = r;
	d[x][y] = v;
}

void bfs(int x, int y, int v, int r) {
	d[x][y] = v;
	b[x][y] = r;
	qa = qb = 0;
	q[qb][0] = x;
	q[qb][1] = y;
	++qb;
	while (qa < qb) {
		x = q[qa][0];
		y = q[qa][1];
		v = d[x][y];
		++qa;
		for (int i = 0; i < 4; ++i)
			add(x + dr[i][0], y + dr[i][1], v + 1, i);
	}
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%s", s + i);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				d[i][j] = -1;
		bfs(0, 0, 0, -1);
		/*
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j)
				printf("%d ", d[i][j]);
			puts("");
		}
		*/
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (s[i][j] == 'T') {
					ti = i;
					tj = j;
				}
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				p[i][j] = 0;
		si = ti;
		sj = tj;
		while (b[si][sj] != -1) {
			t = b[si][sj];
			p[si][sj] = 1;
			si -= dr[t][0];
			sj -= dr[t][1];
		}
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) {
				cd[i][j] = d[i][j];
				d[i][j] = -1;
			}
		bfs(ti, tj, 0, -1);
		ans = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (s[i][j] != '.') {
					ans += p[i][j] ? (cd[i][j]) : min(cd[i][j], d[i][j]);
				}
		printf("Case #%d: %d\n", r, ans);
	}
	return 0;
}
