/*
 * main.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: michael
 */
#include <iostream>
#include <stdio.h>

using namespace std;

const char *response[] = {"Game has not completed","Draw","X won","O won"};

bool checkRow (const char board[4][5], const int row, const char player){
	for (int i=0; i<4; i++){
		if (board[row][i] != player && board[row][i] != 'T')
			return false;
	}
	return true;
}

bool checkCol (const char board[4][5], const int col, const char player){
	for (int i=0; i<4; i++){
		if (board[i][col] != 'T' && board[i][col] != player){
			return false;
		}
	}
	return true;
}

bool checkDiags (const char board[4][5], const char player){
	bool status = true;
	for (int i=0; i<4; i++){
		if (board[i][i] != 'T' && board[i][i] != player){
			status = false;
			break;
		}
	}
	if (status){
		return status;
	}
	status = true;
	for (int i=0; i<4; i++){
		if (board[3-i][i] != 'T' && board[3-i][i] != player){
			status = false;
			break;
		}
	}

	return status;
}

bool checkEmpties (const char board[4][5]){
	for (int i=0; i<4; i++){
		for (int j=0; j<4; j++){
			if (board[i][j] == '.'){
				return true;
			}
		}
	}
	return false;
}

int readGame (const char board[4][5]){
	/* Status list:
	 * 0 = game not complete
	 * 1 = game draw
	 * 2 = X win
	 * 3 = O win
	 */
	int status = 0;
	if (checkDiags(board, 'O')){
		status = 3;
	} else {
		for (int i = 0; i < 4; i++) {
			if (checkRow(board, i, 'O') || checkCol(board, i, 'O')) {
				status = 3;
				break;
			}
		}
	}
	if (status){
		return status;
	}
	if (checkDiags(board, 'X')){
		status = 2;
	} else {
		for (int i=0; i<4; i++){
			if (checkRow(board, i, 'X') || checkCol(board, i, 'X')){
				status = 2;
				break;
			}
		}
	}
	if (status){
		return status;
	}
	if (!checkEmpties(board)){
		status = 1;
		return status;
	}
	return status;
}

int main(){
	char buffer[6];
	int numCases;

	cin.getline(buffer, 6);
	sscanf(buffer, "%d", &numCases);
	for(int i=0; i<numCases; i++){
		char board[4][5];
		cin.getline(board[0],5);
		cin.getline(board[1],5);
		cin.getline(board[2],5);
		cin.getline(board[3],5);
		cin.getline(buffer,6);
		int status = readGame(board);
		printf("Case #%i: %s\n",i+1,response[status]);
	}


	return 0;
}



