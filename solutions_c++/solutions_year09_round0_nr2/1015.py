#include <cstdio>
#include <cstring>

using namespace std;

const int di[4] = {-1, 0, 0, 1};
const int dj[4] = {0, -1, 1, 0};

int n, m;
int g[100][100];
char res[101][101];

char dfs (int i, int j, char c) {
	if (res[i][j]) return res[i][j];
	int cur = g[i][j];
	int ii = i, jj = j;
	for (int k = 0; k < 4; k++) {
		int ni = i + di[k];
		int nj = j + dj[k];
		if (ni >= 0 && ni < n && nj >= 0 && nj < m && g[ni][nj] < cur) {
			cur = g[ni][nj];
			ii = ni;
			jj = nj;
		}
	}
	if (cur != g[i][j]) c = dfs (ii, jj, c);
	res[i][j] = c;
	return c;
}

int main () {
	int tt;
	scanf ("%d", &tt);
	for (int it = 1; it <= tt; it++) {
		scanf ("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				scanf ("%d", &g[i][j]);
		memset (res, 0, sizeof (res));
		char cur = 'a';
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (!res[i][j])
					if (dfs (i, j, cur) == cur) cur++;
		printf ("Case #%d:\n", it);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (j != 0) printf (" ");
				printf ("%c", res[i][j]);
			}
		        printf ("\n");
		}
	}
}