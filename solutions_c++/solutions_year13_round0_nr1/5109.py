//a.cpp
//By λKT345

#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

#define TR(container, it) \
	for(typeof(container.begin()) it = container.begin(); it != container.end(); ++it)

int directions[4][2][2] = {{{1, 1}, {-1, -1}}, {{0, 1}, {0, -1}},
						   {{1, 0}, {-1, 0}}, {{1, -1}, {-1, 1}}};
int directionsInt[8][2] = {{1, 1}, {0, 1}, {1, 0}, {1, -1},
						   {-1, -1}, {0, -1}, {-1, 0}, {-1, 1}};
char curr[4][5];

int check(int i, int j, char currChar, int dir) {
	if(i >= 4 || i < 0 || j >= 4 || j < 0) return 0;
	if(curr[i][j] != currChar && curr[i][j] != 'T') return 0;
	return check(i + directionsInt[dir][0], j + directionsInt[dir][1], currChar, dir) + 1;
}

bool checkWon(int i, int j, char currChar) {
	int maxCount = 0;
	for(int k = 0; k < 4; ++k) {
		maxCount = max(maxCount,
						check(i + directions[k][0][0], j + directions[k][0][1], currChar, k) + 
						check(i + directions[k][1][0], j + directions[k][1][1], currChar, k + 4) + 1);
	}
	return(maxCount >= 4);
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; ++t) {
		for(int i = 0; i < 4; ++i) {
			scanf("%s", curr[i]);
		}
		bool oWon = false, xWon = false;
		bool gameCompleted = true;
		for(int i = 0; i < 4; ++i) {
			for(int j = 0; j < 4; ++j) {
				char c = curr[i][j];
				if(c == 'T') {
					xWon = (xWon || checkWon(i, j, 'X'));
					oWon = (oWon || checkWon(i, j, 'O'));
				} else if(c == 'X') {
					xWon = (xWon || checkWon(i, j, 'X'));
				} else if(c == 'O') {
					oWon = (oWon || checkWon(i, j, 'O'));
				} else {
					gameCompleted = false;
				}
			}
		}
		if(oWon) {
			if(xWon) {
				printf("Case #%d: Draw\n", t + 1);
			} else {
				printf("Case #%d: O won\n", t + 1);
			}
		} else if(xWon) {
			printf("Case #%d: X won\n", t + 1);
		} else if(gameCompleted) {
			printf("Case #%d: Draw\n", t + 1);
		} else {
			printf("Case #%d: Game has not completed\n", t + 1);
		}
	}
	return 0;
}
