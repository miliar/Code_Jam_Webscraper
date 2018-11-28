#include <cstdio>
#include <queue>

const int MAXN = 110;
const int BUTTONS = 100;
const int INF = 1000000000;

using namespace std;

struct Entry {
	int i, x, y;

	Entry() {}
	Entry(int i, int x, int y) {
		this->i = i;
		this->x = x;
		this->y = y;
	}
};

int n, tests;
char type[MAXN]; int position[MAXN];
int minMoves[MAXN][MAXN][MAXN];
queue <Entry> q;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d ", &tests);
	for (int t = 1; t <= tests; ++t) {
		scanf("%d ", &n);
		for (int i = 1; i <= n; ++i)
			scanf("%c %d ", &type[i], &position[i]);

		for (int i = 0; i <= n; ++i)
			for (int j = 1; j <= BUTTONS; ++j)
				for (int k = 1; k <= BUTTONS; ++k)
					minMoves[i][j][k] = INF;

		q.push(Entry(0, 1, 1));
		minMoves[0][1][1] = 0;
		while (!q.empty()) {
			Entry top = q.front();
			q.pop();

			for (int i = -1; i <= 1; ++i)
				for (int j = -1; j <= 1; ++j) {
					int posX = top.x + i;
					int posY = top.y + j;
					int posI = top.i;

					if (posX > 0 && posX <= BUTTONS && posY > 0 && posY <= BUTTONS) {
						if (i == 0 && top.i <= n && type[top.i+1] == 'O' && posX == position[top.i+1])
							++posI;
						if (j == 0 && top.i <= n && type[top.i+1] == 'B' && posY == position[top.i+1])
							++posI;

						if (minMoves[top.i][top.x][top.y] + 1 < minMoves[posI][posX][posY]) {
							minMoves[posI][posX][posY] = minMoves[top.i][top.x][top.y] + 1;
							q.push(Entry(posI, posX, posY));
						}
					}
				}
		}

		int sol = INF;
		for (int i = 1; i <= BUTTONS; ++i)
			for (int j = 1; j <= BUTTONS; ++j)
				sol = min(sol, minMoves[n][i][j]);
		printf("Case #%d: %d\n", t, sol);
	}

	return 0;
}
