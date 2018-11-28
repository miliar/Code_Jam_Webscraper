// MS Visual C++ 2008 Express
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

char s[501];
long long w[501][501], vx[501][501], vy[501][501];
long long sw[501][501], svx[501][501], svy[501][501];

int main()
{
	freopen("B-Large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tk = 1; tk <= T; tk++) {
		int r, c, d;
		scanf("%d%d%d", &r, &c, &d);
		for (int i = 0; i < r; i++)	{
			scanf("%s", s);
			for (int j = 0; j < c; j++) w[i][j] = s[j] - '0';
		}
		for (int i = 0; i < r; i++) 
			for (int j = 0; j < c; j++) {
				vx[i][j] = w[i][j] * i;
				vy[i][j] = w[i][j] * j;
			}

		for (int j = 0; j <= c; j++) sw[0][j] = svx[0][j] = svy[0][j] = 0;
		for (int i = 1; i <= r; i++) {
			sw[i][0] = svx[i][0] = svy[i][0] = 0;
			for (int j = 1; j <= c; j++) {
				svx[i][j] = svx[i - 1][j] + svx[i][j - 1] - svx[i - 1][j - 1] + w[i - 1][j - 1] * (i - 1);
				svy[i][j] = svy[i - 1][j] + svy[i][j - 1] - svy[i - 1][j - 1] + w[i - 1][j - 1] * (j - 1);
				sw[i][j] = sw[i - 1][j] + sw[i][j - 1] - sw[i - 1][j - 1] + w[i - 1][j - 1];
			}
		}

		int k = min(r, c) + 1, f = 0;
		while (!f) {
			k--;
			for (int i = 0; i <= r - k && !f; i++)
				for (int j = 0; j <= c - k && !f; j++) {
					long long m = sw[i + k][j + k] - sw[i][j + k] - sw[i + k][j] + sw[i][j] -
						w[i + k - 1][j + k - 1] - w[i][j + k - 1] - w[i + k - 1][j] - w[i][j];

					long long vmx = svx[i + k][j + k] - svx[i][j + k] - svx[i + k][j] + svx[i][j] -
						vx[i + k - 1][j + k - 1] - vx[i][j + k - 1] - vx[i + k - 1][j] - vx[i][j];

					long long vmy = svy[i + k][j + k] - svy[i][j + k] - svy[i + k][j] + svy[i][j] -
						vy[i + k - 1][j + k - 1] - vy[i][j + k - 1] - vy[i + k - 1][j] - vy[i][j];

					f = (m * (2*i + k - 1) == 2*vmx && m * (2*j + k - 1) == 2*vmy);
				}
		}
		if (k < 3) printf("Case #%d: IMPOSSIBLE\n", tk, k);
		else printf("Case #%d: %d\n", tk, k);
	}

	return 0;
}