/*
 * A.cpp
 *
 *  Created on: May 22, 2011
 *      Author: yassery
 */

#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

char grid[100][100];

int main() {
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
	freopen("test.txt", "wt", stdout);
#endif

	int TC,r,c;
	cin >> TC;

	for (int tt = 0; tt < TC; tt++) {
		printf("Case #%d:\n",tt+1);
		cin >> r >> c;

		for (int i = 0; i < 100; i++)
			for (int j = 0; j < 100; j++)
				grid[i][j] = '-';

		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
				cin >> grid[i][j];

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (grid[i][j] == '#') {
					if (grid[i + 1][j] != '#' || grid[i + 1][j + 1] != '#'
							|| grid[i][j + 1] != '#')
						goto impossible;
					grid[i][j] = '/';
					grid[i + 1][j] = '\\';
					grid[i + 1][j + 1] = '/';
					grid[i][j + 1] = '\\';
				}
			}
		}
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				printf("%c",grid[i][j]);
			}
			printf("\n");
		}

		continue;
		impossible: ;
		printf("Impossible\n");
	}

	return 0;
}
