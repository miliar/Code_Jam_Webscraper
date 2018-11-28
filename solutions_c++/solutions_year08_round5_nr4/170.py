#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

long F[110][110];
int ok[110][110];
int H, W;

int getF(int r, int c) {
	if (r < 1 || c < 1 || r > H || c > W) return 0;
	if (!ok[r][c]) return 0;
	return F[r][c];
}

int doit() {
	int R;
	cin >> H >> W >> R;
	for (int i = 0; i < 110; i++) {
		for (int j = 0; j < 110; j++) {
			F[i][j] = 1;
			ok[i][j] = 0;
		}
	}
	ok[1][1] = 1;
	for (int i = 0; i < R; i++) {
		int a, b;
		cin >> a >> b;
		F[a][b] = 0;
	}
	for (int d = 1; d < 110; d++) {
		for (int k = 0; k <= d; k++) {
			int r = d * 2 + 1 - k;
			int c = d + 1 + k;
			if (r > H || c > W || r < 0 || c < 0) {
				continue;
			}
			F[r][c] = (F[r][c] * (getF(r - 2, c - 1) + getF(r - 1, c - 2))) % 10007;
			ok[r][c] = 1;
		}
	}
	if (!ok[H][W]) return 0;
	return F[H][W];
}

int main() {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		int res = doit();
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}
