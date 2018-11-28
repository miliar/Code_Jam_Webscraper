#include <cstdio>
#include <algorithm>

using namespace std;

char board[10][10];
int dx[] = {-1, -1, 0, 1};
int dy[] = {0, -1, -1, -1};

void solve() {
	int d[10][10][4][2] = {0};
	int flag = 1;
	for (int i = 1; i <= 4; ++i) {
		for (int j = 1; j <= 4; ++j) {
			for (int dir = 0; dir < 4; ++dir) {
				if (board[i][j] == 'T' || board[i][j] == 'X') {
					d[i][j][dir][0] = d[i + dy[dir]][j + dx[dir]][dir][0] + 1;
				}
				if (board[i][j] == 'T' || board[i][j] == 'O') {
					d[i][j][dir][1] = d[i + dy[dir]][j + dx[dir]][dir][1] + 1;
				}
				if (d[i][j][dir][0] == 4 || d[i][j][dir][1] == 4) {
					printf("%c won\n", d[i][j][dir][0] == 4 ? 'X' : 'O');
					return;
				}
			}
			if (board[i][j] == '.') flag = 0;
		}
	}
	if (flag) printf("Draw\n");
	else {
		printf("Game has not completed\n");
	}
}

int main() {
	int r;
	scanf("%d", &r);
	for (int cs = 1; cs <= r; ++cs) {
		printf("Case #%d: ", cs);
		for (int i = 1; i <= 4; ++i) scanf("%s", board[i] + 1);
		solve();
	}
	return 0;
}
