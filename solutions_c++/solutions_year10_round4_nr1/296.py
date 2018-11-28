#include <cstdio>
#include <algorithm>

using namespace std;

int cases, n;
char board[110][110];
char temp[110];
int cost;

bool Compare(char c1, char c2) {
	if (c1 == ' ' || c2 == ' ') return true;
	return c1 == c2;
}

int main() {

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &cases);
	for(int i = 0; i < cases; ++i) {
		scanf("%d", &n);
		gets(temp);

		memset(board, 0, sizeof(board));
		for(int j = 0; j < 2 * n - 1; ++j)
			gets(board[j]);

		for(int j = 0; j < 2 * n - 1; ++j) {
			for(int k = 0; k < 2 * n - 1; ++k) {
				if (board[j][k] >= '0' && board[j][k] <= '9') continue;
				board[j][k] = ' ';
			}
		}

		cost = 987654321;
		for(int p = 0; p < 2 * n - 1; ++p) {
			for(int q = 0; q < 2 * n - 1; ++q) {

				bool symmetry = true;
				for(int j = 0; j < 2 * n - 1; ++j) {
					for(int k = 0; k < 2 * n - 1; ++k) {
						int x = 2 * p - j;
						int y = 2 * q - k;

						if (board[j][k] < '0' || board[j][k] > '9') continue;

						if (x >= 0 && x < 2 * n - 1 && !Compare(board[x][k], board[j][k])) {
							symmetry = false;
							break;
						}

						if (y >= 0 && y < 2 * n - 1 && !Compare(board[j][y], board[j][k])) {
							symmetry = false;
							break;
						}

						if (x >= 0 && x < 2 * n - 1 && y >= 0 && y < 2 * n - 1 && !Compare(board[x][y], board[j][k])) {
							symmetry = false;
							break;
						}
					}
					if (!symmetry) break;
				}

				if (symmetry) {
					int dist = 0;
					for(int j = 0; j < 2 * n - 1; ++j) {
						for(int k = 0; k < 2 * n - 1; ++k) {
							if (board[j][k] >= '0' && board[j][k] <= '9')
								dist = max(dist, abs(j - p) + abs(k - q) + 1);
						}
					}

					cost = min(cost, dist * dist - n * n);
				}
			}
		}

		printf("Case #%d: %d\n", i + 1, cost);
	}

	return 0;
}