#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <cstring>
#include <set>
#include <sstream>
#include <cstdlib>
using namespace std;

char CheckRowStatus(string x);
string CheckBoardStatus(string board[]);

int main()
{
	ifstream fin;
	fin.open ("input.txt");

	ofstream fout;
	fout.open ("output.txt");

	int N; // num test cases
	fin >> N;
	for( int n = 0; n < N; n++ ) {
		string ttt[4];
		fin >> ttt[0];
		fin >> ttt[1];
		fin >> ttt[2];
		fin >> ttt[3];

		string sResult = CheckBoardStatus(ttt);
		cout << "Case #" << n+1 << ": " << sResult << endl;
		fout << "Case #" << n+1 << ": " << sResult << endl;
	}
	string x;
	cin >> x;
	return 0;
}

char CheckRowStatus(string x)
{
	bool xwin = true;
	bool owin = true;
	bool hasempty = false;
	for(int i = 0; i < x.length(); i++)
	{
		switch(x[i])
		{
			case 'X':
				owin = false;
				break;
			case 'O':
				xwin = false;
				break;
			case '.':
				owin = xwin = false;
				hasempty = true;
				break;
			case 'T': // nothing
				break;
		}
	}
	if (xwin) {
		return 'X';
	}
	if (owin)
		return 'O';
	if (hasempty)
		return '.';
	return 'D';
}


string CheckBoardStatus(string board[])
{
	bool xwin = false;
	bool owin = false;
	bool empty = false;
	char ch = CheckRowStatus(board[0]);
	if (ch == 'X')
		return "X won";
	if (ch == 'O')
		return "O won";
	if (ch == '.')
		empty = true;
	
	ch = CheckRowStatus(board[1]);
	if (ch == 'X')
		return "X won";
	if (ch == 'O')
		return "O won";
	if (ch == '.')
		empty = true;
	
	ch = CheckRowStatus(board[2]);
	if (ch == 'X')
		return "X won";
	if (ch == 'O')
		return "O won";
	if (ch == '.')
		empty = true;
	
	ch = CheckRowStatus(board[3]);
	if (ch == 'X')
		return "X won";
	if (ch == 'O')
		return "O won";
	if (ch == '.')
		empty = true;

	string sTest = "";
	sTest += board[0][0];
	sTest += board[1][0];
	sTest += board[2][0];
	sTest += board[3][0];

	ch = CheckRowStatus(sTest);
	if (ch == 'X')
		return "X won";
	if (ch == 'O')
		return "O won";
	if (ch == '.')
		empty = true;

	sTest = "";
	sTest += board[0][1];
	sTest += board[1][1];
	sTest += board[2][1];
	sTest += board[3][1];
	ch = CheckRowStatus(sTest);
	if (ch == 'X')
		return "X won";
	if (ch == 'O')
		return "O won";
	if (ch == '.')
		empty = true;

	sTest = "";
	sTest += board[0][2];
	sTest += board[1][2];
	sTest += board[2][2];
	sTest += board[3][2];
	ch = CheckRowStatus(sTest);
	if (ch == 'X')
		return "X won";
	if (ch == 'O')
		return "O won";
	if (ch == '.')
		empty = true;

	sTest = "";
	sTest += board[0][3];
	sTest += board[1][3];
	sTest += board[2][3];
	sTest += board[3][3];
	ch = CheckRowStatus(sTest);
	if (ch == 'X')
		return "X won";
	if (ch == 'O')
		return "O won";
	if (ch == '.')
		empty = true;

	sTest = "";
	sTest += board[0][0];
	sTest += board[1][1];
	sTest += board[2][2];
	sTest += board[3][3];
	ch = CheckRowStatus(sTest);
	if (ch == 'X')
		return "X won";
	if (ch == 'O')
		return "O won";
	if (ch == '.')
		empty = true;

	sTest = "";
	sTest += board[0][3];
	sTest += board[1][2];
	sTest += board[2][1];
	sTest += board[3][0];
	ch = CheckRowStatus(sTest);
	if (ch == 'X')
		return "X won";
	if (ch == 'O')
		return "O won";
	if (ch == '.')
		empty = true;

	if (empty)
		return "Game has not completed";

	return "Draw";
}