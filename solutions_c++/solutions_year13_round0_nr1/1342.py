#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <cmath>
using namespace std;

#define CY 10

char S[CY][CY];
int N = 4, M = 4;

int can(int n, int m) {
	int O, X, T, sum = 0;
	for (int i = 0; i < n; ++i) {
		O = 0; X = 0, T = 0;
		for (int j = 0; j < m; ++j) {
			if (S[i][j] == 'O') O++;
			else if (S[i][j] == 'X') X++;
			else if (S[i][j] == 'T') T++;
		}
		sum += O + X + T;
		if (O == 4 || O == 3 && T == 1) return 1;
		if (X == 4 || X == 3 && T == 1) return -1;
	}
	for (int j = 0; j < m; ++j) {
		O = 0; X = 0, T = 0;
		for (int i = 0; i < n; ++i) {
			if (S[i][j] == 'O') O++;
			else if (S[i][j] == 'X') X++;
			else if (S[i][j] == 'T') T++;
		}
		if (O == 4 || O == 3 && T == 1) return 1;
		if (X == 4 || X == 3 && T == 1) return -1;
	}
	O = 0, X = 0, T = 0;
	for (int i = 0; i < n; ++i) {
		if (S[i][i] == 'O') O++;
		else if (S[i][i] == 'X') X++;
		else if (S[i][i] == 'T') T++;
	}
	if (O == 4 || O == 3 && T == 1) return 1;
	if (X == 4 || X == 3 && T == 1) return -1;
	O = 0, X = 0, T = 0;
	for (int i = 0; i < n; ++i) {
		if (S[i][n - 1 - i] == 'O') O++;
		else if (S[i][n - 1 - i] == 'X') X++;
		else if (S[i][n - 1 - i] == 'T') T++;
	}
	if (O == 4 || O == 3 && T == 1) return 1;
	if (X == 4 || X == 3 && T == 1) return -1;
	if (sum == n * m) return 0;
	else return 2;
}

int main(void) {
	int cas;
	scanf("%d", &cas);
	for (int T = 1; T <= cas; ++T) {
		for (int i = 0; i < N; ++i) {
			scanf("%s", S[i]);
		}
		printf("Case #%d: ", T);
		int ans = can(N, M);
		if (ans == -1) puts("X won");
		else if (ans == 0) puts("Draw");
		else if (ans == 1) puts("O won");
		else puts("Game has not completed");
	}
	return 0;
}