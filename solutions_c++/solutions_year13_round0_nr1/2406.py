#include <cstdio>

using namespace std;

char grid[5][5];

int main() {
	freopen("smallin.txt", "r", stdin);
	freopen("smallout.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ti=0; ti<t; ti++) {
		printf("Case #%d: ", ti+1);
		for (int i=0; i<4; i++) {
			scanf("%s", grid[i]);
		}
		bool fin = true;
		bool x = false;
		bool o = false;
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				if (grid[i][j] == '.') {
					fin = false;
				}
			}
		}

		// x win
		{
			for (int i=0; i<4; i++) {
				bool cmp = true;
				for (int j=0; j<4; j++) {
					if (grid[i][j] != 'X' && grid[i][j] != 'T') {
						cmp = false;
					}
				}
				if (cmp) x = true;
			}
			for (int i=0; i<4; i++) {
				bool cmp = true;
				for (int j=0; j<4; j++) {
					if (grid[j][i] != 'X' && grid[i][j] != 'T') {
						cmp = false;
					}
				}
				if (cmp) x = true;
			}
			bool cmp = true;
			for (int i=0; i<4; i++) {
				if (grid[i][i] != 'X' && grid[i][i] != 'T') {
					cmp = false;
				}
			}
			if (cmp) x = true;
			cmp = true;
			for (int i=0; i<4; i++) {
				if (grid[3-i][i] != 'X' && grid[3-i][i] != 'T') {
					cmp = false;
				}
			}
			if (cmp) x = true;
		}

		// o win
		{
			for (int i=0; i<4; i++) {
				bool cmp = true;
				for (int j=0; j<4; j++) {
					if (grid[i][j] != 'O' && grid[i][j] != 'T') {
						cmp = false;
					}
				}
				if (cmp) o = true;
			}
			for (int i=0; i<4; i++) {
				bool cmp = true;
				for (int j=0; j<4; j++) {
					if (grid[j][i] != 'O' && grid[i][j] != 'T') {
						cmp = false;
					}
				}
				if (cmp) o = true;
			}
			bool cmp = true;
			for (int i=0; i<4; i++) {
				if (grid[i][i] != 'O' && grid[i][i] != 'T') {
					cmp = false;
				}
			}
			if (cmp) o = true;
			cmp = true;
			for (int i=0; i<4; i++) {
				if (grid[3-i][i] != 'O' && grid[3-i][i] != 'T') {
					cmp = false;
				}
			}
			if (cmp) o = true;
		}
		if (fin && !x && !o) {
			printf("Draw\n");
		}
		else if (fin) {
			printf("%c won\n", x?'X':'O');
		}
		else if (!x && !o) {
			printf("Game has not completed\n");
		}
		else {
			printf("%c won\n", x?'X':'O');
		}
	}
	return 0;
}

