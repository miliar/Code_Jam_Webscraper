#include <vector>
#include <string.h>
#include <map>
#include <stdio.h>
#include <iostream>
using namespace std;
bool checkRow(char c, vector<string> board) {
	bool ret = true;
	int ctr;
	for(int i=0; i < 4; i++) {
		ctr = 0;
		for(int j=0; j < 4; j++) {
			if(board[i][j] == 'T' || board[i][j] == c) {
				ctr++;
			} 
		}
		if(ctr == 4) {
			return ret;
		}
	}
	if(ctr != 4) {
		ret = false;
	}
	return ret;
}

bool checkCol(char c, vector<string> board) {
	bool ret = true;
	int ctr;
	for(int i=0; i < 4; i++){
		ctr = 0;
		for(int j=0; j < 4; j++) {
			if(board[j][i] == 'T' || board[j][i] == c) {
				ctr++;
			} 
		}
		if(ctr == 4){
			return ret;
		}
	}
	if(ctr != 4) {
		
		ret = false;
	}
	return ret;
}

bool checkDiagonal(char c, vector<string> board) {
	bool ret = false;
	int ctrr = 0, ctrl = 0;
	for(int i=0; i < 4; i++) {
		for(int j=0; j < 4; j++) {			
			if(i == j && (board[i][j] == 'T' || board[i][j] == c)) {
				ctrr++;
			} 
		}
		for(int k=0; k < 4; k++) {
			if(4-i-1 == (4-k-1) && (board[i][4-k-1] == 'T' || board[i][4-k-1] == c)) {				
				ctrl++;
			} 
		}
	}
	if(ctrr == 4 || ctrl == 4) {
		ret = true;
	}
	return ret;
}

int empty(vector<string> board) {
	int ret = 0;
	for(int i=0; i < 4; i++) {
		for(int j=0; j < 4; j++){
			if(board[i][j] == '.') {
				ret += 1;
			}
		}
	}
	return ret;
}

string process(vector<string> board) {
	string ret = "";
	if(checkRow('X', board) || checkCol('X', board) || checkDiagonal('X', board)) {
		ret = "X won";
	} else if(checkRow('O', board) || checkCol('O', board) || checkDiagonal('O', board)) {
		ret = "O won";
	} else if(!(checkRow('O', board) || checkCol('O', board) || checkDiagonal('O', board)) || !(checkRow('X', board) || checkCol('X', board) || checkDiagonal('X', board)) ) {
		if(empty(board) == 0) {
			ret = "Draw";
		} else {
			ret = "Game has not completed";
		}
	} 	
	return ret;
}

int main() {
	int T;
	scanf("%d", &T);
	vector<string> board;
	string ret;
	int cases = 0;
	while(T--) {
		cases += 1;
		board.clear();
		for(int i = 0; i < 4; i++) {
			string t;
			cin >> t;
			board.push_back(t);
		}
		ret = process(board);
		printf("Case #%d: ", cases);
		cout << ret << endl;
	}
}
