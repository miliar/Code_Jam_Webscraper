#include <cstdlib>
#include <cstdio>
#include <memory.h>

int H, W;
int M[101][101];
char A[101][101];

int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};

void climb(int y, int x, int mark)
{
	if (y < 0 || y >= H || x < 0 || x >= W) return;
	if (A[y][x] != 0) return;
	A[y][x] = mark + 'a';

	for (int k = 0; k < 4; k++) {
		int py = y + dy[k];
		int px = x + dx[k];
		
		if (py < 0 || py >= H || px < 0 || px >= W || A[py][px] != 0) continue;
		if (M[y][x] >= M[py][px]) continue;

		int maxA = 1000000;
		int nny = -1, nnx = -1;
		for (int kk = 0; kk < 4; kk++) {
			int ny = py + dy[kk];
			int nx = px + dx[kk];
			if (ny < 0 || ny >= H || nx < 0 || nx >= W) continue;
			if (M[ny][nx] < maxA) {
				maxA = M[ny][nx];
				nny = ny;
				nnx = nx;
			}
		}
		if (nny == y && nnx == x) climb(py, px, mark);
	}
}
int fy, fx;
void flow(int y, int x)
{
	if (y < 0 || y >= H || x < 0 || x >= W) return;
	if (A[y][x] != 0) return;
	
	int maxA = M[y][x];
	bool ok = false;
	for (int k = 0; k < 4; k++) {
		int ny = y + dy[k];
		int nx = x + dx[k];
		if (ny < 0 || ny >= H || nx < 0 || nx >= W) continue;
		if (M[ny][nx] < maxA) {
			maxA = M[ny][nx];
			fy = ny;
			fx = nx;
			ok = true;
		}
	}
	if (ok) flow(fy, fx);
}
void solve(int y, int x, int mark)
{
	fy = y;
	fx = x;
	flow(y, x);
	climb(fy, fx, mark);	
}


int main()
{
	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++) {
		scanf("%d%d", &H, &W);
		memset(&M, 0x00, sizeof(H));
		memset(&A, 0x00, sizeof(A));
		int mark = 0;
		for (int i = 0; i < H; i++) for (int j =0; j < W; j++) scanf("%d", &M[i][j]);
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (A[i][j] == 0) solve(i, j, mark++);
			}
		}
		printf("Case #%d:\n", t);
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (j) printf(" ");
				printf("%c", A[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
