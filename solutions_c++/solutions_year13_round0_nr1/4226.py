#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;


char* board(){
	char board[4][4];
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			cin >> board[i][j];
		}
	}

	bool empty = false;

	for(int i=0; i<4; i++){
		char temp;
		if(board[i][0] == '.' || board[i][1] == '.' || board[i][2] == '.'|| board[i][3] == '.'){
			empty = true;
		}else{
			int count = 0;
			temp = (board[i][0] == 'T')?board[i][1]:board[i][0];
			for(int j=0; j<4; j++){
				if(board[i][j] == temp || board[i][j] == 'T'){
					count++;
				}
			}
			if(count == 4){
				if(temp == 'O'){
					return "O won";
				}else{
					return "X won";
				}
			}
		}

		if(board[0][i] == '.' || board[1][i] == '.' || board[2][i] == '.'|| board[3][i] == '.'){
			empty = true;
		}else{
			int count = 0;
			temp = (board[0][i] == 'T')?board[1][i]:board[0][i];
			for(int j=0; j<4; j++){
				if(board[j][i] == temp || board[j][i] == 'T'){
					count++;
				}
			}
			if(count == 4){
				if(temp == 'O'){
					return "O won";
				}else{
					return "X won";
				}
			}
		}
	}

	char temp;
	if(board[0][0] == '.' || board[1][1] == '.' || board[2][2] == '.'|| board[3][3] == '.'){
		empty = true;
	}else{
		int count = 0;
		temp = (board[0][0] == 'T')?board[1][1]:board[0][0];
		for(int i=0; i<4; i++){
			if(board[i][i] == temp || board[i][i] == 'T'){
				count++;
			}
		}
		if(count == 4){
			if(temp == 'O'){
				return "O won";
			}else{
				return "X won";
			}
		}
	}
	if(board[0][3] == '.' || board[1][2] == '.' || board[2][1] == '.'|| board[3][0] == '.'){
		empty = true;
	}else{
		int count = 0;
		temp = (board[0][3] == 'T')?board[1][2]:board[0][3];
		for(int i=0; i<4; i++){
			if(board[i][3-i] == temp || board[i][3-i] == 'T'){
				count++;
			}
		}
		if(count == 4){
			if(temp == 'O'){
				return "O won";
			}else{
				return "X won";
			}
		}
	}

	if(empty){
		return "Game has not completed";
	}
	else{
		return "Draw";
	}
}

int main(){
	ifstream input("A-large.in");
	cin.rdbuf(input.rdbuf());

	ofstream output("out.txt");
	cout.rdbuf(output.rdbuf());
	
	int T;
	cin >> T;

	for(int i=0; i<T; i++){
		cout << "Case #" << i+1 << ": " << board() << endl;
	}
	
	return 0;
}