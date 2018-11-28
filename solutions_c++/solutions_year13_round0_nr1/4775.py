#include<stdio.h>
#include<stdlib.h>

char square[4][4];
int T;
int round;

inline void Input()
{
	round = 0;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			square[i][j] = getchar();
			if (square[i][j] == 'X' ||
			    square[i][j] == 'O' ||
			    square[i][j] == 'T') {
				round++;
			}
		}	
		getchar();
	}
	getchar();
}

void Test()
{
	if (round <= 5) {
		printf("Game has not completed\n");
		return;
	}
	int cntX, cntO;
	//detect row
	for (int i = 0; i < 4; i++) {
		cntX = cntO = 0;
		for (int j = 0; j < 4; j++) {
			if (square[i][j] == 'X'){
				cntX++;
			} else if (square[i][j] == 'O') {
				cntO++;
			} else if (square[i][j] == 'T') {
				cntX++;
				cntO++;
			} else {
				continue;
			}
		}
		if (cntX == 4) {
			printf("X won\n");
			return;
		} else if (cntO == 4) {
			printf("O won\n");
			return;
		} 
	}
	//detect col
	for (int i = 0; i < 4; i++) {
		cntX = cntO = 0;
		for (int j = 0; j < 4; j++) {
			if (square[j][i] == 'X'){
				cntX++;
			} else if (square[j][i] == 'O') {
				cntO++;
			} else if (square[j][i] == 'T') {
				cntX++;
				cntO++;
			} else {
				continue;
			}
		}
		if (cntX == 4) {
			printf("X won\n");
			return;
		} else if (cntO == 4) {
			printf("O won\n");
			return;
		} 
	}
	//detect diag
	cntX = cntO = 0;
	for (int i = 0; i < 4; i++) {
		if (square[i][i] == 'X'){
			cntX++;
		} else if (square[i][i] == 'O') {
			cntO++;
		} else if (square[i][i] == 'T') {
			cntX++;
			cntO++;
		} else {
			break;
		}
	}
	if (cntX == 4) {
		printf("X won\n");
		return;
	} else if (cntO == 4) {
		printf("O won\n");
		return;
	} 
	//detect anti_diag
	cntX = cntO = 0;
	for (int i = 0; i < 4; i++) {
		if (square[i][3-i] == 'X'){
			cntX++;
		} else if (square[i][3-i] == 'O') {
			cntO++;
		} else if (square[i][3-i] == 'T') {
			cntX++;
			cntO++;
		} else {
			break;
		}
	}
	if (cntX == 4) {
		printf("X won\n");
		return;
	} else if (cntO == 4) {
		printf("O won\n");
		return;
	} 
	if (round < 16) {
		printf("Game has not completed\n");
	} else {
		printf("Draw\n");
	}
}

int main()
{
	//freopen("./A-large.in", "r", stdin);
	//freopen("./large.out","w",stdout);
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++) {
		Input();
		printf("Case #%d: ", i+1);
		Test();
	}
	return 0;
}
