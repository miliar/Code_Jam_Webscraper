#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int cases, n;
int t;
int x1, x2, y1, y2;
int board[200][200], next[200][200];

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	scanf("%d", &cases);
	for(int i = 0; i < cases; ++i) {
		scanf("%d", &n);

		memset(board, 0, sizeof(board));
		for(int j = 0; j < n; ++j) {
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			--x1;	--y1;

			for(int j = x1; j < x2; ++j)
				for(int k = y1; k < y2; ++k)
					board[j][k] = 1;
		}
		
		for(t = 0; ; ++t) {
			memset(next, 0, sizeof(next));

			bool go = false;
			for(int j = 0; j < 200; ++j) {
				for(int k = 0; k < 200; ++k) {
					if (board[j][k] != 0) {
						go = true;
						break;
					}
				}
				if (go) break;
			}

			if (!go) break;

			for(int j = 0; j < 200; ++j) {
				for(int k = 0; k < 200; ++k) {
					if (board[j][k] == 1) {
						if (j != 0 && board[j-1][k] == 1) next[j][k] = 1;
						else if (k != 0 && board[j][k-1] == 1) next[j][k] = 1;
					}
					else {
						if (j != 0 && k != 0 && board[j-1][k] == 1 && board[j][k-1] == 1)
							next[j][k] = 1;
					}
				}
			}

			for(int j = 0; j < 200; ++j)
				for(int k = 0; k < 200; ++k)
					board[j][k] = next[j][k];
		}

		printf("Case #%d: %d\n", i + 1, t);
	}

	return 0;
}