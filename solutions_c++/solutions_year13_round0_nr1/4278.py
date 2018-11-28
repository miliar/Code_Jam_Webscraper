#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

string ProcessBoard(vector<string> & board);
int ConvertToInteger(char ch);

int main()
{
	ifstream infile("A-large.in");
	//ifstream infile("ProblemAInput.txt");
	ofstream outfile("ProblemAOutputLarge.txt");

	int T;
	infile >> T;

	vector<string> board(4);
	for (int i = 0; i < T; i++) {
		for (int j = 0; j < 4; j++)
			infile >> board[j];
		outfile << "Case #" << (i+1) << ": " << ProcessBoard(board) << endl;
	}

	return 0;
}

string ProcessBoard(vector<string> & board)
{
	vector<int> rowSums(4);
	vector<int> colSums(4);
	vector<int> diagSums(2);
	
	bool all_positive = true;
	for (int i = 0; i < 4; i++) {
		rowSums[i] = ConvertToInteger(board[i][0]) + ConvertToInteger(board[i][1]) + ConvertToInteger(board[i][2]) + ConvertToInteger(board[i][3]);
		colSums[i] = ConvertToInteger(board[0][i]) + ConvertToInteger(board[1][i]) + ConvertToInteger(board[2][i]) + ConvertToInteger(board[3][i]);
		if (rowSums[i] < 0 || colSums[i] < 0)
			all_positive = false;
	}
	for (int i = 0; i < 4; i++) {
		diagSums[0] += ConvertToInteger(board[i][i]);
		diagSums[1] += ConvertToInteger(board[i][3-i]);
	}
	if (diagSums[0] < 0 || diagSums[1] < 0)
		all_positive = false;

	for (int i = 0; i < 4; i++) {
		if (rowSums[i] >= 7 || colSums[i] >= 7)
			return "X won";
		else if (rowSums[i] == 1 || rowSums[i] == 0 || colSums[i] == 1 || colSums[i] == 0)
			return "O won";
	}
	if (diagSums[0] >= 7 || diagSums[1] >= 7)
		return "X won";
	else if (diagSums[0] == 0 || diagSums[0] == 1 || diagSums[1] == 0 || diagSums[1] == 1)
		return "O won";

	if (all_positive)
		return "Draw";
	else
		return "Game has not completed";
}

int ConvertToInteger(char ch)
{
	if (ch=='X')
		return 2;
	else if (ch=='O')
		return 0;
	else if (ch=='T')
		return 1;
	else
		return -10;
}