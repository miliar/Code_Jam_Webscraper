#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MaxN = 105;
const int MaxM = MaxN * MaxN;
const double eps = 1e-8;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

int H, R, C;
int c[MaxN][MaxN], f[MaxN][MaxN];
double DP[MaxN][MaxN];

int sgn(double x) {
	return x < -eps ? -1 : x > eps;
}

struct Node {
	int x, y;
	Node() {}
	Node(int x, int y) : x(x), y(y) {}
} q[MaxM], *pF, *pB;
bool vst[MaxN][MaxN];

bool in(int x, int y) {
	if (x < 0 || x >= R) return false;
	if (y < 0 || y >= C) return false;
	if (c[x][y] - f[x][y] < 50) return false;
	return true;
}

void BFS() {
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++) {
			DP[i][j] = 1e100;
			vst[i][j] = false;
		}
	pF = pB = q;
	DP[0][0] = 0.0;
	*pB++ = Node(0, 0);
	vst[0][0] = true;
	while (pF != pB) {
		// printf("(%d, %d)\n", pF->x, pF->y);
		for (int i = 0; i < 4; i++) {
			*pB = Node(pF->x + dx[i], pF->y + dy[i]);
			if (in(pB->x, pB->y)) {
				if (vst[pB->x][pB->y]) continue;
				if (c[pB->x][pB->y] - f[pF->x][pF->y] < 50) continue;
				if (c[pF->x][pF->y] - f[pB->x][pB->y] < 50) continue;
				if (sgn(c[pB->x][pB->y] - H - 50.0) >= 0) {
					DP[pB->x][pB->y] = 0.0;
					vst[pB->x][pB->y] = true;
					pB++;
				}
			}
		}
		pF++;
	}
}

double sol() {
	pF = pB = q;
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++)
			if (DP[i][j] < 1e100) {
				*pB++ = Node(i, j);
				vst[i][j] = true;
			} else {
				vst[i][j] = false;
			}
	
	while (pF != pB) {
		vst[pF->x][pF->y] = false;
		// printf("(%d, %d) %.2f\n", pF->x, pF->y, DP[pF->x][pF->y]);
		for (int i = 0; i < 4; i++) {
			*pB = Node(pF->x + dx[i], pF->y + dy[i]);
			if (in(pB->x, pB->y)) {
				if (c[pB->x][pB->y] - f[pF->x][pF->y] < 50) continue;
				if (c[pF->x][pF->y] - f[pB->x][pB->y] < 50) continue;
				double& ref = DP[pB->x][pB->y];
				double next = DP[pF->x][pF->y];
				if (sgn(c[pB->x][pB->y] - (H - next * 10.0) - 50.0) < 0) {
					next = (H - (c[pB->x][pB->y] - 50.0)) / 10.0;
				}
				// printf("next = %.2f\n", next);
				if (sgn(H - next * 10.0 - f[pF->x][pF->y] - 20.0) >= 0) {
					next += 1.0;
				} else {
					next += 10.0;
				}
				if (ref > next) {
					ref = next;
					if (!vst[pB->x][pB->y]) {
						vst[pB->x][pB->y] = true;
						pB++;
						if (pB == q + MaxM) pB = q;
					}
				}
			}
		}
		*pF++;
		if (pF == q + MaxM) pF = q;
	}	
	
	return DP[R - 1][C - 1];
}

int main() {
	int T;
	int cas = 1;
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", cas++);
		scanf("%d%d%d", &H, &R, &C);
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				scanf("%d", &c[i][j]);
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				scanf("%d", &f[i][j]);
		BFS();
		printf("%.12f\n", sol());
	}
	
	return 0;
}

