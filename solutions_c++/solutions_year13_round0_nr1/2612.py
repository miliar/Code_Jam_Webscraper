#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

const int StROW[] = {0, 0, 0, 1, 2, 3, 0, 0, 0, 0};
const int StCOL[] = {0, 3, 0, 0, 0, 0, 0, 1, 2, 3};
const int ROWS[]  = {1, 1, 0, 0, 0, 0, 1, 1, 1, 1};
const int COLS[]  = {1,-1, 1, 1, 1, 1, 0, 0, 0, 0};
const int LEN = 10;

int main(){
	freopen("C:\\googlecj\\ticlarge.in", "r", stdin);
	freopen("C:\\googlecj\\ticlarge.out", "w", stdout);
	int tc, caseNum=1, i, j, k, r, c, oC, xC;
	char inp[10], board[5][5];
	bool hasWinner, hasDot, sawT;
	scanf("%d", &tc);
	while( tc-- ){
		for(i=0; i<4; i++){
			scanf("%s", inp);
			for(j=0; j<4; j++)
				board[i][j] = inp[j];
		}

		hasWinner = hasDot = false;
		for(i=0; i<LEN; i++){
			r = StROW[i], c = StCOL[i];
			oC = xC = 0;
			sawT = false;
			for(j=0; j<=4; j++){
				if(board[r][c]=='X')
					xC ++;
				else if(board[r][c] =='O')
					oC ++;
				else if(board[r][c] == '.')
					hasDot = true;
				else if(board[r][c] == 'T')
					sawT = true;
				r += ROWS[i];
				c += COLS[i];
			}

			if(xC==4 || (xC==3 && sawT)){
				hasWinner = true;
				printf("Case #%d: X won\n", caseNum);
				break;
			}else if(oC==4 || (oC==3 && sawT)){
				hasWinner = true;
				printf("Case #%d: O won\n", caseNum);
				break;
			}
		}

		if(!hasDot && !hasWinner)
			printf("Case #%d: Draw\n", caseNum);
		else if(!hasWinner)
			printf("Case #%d: Game has not completed\n", caseNum);
		caseNum ++;
	}

	return 0;
}


