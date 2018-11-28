#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;

int r, c;

char map[55][55];

bool judge() {
	int i, j;
	for (i = 0; i < r; ++i) {
			for (j = 0; j < c; ++j) {
				if (map[i][j] == '#') {
					map[i][j] = '/';

					if (j + 1 >= c)	return false;

					if (map[i][j+1] == '#')	{
						map[i][j+1] = '\\';
					}
					else 
						return false;

					if (i + 1 >= r)	return false;
					if (map[i + 1][j] == '#') {
						map[i + 1][j] = '\\';
					}
					else 
						return false;

					if (map[i + 1][j + 1] == '#'){
						map[i + 1][j + 1] = '/';
					}
					else
						return false;
				}
			}
	}
	return true;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("out1.txt", "w", stdout);

	int t, i, ii;
	scanf ("%d", &t);
	
	for (ii = 1; ii <= t; ++ii) {
		scanf ("%d%d", &r, &c);

		for (i = 0; i < r; ++i)	{
			scanf ("%s", map[i]);
		}

		bool flag = judge();

		printf("Case #%d:\n", ii);
		if (!flag)	puts("Impossible");
		else {
			for (i = 0; i < r; ++i) {
				printf("%s\n", map[i]);
			}
		}
	}
	return 0;
}

