#include <cstdio>

const int N = 64;
char map[N][N];
int r, c;

int dir[4][2] = {{0, 0}, {1, 0}, {0, 1}, {1, 1}};
char place[] = {'/', '\\', '\\', '/'};

bool chk(int x, int y) {
	if (x >= r || y >= c || map[x][y] != '#')
		return false;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int kase = 0; kase < t; ++kase) {
		scanf("%d%d", &r, &c);
		for (int i = 0; i < r; ++i)
			scanf("%s", &map[i]);
		bool res = true;
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				if (map[i][j] == '#') {
					for (int k = 0; k < 4; ++k) {
						int ni = i + dir[k][0];
						int nj = j + dir[k][1];
						if (chk(ni, nj)) {
							map[ni][nj] = place[k];
						} else {
							res = false;
							break;
						}
					}
				}
			}
		}
		printf("Case #%d:\n", kase + 1);
		if (res) {
			for (int i = 0; i < r; ++i)
				printf("%s\n", map[i]);
		} else {
			printf("Impossible\n");
		}
	}
	return 0;
}
