/*
 * B.cpp
 *
 *  Created on: 2011-5-7
 *      Author: stm
 */

#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 110;
char s[MAXN], ans[MAXN], c[MAXN][MAXN], d[MAXN][MAXN];
int T, n, C, D, tot;

bool Match(char a, char b, char aa, char bb)
{
	return (a == aa && b == bb) || (a == bb && b == aa);
}

int main()
{
	//freopen("B-small.in", "r", stdin);
	//freopen("B-small.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &C);
		for (int i = 0; i < C; ++i) scanf("%s", c[i]);
		scanf("%d", &D);
		for (int i = 0; i < D; ++i) scanf("%s", d[i]);
		scanf("%d", &n);
		scanf("%s", s);

		tot = 0;
		for (int i = 0; i < n; ++i) {
			if (tot == 0) {
				ans[tot++] = s[i];
				continue;
			}
			bool found = false;
			for (int j = 0; j < C; ++j)
				if (Match(c[j][0], c[j][1], ans[tot - 1], s[i])) {
					found = true;
					ans[tot - 1] = c[j][2];
					break;
				}
			if (found) continue;
			bool found2 = false;
			for (int j = 0; j < D && (!found2); ++j)
				for (int k = 0; k < tot; ++k)
					if (Match(d[j][0], d[j][1], ans[k], s[i])) {
						tot = 0;
						found2 = true;
						break;
					}
			if (found2) continue;
			ans[tot++] = s[i];
		}

		printf("Case #%d: ", t);
		if (tot == 0) puts("[]");
		else {
			printf("[");
			for (int i = 0; i < tot - 1; ++i) {
				printf("%c, ", ans[i]);
			}
			printf("%c", ans[tot - 1]);
			puts("]");
		}
	}
}
