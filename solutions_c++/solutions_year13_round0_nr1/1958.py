#include <stdio.h>
#include <algorithm>
using namespace std;

int n;
char b[6][6];

bool checkWinInLine(char player, int init[], int mv[]) {
	int i=init[0], j=init[1];

	for (int k=0; k<4; k++) {
		if (b[i][j]!='T' && b[i][j]!=player)
			return false;
	
		i+=mv[0], j+=mv[1];
	}

	return true;
}

bool checkComplete() {
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			if (b[i][j]=='.')
				return false;
	return true;
}

bool checkWin(char player) {
	int init[][2] = {{0,0}, {0,1}, {0,2}, {0,3},
			{0,0}, {1,0}, {2,0}, {3,0},
			{0,0},{3,0}};
	int mv[][2] = {{1,0},{1,0},{1,0},{1,0},
			{0,1},{0,1},{0,1},{0,1},
			{1,1},{-1,1}};

	for (int i=0; i<10; i++)
		if (checkWinInLine(player,init[i],mv[i]))
			return true;
	return false;
}

int main() {
	scanf("%d", &n);

	for (int i=1; i<=n; i++) {
		for (int j=0; j<4; j++)
			scanf(" %s", b[j]);

		printf("Case #%d: ", i);
		
		if (checkWin('X'))
			printf("X won");
		else if (checkWin('O'))
			printf("O won");
		else if (checkComplete())
			printf("Draw");
		else
			printf("Game has not completed");

		printf("\n");
	}
	return 0;
}
