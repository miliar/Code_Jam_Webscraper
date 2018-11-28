#include <iostream>

using namespace std;

string gameloop();
void inputboard();
bool haswon(char);
bool checkrows(char);
bool checkcols(char);
bool checkdiags(char);
bool boardfull();

char board[4][4];

int main(){
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		cout << "Case #" << i+1 << ": " << gameloop() << endl;
	}
}

string gameloop(){
	inputboard();
	if(haswon('X')){
		return "X won";
	}
	if(haswon('O')){
		return "O won";
	}
	if(boardfull()){
		return "Draw";
	}
	return "Game has not completed";
}

void inputboard(){
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			cin >> board[i][j];
		}
	}
}

bool haswon(char let){
	return checkrows(let) || checkcols(let) || checkdiags(let);
}

bool checkrows(char let){
	for(int i = 0; i < 4; i++){
		int j;
		for(j = 0; j < 4; j++){
			if(board[i][j] != 'T' && board[i][j] != let)
				break;
		}
		if(j == 4)
			return true;
	}
	return false;
}

bool checkcols(char let){
	for(int i = 0; i < 4; i++){
		int j;
		for(j = 0; i < 4; j++){
			if(board[j][i] != 'T' && board[j][i] != let)
				break;
		}
		if(j == 4)
			return true;
	}
	return false;
}

bool checkdiags(char let){
	bool ltr = true, rtl = true;
	for(int i = 0, j = 0; i < 4 && (ltr || rtl); i++, j++){
		if(board[i][j] != 'T' && board[i][j] != let)
			ltr = false;
		if(board[3-i][j] != 'T' && board[3-i][j] != let)
			rtl = false;
	}
	return ltr || rtl;
}

bool boardfull(){
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(board[i][j] == '.')
				return false;
		}
	}
	return true;
}