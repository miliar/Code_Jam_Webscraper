#include <stdio.h>
#include <cstring>
#include <functional>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <vector>
#include <stack>
#include <map>
#include <cmath>
#include <string>
using namespace std;

int main(){
	string inputValue;
	int cases;
	cin >> inputValue;
	cases = atoi(inputValue.c_str());

	int k = 1;
	char M[4][4];
	while(cases){
		int i,j;
		// Read the input
		for(i = 0; i < 4; i++){
			cin >> inputValue;
			for(j = 0; j < 4; j++){
				M[i][j] = inputValue[j];
			}
		}

		bool winX = false;
		bool winY = false;

		int diag1X = 0;
		int diag1Y = 0;

		int diag2X = 0;
		int diag2Y = 0;

		int playedPos = 0;

		//Process hor, vert, diag
		for(i = 0; i < 4; i++){
			int hcountX = 0;
			int hcountY = 0;

			int vcountX = 0;
			int vcountY = 0;

			for(j = 0; j < 4; j++){
				if(M[i][j] != '.'){
					playedPos++;
				}

				// horizontal
				if(M[i][j] == 'X'){
					hcountX++;
				}else if(M[i][j] == 'O'){
					hcountY++;
				}else if(M[i][j] == 'T'){
					hcountX++;
					hcountY++;
				}

				//vertical
				if(M[j][i] == 'X'){
					vcountX++;
				}else if(M[j][i] == 'O'){
					vcountY++;
				}else if(M[j][i] == 'T'){
					vcountX++;
					vcountY++;
				}

				//diag 1
				if(i == j){
					if(M[i][j] == 'X'){
						diag1X++;
					}else if(M[i][j] == 'O'){
						diag1Y++;
					}else if(M[i][j] == 'T'){
						diag1X++;
						diag1Y++;
					}
				}

				//diag2
				if(i + j == 3){
					if(M[i][j] == 'X'){
						diag2X++;
					}else if(M[i][j] == 'O'){
						diag2Y++;
					}else if(M[i][j] == 'T'){
						diag2X++;
						diag2Y++;
					}
				}
			}

			winX |= (hcountX == 4 || vcountX == 4 || diag1X == 4 || diag2X == 4);
			winY |= (hcountY == 4 || vcountY == 4 || diag1Y == 4 || diag2Y == 4);
		}

		if(winX){
			printf("Case #%d: X won\n", k);
		}else if(winY){
			printf("Case #%d: O won\n", k);
		}else if(playedPos == 16){
			printf("Case #%d: Draw\n", k);
		}else{
			printf("Case #%d: Game has not completed\n", k);
		}

		k++;
		cases--;
	}
	
	return 0;
}