#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

char matrix[6][6];

int main()
{
	int t; scanf("%d",&t);
	for(int k = 1; k <= t; ++k) {
		for(int i = 0; i < 4; ++i)
			scanf("%s",matrix[i]);
		bool X, O, dot, complete = true, valid = false;
		printf("Case #%d: ",k);
		for(int i = 0; i < 4 && !valid; ++i) {
			X = false, O = false, dot = false;
			for(int j = 0; j < 4 && !valid; ++j) {
				switch(matrix[i][j]) {
					case 'X': X = true; break;
					case 'O': O = true; break;
					case '.': dot = true; break;
				}
			}
			if(X && !O && !dot) {
				printf("X won\n");
				valid = true;
			}
			else if(O && !X && !dot) {
				printf("O won\n");
				valid = true;
			}
			else if(dot) complete = false;
			X = false, O = false, dot = false;
			for(int j = 0; j < 4 && !valid; ++j) {
				switch(matrix[j][i]) {
					case 'X': X = true; break;
					case 'O': O = true; break;
					case '.': dot = true; break;
				}
			}
			if(X && !O && !dot) {
				printf("X won\n");
				valid = true;
			}
			else if(O && !X && !dot) {
				printf("O won\n");
				valid = true;
			}
			else if(dot) complete = false;
		}
		X = false, O = false, dot = false;
		for(int i = 0; i < 4 && !valid; ++i) {
			switch(matrix[i][i]) {
				case 'X': X = true; break;
				case 'O': O = true; break;
				case '.': dot = true; break;
			}
		}
		if(X && !O && !dot) {
			printf("X won\n");
			valid = true;
		}
		else if(O && !X && !dot) {
			printf("O won\n");
			valid = true;
		}
		X = false, O = false, dot = false;
		for(int i = 0; i < 4 && !valid; ++i) {
			switch(matrix[i][3 - i]) {
				case 'X': X = true; break;
				case 'O': O = true; break;
				case '.': dot = true; break;
			}
		}
		if(X && !O && !dot) {
			printf("X won\n");
			valid = true;
		}
		else if(O && !X && !dot) {
			printf("O won\n");
			valid = true;
		}
		if(valid) continue;
		if(!complete) printf("Game has not completed\n");
		else printf("Draw\n");
	}
	return 0;
}
