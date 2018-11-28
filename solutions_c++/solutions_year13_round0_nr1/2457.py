#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int i,j,k,nonEmpty,t;
string board[4];

int check(){
	int couX,couO,i,j;

	for(i=0; i<4; ++i){
		couX=couO=0;
		for(j=0; j<4; ++j)
			if(board[i][j]=='X' || board[i][j]=='T') ++couX;
			else
				if(board[i][j]=='O' || board[i][j]=='T') ++couO;
		if(couX==4) return 1;
		if(couO==4) return 2;	
	}

	for(i=0; i<4; ++i){
		couX=couO=0;
		for(j=0; j<4; ++j)
			if(board[j][i]=='X' || board[j][i]=='T') ++couX;
			else
				if(board[j][i]=='O' || board[j][i]=='T') ++couO;
		if(couX==4) return 1;
		if(couO==4) return 2;	
	}

	couX=couO=0;
	for(i=0; i<4; ++i){
		if(board[i][i]=='X' || board[i][i]=='T') ++couX;
		if(board[i][i]=='O' || board[i][i]=='T') ++couO;
	}

	if(couX==4) return 1;
	if(couO==4) return 2;

	couX=couO=0;
	for(i=0; i<4; ++i){
		if(board[i][3-i]=='X' || board[i][3-i]=='T') ++couX;
		if(board[i][3-i]=='O' || board[i][3-i]=='T') ++couO;
	}


	if(couX==4) return 1;
	if(couO==4) return 2;
	return 0;
}

int main(){
	cin >> t;
	for(k=1; k<=t; ++k){
		cout << "Case #" << k << ": ";
		nonEmpty=0;

		for(i=0; i<4; ++i){
			cin >> board[i];
			for(j=0; j<4; ++j){
				if(board[i][j]!='.') ++nonEmpty;
			}
		}
		
		int r=check();
		if(r==1) cout << "X won" << endl;
		else
			if(r==2) cout << "O won" << endl;
			else
				if(r==0 && nonEmpty==16) cout << "Draw" << endl;
				else
					cout << "Game has not completed" << endl;
	}
	return 0;
}
