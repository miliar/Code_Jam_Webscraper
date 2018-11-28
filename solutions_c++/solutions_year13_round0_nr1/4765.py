#include <iostream>
#include <string>
using namespace std;
int main()
{
	char chessBoard[4][5];
	int T;
	cin >> T;
	for(int i = 1; i<= T; ++i)
	{
		for(int j = 0; j< 4; ++j)
		{
			scanf("%s",&chessBoard[j]);
		}
		//for(int j = 0; j< 4; ++j) printf("%s\t",chessBoard[j]);
		//printf("\n");
		int ans = 0;
		int complete = 0;
		for(int m = 0; m < 4; ++m) {
			int X = 0, O = 0, X1 = 0, O1 = 0;
			for(int n = 0; n< 4; ++n){
				if(chessBoard[m][n] == 'O' || chessBoard[m][n] == 'T') O++;
				if(chessBoard[m][n] == 'X' || chessBoard[m][n] == 'T') X++;
				if(chessBoard[n][m] == 'O' || chessBoard[n][m] == 'T') O1++;
				if(chessBoard[n][m] == 'X' || chessBoard[n][m] == 'T') X1++;
				if(chessBoard[m][n] == '.') complete = 1;
			}

			if(O==4 || O1 == 4) {ans = 1;break;}
			if(X==4 || X1 == 4) {ans = 2;break;}
		}
		if(ans == 0) {
			int X = 0, O = 0, X1 = 0, O1 = 0;
			for(int m = 0; m< 4; ++m){
				if(chessBoard[m][m] == 'O' || chessBoard[m][m] == 'T') O++;
				if(chessBoard[m][3-m] == 'O' || chessBoard[m][3-m] == 'T') O1++;
				if(chessBoard[m][m] == 'X' || chessBoard[m][m] == 'T') X++;
				if(chessBoard[m][3-m] == 'X' || chessBoard[m][3-m] == 'T') X1++;
			}
			if(O == 4 || O1 == 4) ans = 1;
			else if(X==4 || X1 == 4) ans = 2;
		}
		if(ans == 1) printf("Case #%d: O won\n",i);
		else if(ans == 2) printf("Case #%d: X won\n",i);
		else if(complete == 1) printf("Case #%d: Game has not completed\n",i);
		else printf("Case #%d: Draw\n",i);
	}
}