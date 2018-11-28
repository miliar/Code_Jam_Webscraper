#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

char g[5][5];
int dx[4] = {1, 0, 1, 1}, dy[4] = {0, 1, 1, -1};

bool check(char c) {
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j) if (g[i][j] == c || g[i][j] == 'T')
			for (int a = 0; a < 4; ++a) {
				bool flag = true;
				for (int k = 1; k < 4; ++k) {
					int x = i + dx[a] * k, y = j + dy[a] * k;
					if (x < 0 || x >= 4 || y < 0 || y >= 4 || g[x][y] != 'T' && g[x][y] != c) {
						flag = false; break;
					}
				}
				if (flag) return true;
			}
	return false;
}

void work() {
	for (int i = 0; i < 4; ++i)
		scanf("%s", g[i]);

	if (check('X')) {
		puts("X won"); return ;
	}
	if (check('O')) {
		puts("O won"); return ;
	}
	int cnt = 0;
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (g[i][j] == '.') cnt++;
	if (cnt) puts("Game has not completed");
	else puts("Draw");
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		work();
	}

	return 0;
}
