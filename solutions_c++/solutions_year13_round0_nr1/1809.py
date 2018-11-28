#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<cstring>
#include<cmath>
#include<map>
#define _USE_MATH_DEFINES
using namespace std;

int main() {
	int t;
	char mat[5][5];
	char nl[2];
	scanf("%d", &t);
	bool dot = false;
	int xhor[4];
	int xver[4];
	int ohor[4];
	int over[4];
	int outcome;
	for (int i = 0; i < t; i++) {
		outcome = 0;
		dot = false;
		for (int j = 0; j < 4; j++) {
			xhor[j] = 0;
			xver[j] = 0;
			ohor[j] = 0;
			over[j] = 0;
		}
		for (int j = 0; j < 4; j++) {
			scanf("%s", mat[j]);
			if (outcome > 0) {
				continue;
			}
			for (int k = 0; k < 4; k++) {
				switch(mat[j][k]) {
					case 'X':
						xhor[j]++;
						xver[k]++;
						break;
					case 'O':
						ohor[j]++;
						over[k]++;
						break;
					case '.':
						dot = true;
						break;
					case 'T':
						xhor[j]++;
						xver[k]++;
						ohor[j]++;
						over[k]++;
						break;
					default:
						break;
				}
			}
		}
		for (int j = 0; j < 4; j++) {
			if (xhor[j] == 4) {
				outcome = 1;
				break;
			}
			if (ohor[j] == 4) {
				outcome = 2;
				break;
			}
		}
		if (outcome == 0) {
			for (int j = 0; j < 4; j++) {
				if (xver[j] == 4) {
					outcome = 1;
					break;
				}
				if (over[j] == 4) {
					outcome = 2;
					break;
				}
			}
		}
		if (outcome == 0) {
			bool found = true;
			for (int i = 0; i < 4; i++) {
				if ((mat[i][i] == '.') || (mat[i][i] == 'O')) {
					found = false;
					break;
				}
			}
			if (found) {
				outcome = 1;
			}
			else {
				found = true;
				for (int i = 0; i < 4; i++) {
					if ((mat[i][3-i] == '.') || (mat[i][3-i] == 'O')) {
						found = false;
						break;
					}
				}
				if (found) {
					outcome = 1;
				}
				else {
					bool found = true;
					for (int i = 0; i < 4; i++) {
						if ((mat[i][i] == '.') || (mat[i][i] == 'X')) {
							found = false;
							break;
						}
					}
					if (found) {
						outcome = 2;
					}
					else {
						found = true;
						for (int i = 0; i < 4; i++) {
							if ((mat[i][3-i] == '.') || (mat[i][3-i] == 'X')) {
								found = false;
								break;
							}
						}
						if (found) {
							outcome = 2;
						}
					}
				}
			}
		}
		if (outcome == 0) {
			if (dot) {
				outcome = 4;
			}
			else {
				outcome = 3;
			}
		}
		//scanf("%s", nl);
///////////////
/*		for (int j = 0; j < 4; j++) {
			printf("%s\n", mat[j]);
		}
		for (int j = 0; j < 4; j++) {
			printf("xhor %d : %d\n", j, xhor[j]);
			printf("xver %d : %d\n", j, xver[j]);
			printf("ohor %d : %d\n", j, ohor[j]);
			printf("over %d : %d\n", j, over[j]);
		}

*/
///////////////
		printf("Case #%d: ", i+1);
		switch(outcome) {
			case 1:
				printf("X won\n");
				break;
			case 2:
				printf("O won\n");
				break;
			case 3:
				printf("Draw\n");
				break;
			case 4:
				printf("Game has not completed\n");
				break;
			default:
				break;
		}
	}
	return 0;
}
