#include <vector>
#include <string>
#include <algorithm>

using namespace std;


const int MAX = 110;
int H, W;
int tab[MAX][MAX], ans[MAX][MAX];
char curChar;


// true if I need to change everything back the way, false otherwise
bool followPath(int i, int j) {
	int nextX = -1, nextY = -1, minAlt = 10000;

	if (i-1 >= 0 && tab[i-1][j] < tab[i][j] && tab[i-1][j] < minAlt) { //N
		nextX = i-1; nextY = j;
		minAlt = tab[i-1][j];
	}
	if (j-1 >= 0 && tab[i][j-1] < tab[i][j] && tab[i][j-1] < minAlt) { //W
		nextX = i; nextY = j-1;
		minAlt = tab[i][j-1];
	}
	if (j+1 < W && tab[i][j+1] < tab[i][j] && tab[i][j+1] < minAlt) { //E
		nextX = i; nextY = j+1;
		minAlt = tab[i][j+1];
	}
	if (i+1 < H && tab[i+1][j] < tab[i][j] && tab[i+1][j] < minAlt) { //S
		nextX = i+1; nextY = j;
		minAlt = tab[i+1][j];
	}

	if (minAlt == 10000) {
		ans[i][j] = curChar++;
		return false;
	}
	if (ans[nextX][nextY] != '-') {
		ans[i][j] = ans[nextX][nextY];
		return true;
	}

	ans[i][j] = curChar;
	if (followPath(nextX, nextY)) {
		ans[i][j] = ans[nextX][nextY];
		return true;
	}
	return false;
}


int main() {
	int T;
	scanf("%d", &T);

	for (int C = 1; C <= T; C++) {
		scanf("%d %d", &H, &W);

		curChar = 'a';

		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				scanf("%d", &tab[i][j]);

				ans[i][j] = '-';
			}
		}

		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (ans[i][j] == '-')
					followPath(i, j);
			}
		}

		printf("Case #%d:\n", C);
		for (int i = 0; i < H; i++) {
			printf("%c", ans[i][0]);
			for (int j = 1; j < W; j++) {
				printf(" %c", ans[i][j]);
			}
			printf("\n");
		}
	}

	return 0;
}
