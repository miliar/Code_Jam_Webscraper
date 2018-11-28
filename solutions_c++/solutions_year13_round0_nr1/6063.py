//============================================================================
// Name        : Tic-Tac-Toe-Tomek.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

void printState(string gameState[4]){
	for(int i = 0; i <= 3; i++){
		cout << gameState[i] << endl;
	}
}

bool testRows(string gameState[4], char in){
	bool res = true;
	for(int i = 0; i <= 3; i++){
		//check each row
		res = true;
		for(int j = 0; j <= 3; j++){
			if(gameState[i][j] != in && gameState[i][j] != 'T'){
				//this row is not the answer
				res = false;
				break;
			}
			//cout << gameState[i][j] << endl;
		}
		if(res){
			//we found the answer for user in
			break;
		}
	}

	return res;
}

bool testCols(string gameState[4], char in){
	bool res = true;
	for(int j = 0; j <= 3; j++){
		//check each column
		res = true;
		for(int i = 0; i <= 3; i++){
			if(gameState[i][j] != in && gameState[i][j] != 'T'){
				//this col is not the answer
				res = false;
				break;
			}
			//cout << gameState[i][j] << endl;
		}
		if(res){
			//we found the answer for user in
			break;
		}
	}

	return res;
}

bool testDiag1(string gameState[4], char in){
	bool res = true;
	for(int i = 0; i <= 3; i++){
		//check the diagonal members
		//cout << gameState[i][i] << endl;
		if(gameState[i][i] != in && gameState[i][i] != 'T'){
			//this diagonal is not the answer for in
			res = false;
			break;
		}
	}

	return res;
}

bool testDiag2(string gameState[4], char in){
	bool res = true;
	for(int i = 0; i <= 3; i++){
		//check the diagonal
		if(gameState[i][3 - i] != in && gameState[i][3 - i] != 'T'){
			//this diag is not the answer
			res = false;
			break;
		}
	}

	return res;
}

//all squares are filled --> 'X', 'O', 'T' and nobody won
bool isDraw(string gameState[4]){
	bool res= true;
	for(int i = 0; i <= 3; i++){
		for(int j = 0; j <= 3; j++){
			if(gameState[i][j] == '.'){
				//board is not completed yet
				res = false;
				break;
			}
		}
		if(res == false){
			//board is not filled
			break;
		}
	}

	return res;
}

int main() {
	bool DEBUG = false;
	std::string in;
	int cases;
	cin >> cases;
	//cout << "no of cases: " << cases << endl;
	int i = 0;
	int cnt = 1;
	string gameState[4];
	while(cin >> in){
		//read one row
		gameState[i] = in;
		//cout << in << endl;
		i++;
		//check if we have read one game completely
		if(i % 4 == 0){
			//test the state for rows
			if(testRows(gameState, 'X')){
				if(DEBUG){
					cout << "row" << endl;
				}
				cout << "Case #" << cnt << ": X won" << endl;
			}else if(testRows(gameState, 'O')){
				if(DEBUG){
					cout << "row" << endl;
				}
				cout << "Case #" << cnt << ": O won" << endl;
			}else if(testCols(gameState, 'X')){
				if(DEBUG){
					cout << "col" << endl;
				}
				cout << "Case #" << cnt << ": X won" << endl;
			}else if(testCols(gameState, 'O')){
				if(DEBUG){
					cout << "col" << endl;
				}
				cout << "Case #" << cnt << ": O won" << endl;
			}else if(testDiag1(gameState, 'X')){
				if(DEBUG){
					cout << "diag1" << endl;
				}
				cout << "Case #" << cnt << ": X won" << endl;
			}else if(testDiag1(gameState, 'O')){
				if(DEBUG){
					cout << "diag1" << endl;
				}
				cout << "Case #" << cnt << ": O won" << endl;
			}else if(testDiag2(gameState, 'X')){
				if(DEBUG){
					cout << "diag2" << endl;
				}
				cout << "Case #" << cnt << ": X won" << endl;
			}else if(testDiag2(gameState, 'O')){
				if(DEBUG){
					cout << "diag2" << endl;
				}
				cout << "Case #" << cnt << ": O won" << endl;
			}else if(isDraw(gameState)){
				cout << "Case #" << cnt << ": Draw" << endl;
			}else{
				cout << "Case #" << cnt << ": Game has not completed" << endl;
			}
			i = 0;
			cnt++;
			if(false){
				printState(gameState);
			}
		}

	}

	return 0;
}
