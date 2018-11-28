#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int CaseN, R, C, D, mat[502][502], ans ;
char ch, buf[500];

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &CaseN);
	for (int CaseID = 1; CaseID <= CaseN; CaseID++) {
		scanf("%d %d %d\n", &R, &C, &D);
		for (int i = 1; i <= R; i++) {
			for (int j = 1; j <= C; j++) {
				scanf("%c", &ch);
				mat[i][j] = D + (ch - '0');
			}
			gets(buf);
		}
		ans = -1;
		// odd
		for (int i = 2; i <= R-1; i++)
			for (int j = 2; j <= C-1; j++) {
				for (int size = 1; ; size++) {
					if (i - size < 1 || i + size > R) break;
					if (j - size < 1 || j + size > C) break;
					int sumx = 0, sumy = 0;
					for (int ii = i - size; ii <= i + size; ii++)
						for (int jj = j - size; jj <= j + size; jj++) {
							if ((ii == i - size || ii == i + size) && (jj == j - size || jj == j + size)) continue;
							sumx += (ii - i) * mat[ii][jj];
							sumy += (jj - j) * mat[ii][jj];
						}
					if (!sumx && !sumy) {
						if (size * 2 + 1 > ans) ans = size * 2 + 1;
					}
				}
			}
		// even
		for (int i = 2; i <= R-2; i++)
			for (int j = 2; j <= C-2; j++) {
				for (int size = 2; ; size++) {
					if (i - size + 1 < 1 || i + size > R) break;
					if (j - size + 1 < 1 || j + size > C) break;
					double sumx = 0, sumy = 0;
					for (int ii = i - size + 1; ii <= i + size; ii++)
						for (int jj = j - size + 1; jj <= j + size; jj++) {
							if ((ii == i - size + 1 || ii == i + size) && (jj == j - size + 1 || jj == j + size)) continue;
							sumx += ((double)(ii - 0.5) - i) * mat[ii][jj];
							sumy += ((double)(jj - 0.5) - j) * mat[ii][jj];
						}
					if (abs(sumx) < 1e-8 && abs(sumy) < 1e-8) {
						if (size * 2 > ans) ans = size * 2;
					}
				}
			}
		if (ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", CaseID);
		else
			printf("Case #%d: %d\n", CaseID, ans);
	}
	
	return 0;
}
