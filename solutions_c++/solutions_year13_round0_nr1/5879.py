#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

const int WINNER_X = 1;
const int WINNER_0 = 2;
const int DRAW = 0;

int getWiner(vector<char>& row)
{
	char curSmb = 0;
	for (size_t i = 0; i < row.size(); i++)
	{
		if (row[i] == 'T')
		{
			continue;
		}
		if (row[i] == '.' ||
			(curSmb != 0 && curSmb != 'T' && row[i] != curSmb)
			)
		{
			return DRAW;
		}
		curSmb = row[i];
	}
	if (curSmb == 'X')
	{
		return WINNER_X;
	}
	return WINNER_0;
}

int getResult(vector<vector<char>>& board)
{
	//check rows
	for (int row = 0; row < 4; row++)
	{
		int res = getWiner(board[row]);
		if (res != DRAW)
		{
			return res;
		}
	}
	//check cols
	vector<char> diag1;
	vector<char> diag2;
	for (int col = 0; col < 4; col++)
	{
		vector<char> curCol;
		for (int row = 0; row < 4; row++)
		{
			if (col == row)
			{
				diag1.push_back(board[row][col]);
			}
			else if (col + row == 3)
			{
				diag2.push_back(board[row][col]);
			}
			curCol.push_back(board[row][col]);
		}
		int res = getWiner(curCol);
		if (res != DRAW)
		{
			return res;
		}
	}
	int res = getWiner(diag1);
	if (res != DRAW)
	{
		return res;
	}
	res = getWiner(diag2);
	return res;
}

int main(int argc, char* argv[])
{
	ifstream inputFile;
	ofstream outputFile;
	inputFile.open("data.dat");
	outputFile.open("data.res");
	if (inputFile.is_open() && outputFile.is_open())
	{
		int T;
		vector<vector<char>> board;

		inputFile >> T;
		for (int t = 0; t < T; t++)
		{
			bool hasEmpty = false;
			board.clear();
			vector<char> boardRow;
			char curSmb;
			for (int row = 0; row < 4; row++)
			{
				boardRow.clear();
				for (int col = 0; col < 4; col++)
				{
					inputFile >> curSmb;
					if (curSmb == '.')
					{
						hasEmpty = true;
					}
					boardRow.push_back(curSmb);
				}
				board.push_back(boardRow);
			}
			string message;
			switch (getResult(board))
			{
			case WINNER_X: //X won
				message = "X won";
				break;
			case WINNER_0: //O won
				message = "O won";
				break;
			default://draw or incomplete
				if (hasEmpty)
				{
					message = "Game has not completed";
				}
				else
				{
					message = "Draw";
				}

			}
			outputFile << "Case #" << (t + 1) << ": " << message << endl;
		}
	}
	inputFile.close();
	outputFile.close();
	return 0;
}