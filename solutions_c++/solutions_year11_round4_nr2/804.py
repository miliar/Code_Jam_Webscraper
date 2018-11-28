#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxl = 503;

int table[maxl][maxl];
int row[maxl][maxl][maxl], col[maxl][maxl][maxl];
int mark[maxl][maxl];
int R, C, D, maxK, cnt;

bool check(int k) {
	for (int i = 0; i + k < R; i++) {
		int sum = 0;
		for (int j = 1; j < k; j++)
			sum += col[i + k / 2][j][k];
		sum += col[i + k / 2][0][k - 2] + col[i + k / 2][k][k - 2];
		for (int j = 0; j + k < C; j++) {
			if (!sum) mark[i][j] = cnt;
			if (j + k + 1 < C) {
				sum -= col[i + k / 2][j][k - 2];
				sum -= col[i + k / 2][j + 1][k];
				sum += col[i + k / 2][j + 1][k - 2];
				sum -= col[i + k / 2][j + k][k - 2];
				sum += col[i + k / 2][j + k][k];
				sum += col[i + k / 2][j + k + 1][k - 2];
			}
		}
	}
	for (int j = 0; j + k < C; j++) {
		int sum = 0;
		for (int i = 1; i < k; i++)
			sum += row[i][j + k / 2][k];
		sum += row[0][j + k / 2][k - 2] + row[k][j + k / 2][k - 2];
		for (int i = 0; i + k < R; i++) {
			if (!sum)
				if (mark[i][j] == cnt) {
					//printf("%d %d\n", i, j);
					return true;
				}
			if (i + k + 1 < R) {
				sum -= row[i][j + k / 2][k - 2];
				sum -= row[i + 1][j + k / 2][k];
				sum += row[i + 1][j + k / 2][k - 2];
				sum -= row[i + k][j + k / 2][k - 2];
				sum += row[i + k][j + k / 2][k];
				sum += row[i + k + 1][j + k / 2][k - 2];
			}
		}
	}
	return false;
}

void solve() {
	scanf("%d %d %d", &R, &C, &D);
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++) {
			char ch;
			scanf(" %c", &ch);
			table[i][j] = ch - '0';
		}
	//for (int i = 0; i < R; i++) {
	//	for (int j = 0; j < C; j++)
	//		printf(" %d", table[i][j]);
	//	printf("\n");
	//}
	maxK = min(R, C);
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++) {
			row[i][j][0] = col[i][j][0] = 0;
			row[i][j][1] = -table[i][j] + table[i][j + 1];
			col[i][j][1] = -table[i][j] + table[i + 1][j];
		}
	for (int k = 2; k < maxK; k++)
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++) {
				int delta = k / 2;
				if (k & 1) {
					if (j - delta >= 0 && j + delta < C)
						row[i][j][k] = row[i][j][k - 2] + (delta * 2 + 1) * (-table[i][j - delta] + table[i][j + delta + 1]);
					if (i - delta >= 0 && i + delta < R)
						col[i][j][k] = col[i][j][k - 2] + (delta * 2 + 1) * (-table[i - delta][j] + table[i + delta + 1][j]);
				} else {
					if (j - delta >= 0 && j + delta <= C)
						row[i][j][k] = row[i][j][k - 2] + delta * 2 * (-table[i][j - delta] + table[i][j + delta]);
					if (i - delta >= 0 && i + delta <= R)
						col[i][j][k] = col[i][j][k - 2] + delta * 2 * (-table[i - delta][j] + table[i + delta][j]);
				}
			}
	cnt = 0;
	memset(mark, 255, sizeof mark);
	for (int i = maxK - 1; i >= 2; i--) {
		if (check(i)) {
			printf("%d\n", i + 1);
			return;
		}
		cnt++;
	}
	printf("IMPOSSIBLE\n");
}

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-1.out", "w", stdout);
	int t, i;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}