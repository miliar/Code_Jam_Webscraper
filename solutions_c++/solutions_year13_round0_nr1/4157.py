#include <iostream>
using namespace std;

const int dy[4] = {-1, -1, -1,  0};
const int dx[4] = {-1,  0,  1, -1};

char board[4][5];
int lenO[4][5][4];
int lenX[4][5][4];

bool isValid(int y, int x, int d)
{
	y = y + dy[d];
	x = x + dx[d];

	if( y<0 || x<0 || y>=4 || x>=4 )
		return false;
	return true;
}

// 1 : "X won" (the game is over, and X won)
// 2 : "O won" (the game is over, and O won)
// 3 : "Draw" (the game is over, and it ended in a draw)
// 4 : "Game has not completed" (the game is not over yet)
int judgeBoard()
{
	bool isFull = true;

	for(int y=0; y<4; y++) {
		for(int x=0; x<4; x++) {
			if( board[y][x] == '.' )
				isFull = false;

			for(int d=0; d<4; d++) {

				if( !isValid(y, x, d) ) {
					lenO[y][x][d] = 0;
					lenX[y][x][d] = 0;

					if( board[y][x] == 'O' )
						lenO[y][x][d] = 1;
					
					if( board[y][x] == 'X' )
						lenX[y][x][d] = 1;

					if( board[y][x] == 'T' ) {
						lenO[y][x][d] = 1;
						lenX[y][x][d] = 1;
					}

					continue;
				}

				if( board[y][x] == 'O' ) {
					lenX[y][x][d] = 0;
					lenO[y][x][d] = lenO[y+dy[d]][x+dx[d]][d]+1;
				}else if( board[y][x] == 'X' ) {
					lenO[y][x][d] = 0;
					lenX[y][x][d] = lenX[y+dy[d]][x+dx[d]][d]+1;
				}else if ( board[y][x] == 'T' ) {
					lenO[y][x][d] = lenO[y+dy[d]][x+dx[d]][d]+1;
					lenX[y][x][d] = lenX[y+dy[d]][x+dx[d]][d]+1;
				}else {
					lenX[y][x][d] = 0;
					lenO[y][x][d] = 0;
				}

				if( lenO[y][x][d] == 4 ) {
					return 2;
				}
				if( lenX[y][x][d] == 4 ) {
					return 1;
				}
			}

		}
	}

	if( isFull )
		return 3;
	else
		return 4;
}

int main()
{
	int nTests;
	cin>>nTests;

	for(int tc=1; tc<=nTests; tc++) {

		for(int y=0; y<4; y++)
			cin>>board[y];

		int result = judgeBoard();

		cout<<"Case #"<<tc<<": ";
		if( result == 1 )
			cout<<"X won"<<endl;
		else if( result == 2 )
			cout<<"O won"<<endl;
		else if( result == 3 )
			cout<<"Draw"<<endl;
		else
			cout<<"Game has not completed"<<endl;
	}

	return 0;
}