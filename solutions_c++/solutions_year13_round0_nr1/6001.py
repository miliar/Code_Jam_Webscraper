#include <iostream>
#include <string>
#include <algorithm>
#include <functional>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>

void displayBoard(char** board) {
	for(int i=0; i<4; ++i) {
		for(int j=0; j<4; ++j) {
			std::cout << board[i][j] << " ";
		}
		std::cout << std::endl;
	}
	std::cout << std::endl;
}

bool isWin(char player, char** _board) {
	// ボードコピー & ワイルドカード置換
	char** board = new char*[4];
	for(int i=0; i<4; ++i)	board[i] = new char[4];
	for(int i=0; i<4; ++i) {
		for(int j=0; j<4; ++j)
			board[i][j] = (_board[i][j] == 'T') ? player : _board[i][j];
	}
	
	// 横
	for(int i=0; i<4; ++i) {
		if((board[i][0] == player) && (board[i][1] == player) && (board[i][2] == player) && (board[i][3] == player)) return true;
	}
	
	// 縦
	for(int i=0; i<4; ++i) {
		if((board[0][i] == player) && (board[1][i] == player) && (board[2][i] == player) && (board[3][i] == player)) return true;
	}
	
	// 斜め
	if((board[0][0] == player) && (board[1][1] == player) && (board[2][2] == player) && (board[3][3] == player)) return true;
	if((board[0][3] == player) && (board[1][2] == player) && (board[2][1] == player) && (board[3][0] == player)) return true;
	
	return false;
}

bool isFull(char** board) {
	for(int i=0; i<4; ++i) {
		for(int j=0; j<4; ++j)
			if(board[i][j] == '.') return false;
	}
	
	return true;
}

/******
 * TODO: もし1マス開いてるけど，そこにどっちを入れても引き分けの場合は？
 ******/
int main(int argc, char** argv) {
	unsigned int T;
	std::cin >> T;
	
	for(unsigned int t=0; t<T; ++t) {
		char** board = new char*[4];
		
		for(int i=0; i<4; ++i) {
			board[i] = new char[4];
			for(int j=0; j<4; ++j)	std::cin >> board[i][j];
		}
		
		std::cout << "Case #" << (t+1) << ": ";
		if(isWin('X', board)) std::cout << "X won";
		else if(isWin('O', board)) std::cout << "O won";
		else if(isFull(board)) std::cout << "Draw";
		else std::cout << "Game has not completed";
		std::cout << std::endl;
		
		for(int i=0; i<4; ++i) delete board[i];
		delete board;
	}
	
	return 0;
}
