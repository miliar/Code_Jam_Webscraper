#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

char checkWin(vector<vector<char> > &board){
	int findD1 = true, findD2 = true;
	for(int m=0; m< 4; m++){
		bool findH = true, findV = true;
		for(int n=0; n<4; n++){
//			if(board[m][n] == '.')	break;
			if((board[m][n]!= board[m][0] && board[m][n]!= 'T')||board[m][n] == '.'){
				findH = false;
			}

//			if(board[n][m] == '.')	break;
			if((board[n][m]!= board[0][m] && board[n][m]!= 'T')||board[n][m] == '.'){
				findV = false;
			}
		}
		if(findH){
//			cout << 1;
			if(board[m][0] != 'T')
				return board[m][0];
			else
				return board[m][1];
		}
		else if(findV){
//			cout << 2;
			if(board[0][m] != 'T')
				return board[0][m];
			else
				return board[1][m];
		}
//		if(board[m][m] == '.' )	break;
		if( (board[m][m]!= board[0][0] && board[m][m]!= 'T') ||board[m][m] == '.'){
			findD1 = false;
		}

//		if(board[m][3-m] =='.' )	break;
		if((board[m][3-m]!= board[0][3] && board[m][3-m]!= 'T') ||board[m][3-m] =='.' ){
			findD2 = false;
		}
	}

	if(findD1){
//		cout << 3;
		if(board[0][0] != 'T')
			return board[0][0];
		else
			return board[1][1];
	}
	else if(findD2){
//		cout << 4;
		if(board[0][3] != 'T')
			return board[0][3];
		else
			return board[1][2];
	}
	else
		return 'N';

}


int main(){
	int N;
	cin >> N;

	for(int i=1; i<=N; i++){
		vector<vector<char> > board(4, vector<char>(4));
		bool finish = true;
		for(int m=0; m< 4; m++){
			for(int n=0; n<4; n++){
				char tmp;
				cin >> tmp;
				if(tmp == '.')	finish = false;
				board[m][n] = tmp;
			}
		}

		char c = checkWin(board);
		switch (c){
		case 'X':
			cout << "Case #" << i<<": X won\n";
			break;
		case 'O':
			cout << "Case #" << i<<": O won\n";
			break;
		case 'N':
			if(finish)
				cout << "Case #" << i<<": Draw\n";
			else
				cout << "Case #" << i<<": Game has not completed\n";
			break;
		}
	}



}
