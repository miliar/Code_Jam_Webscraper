#include <cstdio>

const int di[4][2] = {0, 1, 1, 1, 1, 0, 1, -1};

int T, n, k, t;
char s[100][100], b[100][100];
bool R, B;

bool ib(int x, int y) {
	return 0 <= x && x < n && 0 <= y && y < n && b[x][y] == 'B';
}

bool ir(int x, int y) {
	return 0 <= x && x < n && 0 <= y && y < n && b[x][y] == 'R';
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; ++i)
			scanf("%s", s[i]);
		for (int i = 0; i < n; ++i) {
			t = 0;
			for (int j = 0; j < n; ++j) if (s[i][j] != '.')
				b[i][t] = s[i][j], ++t;
			for (int j = t - 1; 0 <= j; --j)
				b[i][n - t + j] = b[i][j];
			for (int j = 0; j < n - t; ++j)
				b[i][j]= '.';
		}
		R = B = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j) {
				if (ib(i, j) && !B)
					for (int p = 0; p < 4 && !B; ++p) {
						B = 1;
						for (int q = 1; q < k && B; ++q)
							B = ib(i + di[p][0]*q, j + di[p][1]*q);
					}
				if (ir(i, j) && !R)
					for (int p = 0; p < 4 && !R; ++p) {
						R = 1;
						for (int q = 1; q < k && R; ++q)
							R = ir(i + di[p][0]*q, j + di[p][1]*q);
					}
			}
		if (B && R) puts("Both");
		else if (B) puts("Blue");
		else if (R) puts("Red");
		else puts("Neither");
	}
	return 0;
}
