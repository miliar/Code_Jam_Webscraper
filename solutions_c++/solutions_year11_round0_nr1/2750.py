/*
 * A.cpp
 *
 *  Created on: 2011-5-7
 *      Author: stm
 */

#include <cstdio>
#include <cstring>

const int MAXN = 110;

int main()
{
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, n;
	char c;
	int k;
	int B[MAXN], O[MAXN], p[MAXN][2], nB, nO;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &n);
		nB = nO = 0;
		for (int i = 0; i < n; ++i) {
			scanf(" %c %d", &c, &k);
			if (c == 'B') {
				p[i][0] = 0;
				B[nB++] = k;
			}
			else {
				p[i][0] = 1;
				O[nO++] = k;
			}
			p[i][1] = k;
		}

		int pB = 0, pO = 0, curB = 1, curO = 1;
		int ans = 0;
		int i = 0;
		while (pB < nB || pO < nO)
		{
			if (i >= n) break;
			bool pushed = 0;
			if (pB < nB) {
				if (curB < B[pB]) curB++;
				else
				if (curB > B[pB]) curB--;
				else
				if (p[i][0] ==0) {
					pB++; i++;
					pushed = 1;
				}
			}
			if (pO < nO) {
				if (curO < O[pO]) curO++;
				else
				if (curO > O[pO]) curO--;
				else
				if (p[i][0] == 1 && (!pushed)) {
					pO++; i++;
				}
			}
			++ans;
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
