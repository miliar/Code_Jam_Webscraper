/*
 * A.cpp
 *
 *  Created on: 2011-5-22
 *      Author: stm
 */

#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

const int MAXN = 100;
char s[MAXN][MAXN];
int r, c, T;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d%d", &r, &c);
		for (int i = 0; i < r; ++i)
			scanf("%s", s[i]);

		printf("Case #%d:\n", t);

		int tot = 0;
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
				if (s[i][j] == '#') tot++;

		if (tot % 4) {
			printf("Impossible\n");
			continue;
		}

		bool ok = true;
		for (int i = 0; i < r && ok; ++i)
			for (int j = 0; j < c && ok; ++j)
				if (s[i][j] == '#') {
					if (j + 1 >= c) {
						ok = false; break;
					}
					if (s[i][j + 1] != '#') {
						ok = false; break;
					}
					if (i + 1 >= r) {
						ok = false; break;
					}
					if (s[i + 1][j] != '#' || s[i + 1][j + 1] != '#') {
						ok = false; break;
					}
					s[i][j] = s[i + 1][j + 1] = '/';
					s[i][j + 1] = s[i + 1][j] = '\\';
				}

		if (!ok) {
			printf("Impossible\n");
		}
		else {
			for (int i = 0; i < r; ++i)
				puts(s[i]);
		}
	}
	return 0;
}
