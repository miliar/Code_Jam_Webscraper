#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;


char line[1024];
char map[55][55];
int main()
{
	int kase, serial=1,
		row, col;

	bool ok;

	gets(line);
	kase = atoi(line);
	while (kase--) {
		// begin test case
		ok = true;

		gets(line);
		sscanf(line, "%d %d", &row, &col);

		for (int r=0; r<row; ++r)
			gets(map[r]);

		for (int r=0, c; r<row; ++r) {
			for (c=0; c<col; ++c) {
				if (map[r][c] == '#') {
					if (r + 1 < row && c + 1 < col) {
						map[r][c] = '/';
						if (map[r+1][c+1] == '#')
							map[r+1][c+1] = '/';
						else
							ok = false;
						if (map[r][c+1] == '#')
							map[r][c+1] = '\\';
						else
							ok = false;
						if (map[r+1][c] == '#')
							map[r+1][c] = '\\';
						else
							ok = false;
					}
					else
						ok = false;
				}
			}
		}

		printf("Case #%d:\n", serial++);
		if (ok) {
			for (int r=0; r<row; ++r)
				puts(map[r]);
		}
		else
			puts("Impossible");
		// end test case
	}
	return 0;
}
