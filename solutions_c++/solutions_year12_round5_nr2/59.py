#include <cstdio>
#include <queue>
using namespace std;

const int MAXN = 100;
const int DX[6] = {-1, 0, 1, 1, 0, -1};
const int DY[6] = {0, 1, 1, 0, -1, -1};

int S, Q, bc[MAXN][MAXN], cc[MAXN][MAXN], edge[MAXN][MAXN];
bool mat[MAXN][MAXN], corner[MAXN][MAXN], inner[MAXN][MAXN], tag[MAXN][MAXN], visited[MAXN][MAXN];

void init() {
	memset(mat, 0, sizeof(mat));
	memset(edge, 0, sizeof(edge));
	memset(corner, 0, sizeof(corner));
	memset(inner, 0, sizeof(inner));
	memset(tag, 0, sizeof(tag));
	for (int i = 1; i <= S; i++) {
		for (int j = 1; j < S + i; j++) {
			mat[i][j] = true;
		}
	}
	for (int i = 1; i <= S; i++) {
		for (int j = 1; j < S + i; j++) {
			mat[(S << 1) - i][S - i + j] = true;
		}
	}
	for (int i = 1; i <= S << 1; i++) {
		for (int j = 1; j <= S << 1; j++) {
			int cnt = 0;
			for (int dir = 0; dir < 6; dir++) {
				cnt += mat[i + DX[dir]][j + DY[dir]];
			}
			if (cnt == 6) {
				inner[i][j] = true;
			} else if (cnt == 4) {
				if (i == 1) edge[i][j] = 1;
				else if (j == 1) edge[i][j] = 2;
				else if (i == (S << 1) - 1) edge[i][j] = 3;
				else if (j == (S << 1) - 1) edge[i][j] = 4;
				else if (i < j) edge[i][j] = 5;
				else edge[i][j] = 6;
			} else if (cnt == 3) {
				corner[i][j] = true;
			}
		}
	}
}

void bfs(int x, int y) {
	memset(visited, 0, sizeof(visited));
	queue < pair <int, int> > q;
	visited[x][y] = true;
	for (q.push(make_pair(x, y)); !q.empty(); q.pop()) {
		int x = q.front().first, y = q.front().second;
		for (int dir = 0; dir < 6; dir++) {
			if (tag[x + DX[dir]][y + DY[dir]] && !visited[x + DX[dir]][y + DY[dir]]) {
				visited[x + DX[dir]][y + DY[dir]] = true;
				q.push(make_pair(x + DX[dir], y + DY[dir]));
			}
		}
	}
}

void floodfill() {
	memset(bc, 0, sizeof(bc));
	memset(cc, 0, sizeof(cc));
	for (int o = 1; o <= 6; o++) {
		memset(visited, 0, sizeof(visited));
		queue < pair <int, int> > q;
		for (int i = 1; i <= S << 1; i++) {
			for (int j = 1; j <= S << 1; j++) {
				if (edge[i][j] == o && tag[i][j]) {
					q.push(make_pair(i, j));
					visited[i][j] = true;
				}
			}
		}
		for ( ; !q.empty(); q.pop()) {
			int x = q.front().first, y = q.front().second;
			for (int dir = 0; dir < 6; dir++) {
				if (tag[x + DX[dir]][y + DY[dir]] && !visited[x + DX[dir]][y + DY[dir]]) {
					visited[x + DX[dir]][y + DY[dir]] = true;
					q.push(make_pair(x + DX[dir], y + DY[dir]));
				}
			}
		}
		for (int x = 1; x <= S << 1; x++) {
			for (int y = 1; y <= S << 1; y++) {
				if (visited[x][y]) {
					bc[x][y]++;
				}
			}
		}
	}
	for (int i = 1; i <= S << 1; i++) {
		for (int j = 1; j <= S << 1; j++) {
			if (!tag[i][j]) continue;
			if (corner[i][j]) {
				bfs(i, j);
				for (int x = 1; x <= S << 1; x++) {
					for (int y = 1; y <= S << 1; y++) {
						if (visited[x][y]) {
							cc[x][y]++;
						}
					}
				}
			}
		}
	}
}

bool isBridge() {
	for (int i = 1; i <= S << 1; i++) {
		for (int j = 1; j <= S << 1; j++) {
			if (cc[i][j] >= 2) return true;
		}
	}
	return false;
}

bool isFork() {
	for (int i = 1; i <= S << 1; i++) {
		for (int j = 1; j <= S << 1; j++) {
			if (bc[i][j] >= 3) return true;
		}
	}
	return false;
}

bool isRing() {
	memset(visited, 0, sizeof(visited));
	for (int x = 1; x <= S << 1; x++) {
		for (int y = 1; y <= S << 1; y++) {
			if (visited[x][y] || tag[x][y] || !mat[x][y]) continue;
			queue < pair <int, int> > q;
			visited[x][y] = true;
			bool outside = false;
			for (q.push(make_pair(x, y)); !q.empty(); q.pop()) {
				int x = q.front().first, y = q.front().second;
				for (int dir = 0; dir < 6; dir++) {
					if (!mat[x + DX[dir]][y + DY[dir]]) {
						outside = true;
						continue;
					}
					if (!tag[x + DX[dir]][y + DY[dir]] && !visited[x + DX[dir]][y + DY[dir]]) {
						visited[x + DX[dir]][y + DY[dir]] = true;
						q.push(make_pair(x + DX[dir], y + DY[dir]));
					}
				}
			}
			if (!outside) {
				return true;
			}
		}
	}
	return false;
}

int main() {
	int taskNumber;
	scanf("%d", &taskNumber);
	for (int taskIdx = 0; taskIdx < taskNumber; taskIdx++) {
		scanf("%d%d", &S, &Q);
		init();
		bool finished = false;
		printf("Case #%d: ", taskIdx + 1);
		for (int i = 1; i <= Q; i++) {
			int x, y;
			scanf("%d%d", &x, &y);
			if (finished) continue;
			tag[x][y] = true;
			floodfill();
			bool bridge = isBridge();
			bool fork = isFork();
			bool ring = isRing();
			finished = bridge || fork || ring;
			if (bridge && !fork && !ring) {
				printf("bridge in move %d\n", i);
			}
			if (!bridge && fork && !ring) {
				printf("fork in move %d\n", i);
			}
			if (!bridge && !fork && ring) {
				printf("ring in move %d\n", i);
			}
			if (bridge && fork && !ring) {
				printf("bridge-fork in move %d\n", i);
			}
			if (bridge && !fork && ring) {
				printf("bridge-ring in move %d\n", i);
			}
			if (!bridge && fork && ring) {
				printf("fork-ring in move %d\n", i);
			}
			if (bridge && fork && ring) {
				printf("bridge-fork-ring in move %d\n", i);
			}
		}
		if (!finished) puts("none");
	}
	return 0;
}
