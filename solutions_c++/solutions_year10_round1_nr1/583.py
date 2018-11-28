#include <cstdio>

#define MAX 55

int n, k;
char grid[MAX][MAX];
char grid2[MAX][MAX];
int numInRow[MAX];

void wipe() {
	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) {
			grid[i][j] = grid2[i][j] = 0;
		}
		numInRow[i] = 0;
	}
}

char dx[] = {0, 1, 0, -1, 1, 1, -1, -1};
char dy[] = {1, 0, -1, 0, -1, 1, 1, -1};

bool valid(int x, int y) {
	if (x < 0 || y < 0) return false;
	if (x >= n && y >= n) return false;
	return true;
}

bool check(int r, int c, char find) {
	for (int i = 0; i < 8; i++) {
		bool bad = false;
		for (int j = 0; j < k && !bad; j++) {
			int nx = r + dx[i] * j;
			int ny = c + dy[i] * j;

			if (valid(nx, ny)) {
				if (grid2[nx][ny] != find) bad = true;
			} else bad = true;
		}
		if (!bad) return true;
	}
	return false;
}

void solve() {
	wipe();
	scanf("%d %d ", &n, &k);
	for (int i = 0; i < n; i++) {
		scanf("%s ", grid[i]);
	}

	for (int i = n - 1; i >= 0; i--) { //for each row backwards
		int row = (n - 1) - i;
		for (int j = n - 1; j >= 0; j--) { //for each col backwards
			int col = (n - 1) - j;
			if (grid[i][j] != '.') {
				grid2[row][numInRow[row]++] = grid[i][j];
			}
		}
		for (int j = numInRow[row]; j < n; j++) {
			grid2[row][j] = '.';
		}
	}

	bool red = false;
	bool blue = false;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (check(i, j, 'R')) red = true;
			if (check(i, j, 'B')) blue = true;
		}
	}

	if (!red && !blue) printf("Neither");
	else if (red && !blue) printf("Red");
	else if (!red && blue) printf("Blue");
	else if (red && blue) printf("Both");
}

int main() {
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
	}

	return 0;
}
