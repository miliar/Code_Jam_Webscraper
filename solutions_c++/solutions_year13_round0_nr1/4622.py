#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

void solve(void){
	bool xwon = false, owon= false, emptycells=false;
	int board[4][4];
	string s;
	for (int k = 0; k < 4; ++k){
		cin >> s;
		for (int i = 0; i < 4; ++i){
			if (s[i] == 'X') board[k][i]=50;
			else if (s[i]=='O') board[k][i]=400;
			else if (s[i]=='.') { board[k][i]=0; emptycells=true;}
			else if (s[i]=='T') board[k][i]=1;
			
		}
	}
	// rows
	for (int k = 0; k < 4; ++k){
		int sum=0;
		for (int i = 0; i < 4; ++i){
			sum+=board[k][i];
		}
		if (sum == 200 || sum==151) xwon=true;
		if (sum == 1600 || sum ==1201) owon=true;
	}
	// columns
	for (int k = 0; k < 4; ++k){
		int sum=0;
		for (int i = 0; i < 4; ++i){
			sum+=board[i][k];
		}
		if (sum == 200 || sum==151) xwon=true;
		if (sum == 1600 || sum ==1201) owon=true;
	}
	//diagonals
	int sum = board[0][0]+board[1][1]+board[2][2] + board[3][3];
	if (sum == 200 || sum==151) xwon=true;
	if (sum == 1600 || sum ==1201) owon=true;
	sum = board[0][3] + board[1][2] + board[2][1] + board[3][0];
	if (sum == 200 || sum==151) xwon=true;
	if (sum == 1600 || sum ==1201) owon=true;

	if ( xwon) cout << "X won";
	else if (owon) cout << "O won";
	else if (emptycells) cout << "Game has not completed";
	else cout << "Draw";

}

int main(void){
	int n;
	cin >> n;
	for (int k=0;k<n;++k){
		cout << "Case #"<<k+1<<": ";
		solve();
		cout << endl;
	}

	return 0;
}