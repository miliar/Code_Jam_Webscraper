#include <stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <queue>
#include <cstdio>
#include <fstream>

using namespace std;

bool checkHorizontalWins(char board[4][4], char whose){
	for (int i = 0; i < 4; i++)
	{
		if((board[i][0] == whose || board[i][0] == 'T') && (board[i][1] == whose || board[i][1] == 'T') && (board[i][2] == whose || board[i][2] == 'T')
			&& (board[i][3] == whose || board[i][3] == 'T')) return true;
	}
	return false;
}

bool checkVerticalWins(char board[4][4], char whose){
	for (int i = 0; i < 4; i++)
	{
		if((board[0][i] == whose || board[0][i] == 'T') && (board[1][i] == whose || board[1][i] == 'T') && (board[2][i] == whose || board[2][i] == 'T')
			&& (board[3][i] == whose || board[3][i] == 'T')) return true;
	}
	return false;
}

bool checkDiagonalWins(char board[4][4], char whose){
	if(((board[0][0] == whose || board[0][0] == 'T') && (board[1][1] == whose || board[1][1] == 'T') && (board[2][2] == whose || board[2][2] == 'T')
		&& (board[3][3] == whose || board[3][3] == 'T')) || 
		((board[0][3] == whose || board[0][3] == 'T') && (board[1][2] == whose || board[1][2] == 'T') && (board[2][1] == whose || board[2][1] == 'T')
		&& (board[3][0] == whose || board[3][0] == 'T'))){
			return true;
	}
	return false;
}

bool isBoardFull(char board[4][4]){
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if(board[i][j] == '.') return false;
		}
	}

	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	ofstream outputFile("output.txt");
	int input;
	scanf("%d", &input);

	// ignore new line character
	getchar();
	for (int i = 0; i < input; i++)
	{
		// read each board
		char board[4][4];
		for (int i = 0; i < 4; i++)
		{
			string line;
			getline(cin, line);
			board[i][0] = line.at(0);
			board[i][1] = line.at(1);
			board[i][2] = line.at(2);
			board[i][3] = line.at(3);
		}
		// ignore empty line in input file
		string line;
		getline(cin, line);

		// check for horizontal wins for x
		bool xHorizonal = checkHorizontalWins(board, 'X');
		// check for vertical wins for x
		bool xVertical = checkVerticalWins(board, 'X');
		// check for diagonal for x
		bool xDiagonal = checkDiagonalWins(board, 'X');

		// check for horizontal wins for o
		bool yHorizonal = checkHorizontalWins(board, 'O');
		// check for vertical wins for o
		bool yVertical = checkVerticalWins(board, 'O');
		// check for diagonal for o
		bool yDiagonal = checkDiagonalWins(board, 'O');

		if(xHorizonal == true || xVertical == true || xDiagonal == true){
			outputFile << "Case #" << i + 1 <<": X won\n";
		}else if(yHorizonal == true || yVertical == true || yDiagonal == true){
			outputFile << "Case #" << i + 1 <<": O won\n";
		}else if(isBoardFull(board) == true){
			outputFile << "Case #" << i + 1 <<": Draw\n";
		}else{
			outputFile << "Case #" << i + 1 <<": Game has not completed\n";
		}
	}

	outputFile.close();
	return 0;
}