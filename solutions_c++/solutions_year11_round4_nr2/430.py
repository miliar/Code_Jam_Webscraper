#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int n, m, d;
int board[505][505];


int main() {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
		int r;
		int case_no = 0;
		scanf("%d", &r);
		while (r--) {
				scanf("%d %d %d", &n, &m, &d);
				char row[505];
				for (int i = 0; i < n; ++i) {
						scanf("%s", row);
						for (int j = 0; j < m; ++j)
								board[i][j] = row[j] - '0' + d;
				}
				int sol = 0;
				for (int s = 3; s <= max(n, m); s++) {
						for (int i = 0; i < n - s + 1; ++i) {
								for (int j = 0; j < m - s + 1; ++j) {
										double px = 0, py = 0;
										double cy = i + (s - 1) / 2.0;
										double cx = j + (s - 1) / 2.0;
										for (int a = i; a < i + s; ++a) {
												for (int b = j; b < j + s; ++b) {
														int iy = a - i, ix = b - j;
														if (iy == 0 && ix == 0) continue;
														if (iy == 0 && ix == s - 1) continue;
														if (iy == s - 1 && ix == 0) continue;
														if (iy == s - 1 && ix == s - 1) continue;

														px += board[a][b] * (b - cx);
														py += board[a][b] * (a - cy);
												}
										}
										if (fabs(px) < 1e-7 && fabs(py) < 1e-7) {
												sol = s;
										}
								}
						}
				}
				printf("Case #%d: ", ++case_no);
				if (sol == 0) printf("IMPOSSIBLE\n");
				else printf("%d\n", sol);
		}
		return 0;
}