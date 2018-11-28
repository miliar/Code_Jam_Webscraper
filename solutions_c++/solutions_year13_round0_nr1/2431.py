#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

string prin[] = {"X won", "O won", "Draw", "Game has not completed"};
int t;

int main(){
	scanf(" %d ", &t);
	char board[4][4];
	for(int x = 1; x <= t; x++){
		int ans = 3;
		for(int i = 0; i < 4; i++) scanf(" %s ", board[i]);
		char hor, ver;
		int dots = 0;
		for(int i = 0; i < 4; i++){
			hor = board[i][0];
			ver = board[0][i];
			for(int j = 1; j < 4; j++){
				if(board[i][j] == '.') dots++;
				if(hor == 'T')
					hor = board[i][j];
				if(ver == 'T')
					ver = board[j][i];
				if(hor != 'T' && board[i][j] != 'T' && board[i][j] != hor)
					hor = 'P';
				if(ver != 'T' && board[j][i] != 'T' && board[j][i] != ver)
					ver = 'P';
			}
			if(ver == 'X' || hor == 'X')
				ans = 0;
			else if(ver == 'O' || hor == 'O')
				ans = 1;
		}
		//diagonals
		hor = board[0][0];
		ver = board[0][3];
		for(int i = 1; i < 4; i++){
			if(hor == 'T')
				hor = board[i][i];
			if(ver == 'T')
				ver = board[i][(3-i)];
			if(hor != 'T' && board[i][i] != 'T' && board[i][i] != hor)
				hor = 'P';
			if(ver != 'T' && board[i][(3-i)] != 'T' && board[i][(3-i)] != ver)
				ver = 'P';
		}
		if(ver == 'X' || hor == 'X')
			ans = 0;
		else if(ver == 'O' || hor == 'O')
			ans = 1;
		if(ans == 3 && dots == 0) ans = 2;
		cout << "Case #" << x << ": " << prin[ans] << endl;
	}
	return 0;
}