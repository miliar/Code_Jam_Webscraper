#include <cstdio>
#include <vector>
using namespace std;

const int NMAX = 105;

int mat[NMAX][NMAX];
char f[NMAX][NMAX];

int m, n;

int dy[4] = {-1, 0, 0, 1};
int dx[4] = {0,-1, 1, 0};

pair<int,int> flows(int y, int x) {
	pair<int, int>sol = make_pair(-1, -1);
	for (int i = 0; i < 4; ++i) {
		int yy = y + dy[i];
		int xx = x + dx[i];

		if (yy >= 0 && xx >= 0 && yy < m && xx < n && mat[yy][xx] < mat[y][x]) {
			if (sol.first == -1 || mat[yy][xx] < mat[sol.first][sol.second])
				sol = make_pair(yy, xx);
		}
	}
	return sol;
}

void fill(int y, int x, char c) {
	if (f[y][x] != 0) return;
	if (y < 0 || x < 0 || y >= m || x >= n)
		return;
	f[y][x] = c;
	pair<int, int> w = flows(y, x);
	if (w.first != -1) fill(w.first, w.second, c);
	for (int i = 0; i < 4; ++i) {
		int yy = y + dy[i];
		int xx = x + dx[i];
		if (yy >= 0 && xx >= 0 && yy < m && xx < n) {
			w = flows(yy, xx);
			if (w.first == y && w.second == x)
				fill(yy, xx, c);
		}
	}
}

int main() {
	FILE* fin = fopen("input.txt", "r");
	FILE* fout = fopen("output.txt", "w");
	int t;
	fscanf (fin, "%d", &t);
	for (int nt = 1; nt <= t; ++nt) {
		fscanf (fin, "%d%d", &m, &n);
		for (int i = 0; i < m; ++i)
			for (int j = 0; j < n; ++j)
				fscanf (fin, "%d", &mat[i][j]);
		memset(f, 0, sizeof(f));
		char c = 'a';
		for (int i = 0; i < m; ++i)
			for (int j = 0; j < n; ++j)
				if (0 == f[i][j])
					fill(i, j, c++);
		fprintf (fout, "Case #%d:\n", nt);
		for (int i = 0; i < m; ++i) {
			fprintf (fout, "%c", f[i][0]);
			for (int j = 1; j < n; ++j)
				fprintf (fout, " %c", f[i][j]);
			fprintf (fout, "\n");
		}
	}
	return 0;
}