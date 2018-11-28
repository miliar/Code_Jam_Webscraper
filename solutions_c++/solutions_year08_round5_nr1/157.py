#include <cstdio>
#include <string>
#include <vector>

using namespace std;

char cell[6002][6002];
char xwall[6002][6002];
char ywall[6002][6002];

int main()
{
	char inp[999];

	int cases;
	scanf("%d", &cases);

	for (int caseno = 1; caseno <= cases; caseno++) {
		int n, rep;
		scanf("%d", &n);
		string walk;
		for (int i = 0; i < n; i++) {
			scanf("%s%d", &inp, &rep);
			for (int j = 0; j < rep; j++) {
				walk += inp;
			}
		}

		memset(&(cell[0][0]), 0, sizeof(cell));
		memset(&(xwall[0][0]), 0, sizeof(xwall));
		memset(&(ywall[0][0]), 0, sizeof(ywall));

		int x = 3001, y = 3001, dir = 0;
		for (int i = 0; i < walk.size(); i++) {
			if (walk[i] == 'F') {
				if (dir == 0) {
					y--;
					xwall[x][y] = 1;
				} else if (dir == 1) {
					ywall[x][y] = 1;
					x++;
				} else if (dir == 2) {
					xwall[x][y] = 1;
					y++;
				} else {
					x--;
					ywall[x][y] = 1;
				}
			} else if (walk[i] == 'L') {
				dir = (dir + 3) % 4;
			} else if (walk[i] == 'R') {
				dir = (dir + 1) % 4;
			}
		}

		for (int x = 0; x < 6002; x++) {
			int lines = 0;
			for (int y = 0; y < 6002; y++) {
				if (ywall[x][y]) {
					lines ++;
				}
			}
			int index = 0;
			for (int y = 0; y < 6002; y++) {
				if (ywall[x][y]) {
					index ++;
				}
				if ((index & 1) == 0 && index != 0 && index != lines) {
					cell[x][y] = 1;
				}
			}
		}

		for (int y = 0; y < 6002; y++) {
			int lines = 0;
			for (int x = 0; x < 6002; x++) {
				if (xwall[x][y]) {
					lines ++;
				}
			}
			int index = 0;
			for (int x = 0; x < 6002; x++) {
				if (xwall[x][y]) {
					index ++;
				}
				if ((index & 1) == 0 && index != 0 && index != lines) {
					cell[x][y] = 1;
				}
			}
		}

		int count = 0;
		for (int x = 0; x < 6002; x++) {
			for (int y = 0; y < 6002; y++) {
				if (cell[x][y]) {
					count ++;
				}
			}
		}

		printf("Case #%d: %d\n", caseno, count);
	}

	return 0;
}
