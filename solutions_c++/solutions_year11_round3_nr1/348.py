#include <cstdio>

using namespace std;

const int maxl = 100;

char tiles[maxl][maxl];
int R, C;

void Error() {
	printf("Impossible\n");
}

bool Check(int i, int j) {
	return i + 1 < R && j + 1 < C && tiles[i][j + 1] == '#' && tiles[i + 1][j] == '#' && tiles[i + 1][j + 1] == '#';
}

void solve() {
	scanf("%d %d", &R, &C);
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++)
			scanf(" %c", &tiles[i][j]);
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++)
			if (tiles[i][j] == '#')
				if (!Check(i, j)) {
					Error();
					return;
				} else {
					tiles[i][j] = '/';
					tiles[i][j + 1] = '\\';
					tiles[i + 1][j] = '\\';
					tiles[i + 1][j + 1] = '/';
				}
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++)
			printf("%c", tiles[i][j]);
		printf("\n");
	}
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d:\n", i);
		solve();
	}
	return 0;
}