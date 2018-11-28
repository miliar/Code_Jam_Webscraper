#include <iostream>
#include <string>
//#include <algorithm>
using namespace std;

void a(){
	bool isCom = true;
	int pos;
	string line;
	char board[4][4] = {0};
	char mark;
	for (int i = 0;i < 4; ++i){
		cin >> line;
		for (int j = 0;j < 4; ++j){
			board[i][j] = line[j];
			if (line[j] == '.')
				isCom = false;
		}
	}
	for (int i = 0;i < 4; ++i){
		mark = board[i][0];
		if (board[i][0] == 'T'){
			mark = board[i][1];
		}
		if (mark == '.'){
			continue;
		}
		int j;
		for (j = 1;j < 4; ++j){
			if (board[i][j] != 'T' && board[i][j] != mark){
				break;
			}
		}
		if (j == 4)
			if (mark == 'O'){
				cout << "O won";
				return;
			} else{
				cout << "X won";
				return;
			}
	}
	for (int i = 0;i < 4; ++i){
		mark = board[0][i];
		if (board[0][i] == 'T'){
			mark = board[1][i];
		}
		if (mark == '.'){
			continue;
		}
		int j;
		for (j = 1;j < 4; ++j){
			if (board[j][i] != 'T' && board[j][i] != mark){
				break;
			}
		}
		if (j == 4)
			if (mark == 'O'){
				cout << "O won";
				return;
			} else{
				cout << "X won";
				return;
			}
	}
	mark = board[0][0];
	for (pos = 1;pos < 4; ++pos){
		if (mark == 'T')
			mark = board[pos][pos];
		else if (mark == '.')
			break;
		else if (mark != board[pos][pos] && board[pos][pos] != 'T')
			break;
	}
	if (pos == 4)
		if (mark == 'O'){
			cout << "O won";
				return;
		} else{
			cout << "X won";
				return;
		}
		
	mark = board[0][3];
	for (pos = 1;pos < 4; ++pos){
		if (mark == 'T')
			mark = board[pos][3-pos];
		else if (mark == '.')
			break;
		else if (mark != board[pos][3-pos] && board[pos][3-pos] != 'T')
			break;
	}
	if (pos == 4)
		if (mark == 'O'){
			cout << "O won";
				return;
		} else{
			cout << "X won";
				return;
		}
	if (isCom)
		cout << "Draw";
	else
		cout << "Game has not completed";
}

int main(void){
	int T;
	cin >> T;
	for (int i = 1;i <= T; ++i){
		cout << "Case #" << i << ": ";
		a();
		cout << endl;
	}
	return 0;
}