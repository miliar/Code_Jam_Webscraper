#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <memory.h>

const int MAXN = 110;
const int MAXM = 110;
const int MAXD = 4;

const int dx[MAXD] = {-1, 0, 0, 1};
const int dy[MAXD] = {0, -1, 1, 0};

int T = 0;
int N = 0;
int M = 0;
int m[MAXN][MAXM] = {{0}};
int rep[MAXN][MAXM] = {{0}};
int sink[MAXN * MAXM] = {0};
char ans[MAXN][MAXM] = {{0}};

void read(void) {
	scanf("%d", &T);
}

void init(void) {
	memset(sink, 0, sizeof(sink));
	for (int i = 0; i < MAXN; ++i) {
		memset(m[i], 0, sizeof(m[i]));
		memset(rep[i], 0, sizeof(rep[i]));
		memset(ans[i], 0, sizeof(ans[i]));
	}
}

void readMap(void) {
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j)
			scanf("%d", &m[i][j]);
}

bool ok(const int x, const int y) {
	return (x >= 0) && (x < N) && (y >= 0) && (y < M);
}

void DFS(int x, int y, const int r) {
	if (sink[x * M + y + 1]) {
		sink[r] = sink[x * M + y + 1];
		return;
	}
	bool flow = false;
	int fx = -1;
	int fy = -1;
	for (int i = 0; i < MAXD; ++i) {
		int xx = x + dx[i];
		int yy = y + dy[i];
		if (!ok(xx, yy) || (m[x][y] <= m[xx][yy]))
			continue;
		flow = true;
		if ((-1 == fx) || (m[xx][yy] < m[fx][fy])) {
			fx = xx;
			fy = yy;
		}
	}
	if (flow)
		DFS(fx, fy, r);
	else {
		if (!rep[x][y])
			rep[x][y] = r;
		sink[r] = x * M + y + 1;
	}
}

void solveI(void) {
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j)
			DFS(i, j, i * M + j + 1);
	char cur = 'a';
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j) {
			int x = (sink[i * M + j + 1] - 1) / M;
			int y = (sink[i * M + j + 1] - 1) % M;
			if (rep[x][y] == (i * M + j + 1))
				ans[i][j] = cur++;
			else
				ans[i][j] = ans[(rep[x][y] - 1) / M][(rep[x][y] - 1) % M];
		}
}

void printAns(const int k) {
	printf("Case #%d:\n", k);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j)
			printf("%c ", ans[i][j]);
		puts("");
	}
}

void solve(void) {
	for (int i = 0; i < T; ++i) {
		init();
		readMap();
		solveI();
		printAns(i + 1);
	}
}

int main(void) {
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	read();
	solve();
	return 0;
}
