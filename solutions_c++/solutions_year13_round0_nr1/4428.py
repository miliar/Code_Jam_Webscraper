#include <iostream>
#include <cstdio>
using namespace std;
const int oo = 1e9+7;
char g[6][6];
bool c1(int i, int j) {
	for (int k = j; k < j + 3; k++) if (g[i][k] != g[i][k+1]) return false;
	return true;
}
bool c2(int i, int j) {
	for (int k = i; k < i + 3; k++) if (g[k][j] != g[k+1][j]) return false;
	return true;
}
bool c3(int i, int j) {
	for (int k = 0; k < 3; k++) if (g[i+k][j+k] != g[i+k+1][j+k+1]) return false;
	return true;
}
bool c4(int i, int j) {
	for (int k = 0; k < 3; k++) if (g[i+k][j-k] != g[i+k+1][j-k-1]) return false;
	return true;
}
int main()
{
	int tests;
	scanf ("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		for (int i = 0; i < 4; i++)
			scanf ("%s", g[i]);
		int X = 0, O = 0;
		int tx = -1, ty = -1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				if (g[i][j] == 'T') tx = i, ty = j;
				else if (g[i][j] == 'X') X++;
				else if (g[i][j] == 'O') O++;
			}
		char last = 'X';
		if (X == O) last = 'O';
		if (tx != -1 && ty != -1)
			g[tx][ty] = last;

		bool won = false;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) if (g[i][j] == last) {
				if ((j+3 < 4) && c1(i, j)) {
					won = true;
				}
				if ((i + 3 < 4) && c2(i, j)) {
					won = true;
				}
				if ((i + 3< 4) && (j + 3< 4) && c3(i, j)) {
					won = true;
				}
				if ((i + 3 < 4) && j > 2 && c4(i, j)) {
					won = true;
				}
			}
		}
		if (won) {
			printf ("Case #%d: %c won\n", test, last);
		} else {
			bool completed = true;
			for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) completed &= (g[i][j] != '.');
			if (completed)
				printf ("Case #%d: Draw\n", test);
			else
				printf ("Case #%d: Game has not completed\n", test);
		}
	}
	return 0;
}