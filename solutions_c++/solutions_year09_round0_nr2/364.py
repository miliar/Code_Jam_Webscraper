#include <cstdio>
#include <cstring>

using namespace std;

const int inf = -1u >> 2;
const char white = (char)0, black = (char)1;

int altitude[105][105];
int nrow, ncol;
char basin[105][105], color[105][105];
char label;
int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

void dfs(int r, int c) {
	int i, j, m = inf, idx;
	for (int k = 0; k < 4; k++) {
		if ((i = r + dir[k][0]) >= 0 && i < nrow && 
			(j = c + dir[k][1]) >= 0 && j < ncol && 
			altitude[i][j] < m) {

			m = altitude[i][j];
			idx = k;
		}
	}

	if ( m < altitude[r][c]) {
		i = r + dir[idx][0], j = c + dir[idx][1];

		if (color[i][j] != white) {
			basin[r][c] = basin[i][j];
		}
		else {
			dfs(i, j);
			basin[r][c] = basin[i][j];
		}
		color[r][c] = black;
	}
	else {
		if (basin[r][c] == '\0') {
			basin[r][c] = label++;
		}
	}
}//dfs

void solve() {
	label = 'a';
	memset(color, white, sizeof(color));
	memset(basin, 0, sizeof(basin));

	for (int r = 0; r < nrow; r++) {
		for (int c = 0; c < ncol; c++) {
			if (color[r][c] == 0) {
				dfs(r, c);
			}
		}
	}

	for (int r = 0; r < nrow; r++) {
		printf("%c", basin[r][0]);
		for (int c = 1; c < ncol; c++) {
			printf(" %c", basin[r][c]);
		}
		printf("\n");
	}
}//solve

int main() {
	int nCase;

	scanf("%d", &nCase);
	for (int t = 1; t <= nCase; t++) {
		scanf("%d %d", &nrow, &ncol);

		for (int r = 0; r < nrow; r++) {
			for (int c = 0; c < ncol; c++) {
				scanf("%d", &altitude[r][c]);
			}
		}

		printf("Case #%d:\n", t);
		solve();
	}

	return 0;
}
