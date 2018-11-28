#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

typedef pair <int, int> PII;

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

const int MAXN = 110;

int R, C, room[MAXN][MAXN], dir[MAXN][MAXN], ht[MAXN][MAXN];
char cor[MAXN];

inline bool isValid(int x, int y) {
	return 0 <= x && x < R && 0 <= y && y < C;
}

PII bfs[MAXN * MAXN];

inline void BFS(int room0, int x, int y) {
	int head = 0, tail = 0;
	bfs[tail++] = make_pair(x, y);
	while (head < tail) {
		PII pii = bfs[head++];
		int x = pii.first, y = pii.second;
		room[x][y] = room0;
		for (int i = 0; i < 4; i++) {
			int xx = x + dx[i], yy = y + dy[i];
			if (!isValid(xx, yy) || dir[xx][yy] == 5) continue;
			if (x == xx + dx[dir[xx][yy]] && y == yy + dy[dir[xx][yy]]) bfs[tail++] = make_pair(xx, yy);
		}
	}
}

int main() {
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				memset(room[i], 0xFF, sizeof(int) * C);
				scanf("%d", &ht[i][j]);
			}
		}
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				int lowest = ht[i][j];
				dir[i][j] = 5;
				for (int k = 0; k < 4; k++) {
					int x = i + dx[k], y = j + dy[k];
					if (!isValid(x, y) || ht[x][y] >= lowest) continue;
					lowest = ht[x][y];
					dir[i][j] = k;
				}
			}
		}
		int room0 = 0;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (dir[i][j] == 5) BFS(room0++, i, j);
			}
		}
		printf("Case #%d:\n", oo + 1);
		memset(cor, 0, sizeof(cor));
		char markch = 'a';
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (!cor[room[i][j]]) cor[room[i][j]] = markch++;
			}
		}
		for (int i = 0; i < R; i++) {
			putchar(cor[room[i][0]]);
			for (int j = 1; j < C; j++) {
				putchar(' ');
				putchar(cor[room[i][j]]);
			}
			putchar('\n');
		}
/*		for (int i = 0; i < R; i++) {
			printf("%d", room[i][0]);
			for (int j = 1; j < C; j++) printf(" %d", room[i][j]);
			putchar('\n');
		}*/
	}
	return 0;
}
