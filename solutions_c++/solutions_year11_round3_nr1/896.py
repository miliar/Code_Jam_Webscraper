#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <string>
#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define	MAXN	100

int main(int argc, char *argv[])
{
	int nc, ci;
	static char m[MAXN][MAXN];
	
	scanf("%d", &nc);
	for (ci = 1; ci <= nc; ci++) {
		int r, c, i, j;

		scanf("%d %d", &r, &c);
		for (i = 0; i < r; i++)
			scanf("%s", m[i]);
		
		for (i = 0; i < r - 1; i++) {
			for (j = 0; j < c - 1; j++) {
				if (m[i][j] == '#' && m[i][j + 1] == '#' && 
				    m[i + 1][j] == '#' && m[i + 1][j + 1] == '#') {
					m[i][j] = '/';
					m[i][j + 1] = '\\';
					m[i + 1][j] = '\\';
					m[i + 1][j + 1] = '/';
				}
			}
		}

		bool ok = true;
		for (i = 0; i < r; i++)
			for (j = 0; j < c; j++)
				if (m[i][j] == '#') {
					ok = false;
					break;
				}
				
		printf("Case #%d:\n", ci);
		if (ok) {
			for (i = 0; i < r; i++)
				printf("%s\n", m[i]);
		} else {
			printf("Impossible\n");
		}
	}
	
	return 0;
}
