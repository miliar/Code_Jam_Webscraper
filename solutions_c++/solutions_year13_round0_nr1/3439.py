//Use Visual Studio Express 2008 to compile
// cj13.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;
char board[4][4];
unsigned long T;
unsigned long Case;
void getBoard(){
	for( unsigned short i = 0; i < 4; i++ ) {
		for( unsigned short j = 0; j < 4; j++ ) {
			cin >> board[i][j];
		}
	}
}
void printBoard(){
	for( unsigned short i = 0; i < 4; i++ ) {
		for( unsigned short j = 0; j < 4; j++ ) {
			cout << board[i][j] << " ";
		}
		cout << "\n";
	}
}
bool winsRow( unsigned short r ){
	char ch;
	if ( board[r][0] == '.' )
		return false;
	if ( board[r][0] == 'T' )
		ch = board[r][1];
	else
		ch = board[r][0];
	for( unsigned short c = 1; c < 4; c++ ) {
		if ( board[r][c] == '.' ) {
			return false;
		}
		if ( board[r][c] == 'T' ) {
			continue;
		}
		if ( board[r][c] != ch ) {
			return false;
		}
	}
	string res;
	if ( ch == 'X' )
		res = "X won";
	else
		res = "O won";
	cout << "Case #" << Case + 1 << ": " << res << "\n";
	return true;
}
bool winsCol( unsigned short c ){
	char ch;
	if ( board[0][c] == '.' )
		return false;
	if ( board[0][c] == 'T' )
		ch = board[1][c];
	else
		ch = board[0][c];
	for( unsigned short r = 1; r < 4; r++ ) {
		if ( board[r][c] == '.' ) {
			return false;
		}
		if ( board[r][c] == 'T' ) {
			continue;
		}
		if ( board[r][c] != ch ) {
			return false;
		}
	}
	string res;
	if ( ch == 'X' )
		res = "X won";
	else
		res = "O won";
	cout << "Case #" << Case + 1 << ": " << res << "\n";
	return true;
}
bool winsDiagonalL(){
	char ch;
	if ( board[0][0] == '.' )
		return false;
	if ( board[0][0] == 'T' )
		ch = board[1][1];
	else
		ch = board[0][0];
	for( unsigned short d = 1; d < 4; d++ ) {
		if ( board[d][d] == '.' ) {
			return false;
		}
		if ( board[d][d] == 'T' ) {
			continue;
		}
		if ( board[d][d] != ch ) {
			return false;
		}
	}
	string res;
	if ( ch == 'X' )
		res = "X won";
	else
		res = "O won";
	cout << "Case #" << Case + 1 << ": " << res << "\n";
	return true;
}
bool winsDiagonalR(){
	char ch;
	if ( board[3][0] == '.' )
		return false;
	if ( board[3][0] == 'T' )
		ch = board[2][1];
	else
		ch = board[3][0];
	for( unsigned short d = 1; d < 4; d++ ) {
		if ( board[3-d][d] == '.' ) {
			return false;
		}
		if ( board[3-d][d] == 'T' ) {
			continue;
		}
		if ( board[3-d][d] != ch ) {
			return false;
		}
	}
	string res;
	if ( ch == 'X' )
		res = "X won";
	else
		res = "O won";
	cout << "Case #" << Case + 1 << ": " << res << "\n";
	return true;
}
void wins() {
	for( unsigned short i = 0; i < 4; i++ ){
		if ( winsRow(i) )
			return;
		if( winsCol(i) )
			return;
	}
	if( winsDiagonalR() )
		return;
	if ( winsDiagonalL() )
		return;
	bool dots = false;
	for( unsigned short i = 0; i < 4; i++ ){
		for( unsigned short j = 0; j < 4; j++ ){
			if ( board[i][j] == '.' ) {
				dots = true;
				break;
				break;
			}
		}
	}
	if ( dots ) {
		cout << "Case #" << Case + 1 << ": Game has not completed\n";
		return;
	}
	cout << "Case #" << Case + 1 << ": Draw\n";
}
int _tmain(int argc, _TCHAR* argv[])
{
	cin >> T;
	for( Case = 0; Case < T; Case++ ) {
		getBoard();
		//winsRow(0);
		wins();
		//printBoard();
	}
	//system("pause");
	return 0;
}

