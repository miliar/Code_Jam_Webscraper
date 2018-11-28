#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	scanf("%d", &T);

	char board[5][5];
	int c=1;
	for(;c<=T;c++) {
		memset(board,0,sizeof(board) );
		int dots = 0;
		for(int i=1;i<=4;i++) {
			string line;
			cin >> line;
			for(int j=1;j<=4;j++) {
				board[i][j] = line[j-1];
				if(board[i][j] == '.')
					dots++;
			}
		}

		bool xWin=false;
		bool oWin=false;
		for(int i=1;i<=4;i++) {
			int j=1;
			while( (board[i][j] == 'X' || board[i][j] == 'T') && j<=4) j++;
			if(j==5) {
				xWin=true;
				break;
			}
			
			j=1;
			while( (board[j][i] == 'X' || board[j][i] == 'T') && j<=4) j++;
			if(j==5) {
				xWin=true;
				break;
			}
			
			j=1;
			while( (board[i][j] == 'O' || board[i][j] == 'T') && j<=4) j++;
			if(j==5) {
				oWin=true;
				break;
			}

			j=1;
			while( (board[j][i] == 'O' || board[j][i] == 'T') && j<=4) j++;
			if(j==5) {
				oWin=true;
				break;
			}

		}

		int i=1;
		while(i <=4 && (board[i][i] == 'X' || board[i][i] == 'T') ) i++;
		if(i==5) xWin=true;

		i=1;
		while(i<=4 && (board[i][5-i] =='X' || board[i][5-i]=='T') ) i++;
		if(i==5) xWin=true;

		i=1;
		while(i <=4 && (board[i][i] == 'O' || board[i][i] == 'T') ) i++;
		if(i==5) oWin=true;

		i=1;
		while(i<=4 && (board[i][5-i] =='O' || board[i][5-i]=='T') ) i++;
		if(i==5) oWin=true;
			
		printf("Case \#%d: ", c);

		if(xWin) printf(" X won\n");
		else if(oWin) printf(" O won\n");
		else if(dots == 0) printf(" Draw\n");
		else printf(" Game has not completed\n");
	}


	return 0;
}