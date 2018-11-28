#include <cstdio>
#include <algorithm>
using namespace std;

int T;
char str[505];
int r, c, d, grid[505][505];
int weightx[505][505], weighty[505][505], u[505][505];
int prex[505][505], prey[505][505], preu[505][505];
int main() {
	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("B.out", "w");

	fscanf(fin, "%d", &T);
	for (int test = 0; test < T; test++) {
		fscanf(fin, "%d %d %d\n", &r, &c, &d);
		for (int i = 1; i <= r; i++) {
			fgets(str+1, 505, fin);
			for (int j = 1; j <= c; j++) {
				grid[i][j] = str[j] - '0';
				weightx[i][j] = weightx[i][j-1] + grid[i][j]*i;
				weighty[i][j] = weighty[i][j-1] + grid[i][j]*j;
				u[i][j] = u[i][j-1] + grid[i][j];
				//printf("%d ", weightx[i][j]);
			}
			//printf("\n");
		}


		int ans = 0;

		for (int size = 3; size <= min(r, c); size++) {
			for (int j = size; j <= c; j++) {
				for (int i = 1; i <= r; i++) {
					prex[i][j] = prex[i-1][j] + weightx[i][j] - weightx[i][j-size];
					prey[i][j] = prey[i-1][j] + weighty[i][j] - weighty[i][j-size];
					preu[i][j] = preu[i-1][j] + u[i][j] - u[i][j-size];
					//printf("prex[%d][%d] = %d\n", i, j, prex[i][j]);
				}
			}
			for (int sx = size; sx <= r; sx++) {
				for (int sy = size; sy <= c; sy++) {
					int wx = prex[sx][sy] - prex[sx-size][sy];
					int wy = prey[sx][sy] - prey[sx-size][sy];
					int sum = preu[sx][sy] - preu[sx-size][sy];


					// sx-size+1, sy-size+1
					wx -= grid[sx-size+1][sy-size+1]*(sx-size+1);
					wy -= grid[sx-size+1][sy-size+1]*(sy-size+1);
					sum -= grid[sx-size+1][sy-size+1];

					wx -= grid[sx-size+1][sy]*(sx-size+1);
					wy -= grid[sx-size+1][sy]*(sy);
					sum -= grid[sx-size+1][sy];

					wx -= grid[sx][sy-size+1]*(sx);
					wy -= grid[sx][sy-size+1]*(sy-size+1);
					sum -= grid[sx][sy-size+1];

					wx -= grid[sx][sy]*(sx);
					wy -= grid[sx][sy]*(sy);
					sum -= grid[sx][sy];

					//printf("lower corner = (%d, %d), wx, wy = %d, %d, sum = %d\n", sx, sy, wx, wy, sum);
					if (wx == (sum) * (2*sx-size+1)/2 && wy == sum*(2*sy-size+1)/2) {
						//printf("lower corner %d, %d size %d works\n", sx, sy, size);
						ans = max(ans, size);
					}
				}
			}
		}
		//if (ans > 0) printf("Case #%d: %d\n", test+1, ans);
		//else printf("Case #%d: IMPOSSIBLE\n", test+1);
		if (ans > 0) fprintf(fout, "Case #%d: %d\n", test+1, ans);
		else fprintf(fout, "Case #%d: IMPOSSIBLE\n", test+1);
	}


	return 0;
}
