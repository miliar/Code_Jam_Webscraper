#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <string.h>
using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi; 
typedef vector<string> vs;

#define PB push_back
const long double PI = 3.1415926535897932384626433832795;

string board[5];

bool verifyWin(int &xcount, int &ocount, int &tcount, string &res)
{
	if (xcount+tcount == 4) {
		res = "X won";
		return true;
	} else if (ocount+tcount == 4) {
		res = "O won";
		return true;
	}
	return false;
}
bool checkDiag(string &res)
{
	int xcount = 0, ocount = 0, tcount = 0;
	for (int i = 0; i < 4; ++i) {
		if (board[i][i] == 'X') ++xcount;
		else if (board[i][i] == 'O') ++ocount;
		else if (board[i][i] == 'T') ++tcount;
	}
	if (verifyWin(xcount, ocount, tcount, res)) return true;
	xcount = 0, ocount = 0, tcount = 0;
	for (int i = 0; i < 4; ++i) {
		if (board[i][3-i] == 'X') ++xcount;
		else if (board[i][3-i] == 'O') ++ocount;
		else if (board[i][3-i] == 'T') ++tcount;
	}
	return verifyWin(xcount, ocount, tcount, res);
}
bool checkCol(string &res)
{
	for (int col = 0; col < 4; ++col) {
		int xcount = 0, ocount = 0, tcount = 0;
		for (int row = 0; row < 4; ++row) {
			if (board[row][col] == 'X') ++xcount;
			else if (board[row][col] == 'O') ++ocount;
			else if (board[row][col] == 'T') ++tcount;
		}
		if (verifyWin(xcount, ocount, tcount, res)) return true;
	}
	return false;
}
bool checkRow(string &res)
{
	for (int row = 0; row < 4; ++row) {
		int xcount = 0, ocount = 0, tcount = 0;
		for (int col = 0; col < 4; ++col) {
			if (board[row][col] == 'X') ++xcount;
			else if (board[row][col] == 'O') ++ocount;
			else if (board[row][col] == 'T') ++tcount;
		}
		if (verifyWin(xcount, ocount, tcount, res)) return true;
	}
	return false;
}
bool incomplete()
{
	for (int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			if (board[i][j] == '.') return true;
	return false;
}
main(int argc, char *argv[])
{
	int tc;
	ifstream myfile;
	myfile.open(argv[1]);
	myfile >> tc;
	for (int i = 1; i <= tc; ++i) {
		getline(myfile, board[0]);
		for (int l1 = 0; l1 < 4; ++l1)
			std::getline(myfile, board[l1]);
		string res = "Game has not completed";
		if (!(checkRow(res) || checkCol(res) || checkDiag(res)))
			if (!incomplete()) res = "Draw";
		cout << "Case #" << i << ": " << res << "\n";
	}
}
