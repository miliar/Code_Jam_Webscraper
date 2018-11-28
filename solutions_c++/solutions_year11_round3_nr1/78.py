#include <cstdio>

using namespace std;

char tile[100][100];
int R, C;

void solvefor() {
	for(int i = 0; i < R - 1; ++i) {
		for(int j = 0; j < C - 1; ++j) {
			if (tile[i][j] == '#' && tile[i][j+1] == '#' && tile[i+1][j] == '#' && tile[i+1][j+1] == '#') {
				tile[i][j] = '/';
				tile[i][j+1] = '\\';
				tile[i+1][j] = '\\';
				tile[i+1][j+1] = '/';
			}
		}
	}

	for(int i = 0; i < R; ++i) {
		for(int j = 0; j < C; ++j) {
			if (tile[i][j] == '#') {
				printf("Impossible\n");
				return;
			}
		}
	}

	for(int i = 0; i < R; ++i)
		printf("%s\n", tile[i]);
}

void solve() {
	scanf("%d%d", &R, &C);

	for(int i = 0; i < R; ++i) {
		scanf("%s", tile[i]);
	}

	solvefor();
}

int main() {
	freopen("C:\\Users\\kiheon\\Downloads\\A-large.in", "r", stdin);
	freopen("C:\\workspace\\GCJ\\output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i) {
		printf("Case #%d:\n", i);
		solve();
	}

	return 0;
}
