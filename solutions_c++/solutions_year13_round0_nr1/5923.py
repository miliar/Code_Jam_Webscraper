#include <iostream>
#include <string>
#include <stdio.h>
#include <fstream>

using namespace std;

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("output.txt");

	int T, i, j;
	string board[4];

	cin >> T;

	for( i = 0; i < T; ++i )
	{
		for( j = 0; j < 4; ++j ) cin >> board[j];

		if( ((board[0][0] == 'X' || board[0][0] == 'T') && (board[0][1] == 'X' || board[0][1] == 'T') &&
			(board[0][2] == 'X' || board[0][2] == 'T') && (board[0][3] == 'X' || board[0][3] == 'T')) ||
			((board[1][0] == 'X' || board[1][0] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') &&
			(board[1][2] == 'X' || board[1][2] == 'T') && (board[1][3] == 'X' || board[1][3] == 'T')) ||
			((board[2][0] == 'X' || board[2][0] == 'T') && (board[2][1] == 'X' || board[2][1] == 'T') &&
			(board[2][2] == 'X' || board[2][2] == 'T') && (board[2][3] == 'X' || board[2][3] == 'T')) ||
			((board[3][0] == 'X' || board[3][0] == 'T') && (board[3][1] == 'X' || board[3][1] == 'T') &&
			(board[3][2] == 'X' || board[3][2] == 'T') && (board[3][3] == 'X' || board[3][3] == 'T')) ||
			((board[0][0] == 'X' || board[0][0] == 'T') && (board[1][0] == 'X' || board[1][0] == 'T') &&
			(board[2][0] == 'X' || board[2][0] == 'T') && (board[3][0] == 'X' || board[3][0] == 'T')) ||
			((board[0][1] == 'X' || board[0][1] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') &&
			(board[2][1] == 'X' || board[2][1] == 'T') && (board[3][1] == 'X' || board[3][1] == 'T')) ||
			((board[0][2] == 'X' || board[0][2] == 'T') && (board[1][2] == 'X' || board[1][2] == 'T') &&
			(board[2][2] == 'X' || board[2][2] == 'T') && (board[3][2] == 'X' || board[3][2] == 'T')) ||
			((board[0][3] == 'X' || board[0][3] == 'T') && (board[1][3] == 'X' || board[1][3] == 'T') &&
			(board[2][3] == 'X' || board[2][3] == 'T') && (board[3][3] == 'X' || board[3][3] == 'T')) ||
			((board[0][0] == 'X' || board[0][0] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') &&
			(board[2][2] == 'X' || board[2][2] == 'T') && (board[3][3] == 'X' || board[3][3] == 'T')) ||
			((board[3][0] == 'X' || board[3][0] == 'T') && (board[2][1] == 'X' || board[2][1] == 'T') &&
			(board[1][2] == 'X' || board[1][2] == 'T') && (board[0][3] == 'X' || board[0][3] == 'T')))
		{
			cout << "Case #" << i+1 << ": X won";
		}

		else if( ((board[0][0] == 'O' || board[0][0] == 'T') && (board[0][1] == 'O' || board[0][1] == 'T') &&
			(board[0][2] == 'O' || board[0][2] == 'T') && (board[0][3] == 'O' || board[0][3] == 'T')) ||
			((board[1][0] == 'O' || board[1][0] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') &&
			(board[1][2] == 'O' || board[1][2] == 'T') && (board[1][3] == 'O' || board[1][3] == 'T')) ||
			((board[2][0] == 'O' || board[2][0] == 'T') && (board[2][1] == 'O' || board[2][1] == 'T') &&
			(board[2][2] == 'O' || board[2][2] == 'T') && (board[2][3] == 'O' || board[2][3] == 'T')) ||
			((board[3][0] == 'O' || board[3][0] == 'T') && (board[3][1] == 'O' || board[3][1] == 'T') &&
			(board[3][2] == 'O' || board[3][2] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T')) ||
			((board[0][0] == 'O' || board[0][0] == 'T') && (board[1][0] == 'O' || board[1][0] == 'T') &&
			(board[2][0] == 'O' || board[2][0] == 'T') && (board[3][0] == 'O' || board[3][0] == 'T')) ||
			((board[0][1] == 'O' || board[0][1] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') &&
			(board[2][1] == 'O' || board[2][1] == 'T') && (board[3][1] == 'O' || board[3][1] == 'T')) ||
			((board[0][2] == 'O' || board[0][2] == 'T') && (board[1][2] == 'O' || board[1][2] == 'T') &&
			(board[2][2] == 'O' || board[2][2] == 'T') && (board[3][2] == 'O' || board[3][2] == 'T')) ||
			((board[0][3] == 'O' || board[0][3] == 'T') && (board[1][3] == 'O' || board[1][3] == 'T') &&
			(board[2][3] == 'O' || board[2][3] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T')) ||
			((board[0][0] == 'O' || board[0][0] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') &&
			(board[2][2] == 'O' || board[2][2] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T')) ||
			((board[3][0] == 'O' || board[3][0] == 'T') && (board[2][1] == 'O' || board[2][1] == 'T') &&
			(board[1][2] == 'O' || board[1][2] == 'T') && (board[0][3] == 'O' || board[0][3] == 'T')))
		{
			cout << "Case #" << i+1 << ": O won";
		}

		else if( board[0][0] == '.' || board[0][1] == '.' || board[0][2] == '.' || board[0][3] == '.' ||
			board[1][0] == '.' || board[1][1] == '.' || board[1][2] == '.' || board[1][3] == '.' ||
			board[2][0] == '.' || board[2][1] == '.' || board[2][2] == '.' || board[2][3] == '.' ||
			board[3][0] == '.' || board[3][1] == '.' || board[3][2] == '.' || board[3][3] == '.' )
		{
			cout << "Case #" << i+1 << ": Game has not completed";
		}
		
		else
		{
			cout << "Case #" << i+1 << ": Draw";
		}

		if( i != T - 1 ) cout << endl;
	}

	return 0;
}