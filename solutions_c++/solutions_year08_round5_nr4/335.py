#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int H, W, R;
int board[200][200];

int count() {
	board[1][1] = 1;
	for(int i=1; i<=H; i++)
		for(int j=1; j<=W; j++) {
			if(board[i][j] == -1)
				continue;
			int i1=i-2, j1=j-1;
			if(i1>=1 && j1>=1 && board[i1][j1]!=-1)
				board[i][j] += board[i1][j1];
			i1=i-1, j1=j-2;
			if(i1>=1 && j1>=1 && board[i1][j1]!=-1)
				board[i][j] += board[i1][j1];
			board[i][j] = board[i][j] % 10007;
		}
	return board[H][W];
}

int main(int argc, char* argv[]) {
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		cin >>H >>W >>R;
		memset(board, 0, sizeof(board));
		for(int j=0; j<R; j++) {
			int r, c;
			cin >>r >>c;
			board[r][c] = -1;
		}
		cout <<"Case #" <<i+1 <<": " <<count() <<endl;
	}
}

/*
d:\Documents\Visual Studio 2008\Projects\GoogleCodeJam\Debug\
*/