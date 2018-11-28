#if 1
#include <iostream>
#include <stdio.h>
using namespace std;
char map[51][51];
int R, C;
int main()
{
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		cin >> R >> C;
		for (int i = 0; i < R; i++) scanf("%s", map[i]);
		bool found;
		bool sol = true;
		do {
			found = false;
			bool stop = false;
			for (int i = 0; i < R && !stop; i++)
				for (int j = 0; j < C && !stop; j++)
					if (map[i][j] == '#') {
						found = true;
						if (map[i][j + 1] == '#' && map[i + 1][j] == '#' && map[i + 1][j + 1] == '#') {
							stop = true;
							map[i][j] = '/'; map[i][j + 1] = '\\';
							map[i + 1][j] = '\\'; map[i + 1][j + 1] = '/';
						} else {
							sol = false;
							stop = true;
						}
					}
		} while (found && sol);
		printf("Case #%d:\n", cases);
		if (!sol) puts("Impossible");
		else {
			for (int i = 0; i < R; i++)
				puts(map[i]);
		}
	}
	return 0;
}
#endif