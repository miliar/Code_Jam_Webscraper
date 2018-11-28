#include <cstdio>

int t;
int n, k;
char matr[50][50];
char rmatr[50][50];
//int dp[50][50];

void MakeLength(int x, int y, int sx, int sy, bool& bwin, bool& rwin) {
	int cnt = 1;
	int px = x;
	int py = y;
	x += sx;
	y += sy;
	while (x >= 0 && x < n && y >= 0 && y < n) {
		if (rmatr[px][py] == rmatr[x][y]) {
			cnt++;
			if (cnt >= k) {
				if (rmatr[x][y] == 'B') {
					bwin = true;
				}
				else if (rmatr[x][y] == 'R') {
					rwin = true;
				}
			}
		}
		else {
			cnt = 1;
		}

		px = x;
		py = y;
		x += sx;
		y += sy;
	}
}

int main() {

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &t);

	for (int gi = 1; gi <= t; gi++) {
		scanf("%d %d\n", &n, &k);
		for (int xi = 0; xi < n; xi++) {
			fgets(matr[xi], 50, stdin);
		}

   		for (int xi = 0; xi < n; xi++) {
			for (int yi = 0; yi < n; yi++) {
				rmatr[yi][n-xi-1] = matr[xi][yi];
			}
		}

		// rotate
		for (int yi = 0; yi < n; yi++) {
			int empty_cnt = 0;
			for (int xi = n - 1; xi >= 0; xi--) {
				if (rmatr[xi][yi] != '.') {
					if (empty_cnt > 0) {
						rmatr[xi + empty_cnt][yi] = rmatr[xi][yi];
						rmatr[xi][yi] = '.';
					}
				}
				else {
					empty_cnt++;
				}
			}
		}
/*
		for (int xi = 0; xi < n; xi++) {
			for (int yi = 0; yi < n; yi++) {
				printf("%c ", rmatr[xi][yi]);
			}
			printf("\n");
		}
*/
		bool rwin = false;
		bool bwin = false;

		// lines
		for (int xi = 0; xi < n; xi++) {
			MakeLength(xi, 0, 0, 1, bwin, rwin);
/*			for (int yi = 0; yi < n; yi++) {
				if (yi == 0) {
					dp[xi][yi] = 1;
				}
				else {
					if (rmatr[xi][yi-1] == rmatr[xi][yi]) {
						dp[xi][yi] = dp[xi][yi-1] + 1;
						if (dp[xi][yi] >= k) {
							if (rmatr[xi][yi] == 'R') {
								rwin = true;
							}
							else if (rmatr[xi][yi] == 'B') {
								bwin = true;
							}
						}
					}
					else {
						dp[xi][yi] = 1;
					}
				}
			}*/
		}

//		memset(dp, 0, sizeof(dp));

		// columns
		for (int yi = 0; yi < n; yi++) {
			MakeLength(n - 1, yi, -1, 0, bwin, rwin);
			/*for (int xi = n - 1; xi >= 0; xi--) {
				if (rmatr[xi][yi] == '.') {
					break;
				}
				if (xi == n - 1) {
					dp[xi][yi] = 1;
				}
				else {
					if (rmatr[xi + 1][yi] == rmatr[xi][yi]) {
						dp[xi][yi] = rmatr[xi + 1][yi] + 1;
						if (dp[xi][yi] >= k) {
							if (rmatr[xi][yi] == 'R') {
								rwin = true;
							}
							else if (rmatr[xi][yi] == 'B') {
								bwin = true;
							}
						}
					}
					else {
						dp[xi][yi] = 1;
					}
				}
			}*/
		}

		for (int xi = 0; xi < n; xi++) {
			MakeLength(xi, 0, 1, 1, bwin, rwin);
			MakeLength(xi, 0, -1, 1, bwin, rwin);
		}

		for (int yi = 0; yi < n; yi++) {
			MakeLength(0, yi, 1, 1, bwin, rwin);
			MakeLength(n - 1, yi, -1, 1, bwin, rwin);
		}

		printf("Case #%d: ", gi);
		if (!bwin && !rwin) {
			printf("Neither\n");
		}
		if (bwin && rwin) {
			printf("Both\n");
		}
		if (!bwin && rwin) {
			printf("Red\n");
		}
		if (bwin && !rwin) {
			printf("Blue\n");
		}
	}

	return 0;
}
