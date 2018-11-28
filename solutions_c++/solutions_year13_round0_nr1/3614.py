// Takemoto.cpp : 定义控制台应用程序的入口点。
//

//Problem
//
//Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.
//
//After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.
//
//Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:
//
//"X won" (the game is over, and X won)
//"O won" (the game is over, and O won)
//"Draw" (the game is over, and it ended in a draw)
//"Game has not completed" (the game is not over yet)
//If there are empty cells, and the game is not over, you should output "Game has not completed", even if the outcome of the game is inevitable.
//Input
//
//The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line.
//
//Output
//
//For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above. Make sure to get the statuses exactly right. When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on.
//
//Limits
//
//The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as described above.
//
//Small dataset
//
//1 ≤ T ≤ 10.
//
//Large dataset
//
//1 ≤ T ≤ 1000.

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

enum GameResult
{
	GR_X,
	GR_O,
	GR_Draw,
	GR_Cont,

	GR_Max
};

GameResult searchResult(char ch0, char ch1, char ch2, char ch3)
{
	char ch[4] = {ch0, ch1, ch2, ch3};
	int nX = 0, nO = 0, nT = 0;
	for (int i = 0; i < 4; ++i)
	{
		switch (ch[i])
		{
		case 'X': ++nX; break;
		case 'O': ++nO; break;
		case 'T': ++nT; break;
		default: break;
		}
	}
	
	GameResult ret = GR_Cont;
	if (nX + nT == 4) ret = GR_X;
	else if (nO + nT == 4) ret = GR_O;
	else if (nX + nO + nT == 4) ret = GR_Draw;
	return ret;
}


int main()
{
	//freopen("..\\A-small.in","r",stdin);
	//freopen("..\\A-small.out","w",stdout);
	freopen("..\\A-large.in","r",stdin);
	freopen("..\\A-large.out","w",stdout);

	int n = 0;
	cin >> n;

	vector<string> strOutput;

	for (int m = 0; m < n; ++m)
	{
		string row[4];
		cin >> row[0];
		cin >> row[1];
		cin >> row[2];
		cin >> row[3];

		vector<GameResult> resultList;

		for (int i = 0; i < 4; ++i)
		{
			GameResult result = searchResult(row[i][0], row[i][1], row[i][2], row[i][3]);
			resultList.push_back(result);
		}

		for (int i = 0; i < 4; ++i)
		{
			GameResult result = searchResult(row[0][i], row[1][i], row[2][i], row[3][i]);
			resultList.push_back(result);
		}

		{
			GameResult result = searchResult(row[0][0], row[1][1], row[2][2], row[3][3]);
			resultList.push_back(result);
		}

		{
			GameResult result = searchResult(row[3][0], row[2][1], row[1][2], row[0][3]);
			resultList.push_back(result);
		}

		string strCase;
		bool bWon = false, bCont = false;
		for (vector<GameResult>::iterator it = resultList.begin(); it != resultList.end(); ++it)
		{
			if (*it == GR_X)
			{
				strCase = "X won";
				bWon = true;
				break;
			}
			else if (*it == GR_O)
			{
				strCase = "O won";
				bWon = true;
				break;
			}
			else if (*it == GR_Cont)
			{
				bCont = true;
			}
		}

		if (!bWon)
		{
			strCase = bCont ? "Game has not completed" : "Draw";
		}

		stringstream ss;
		ss << "Case #" << m + 1 << ": " << strCase;
		strOutput.push_back(ss.str());
	}

	for (vector<string>::iterator it = strOutput.begin(); it != strOutput.end(); ++it)
	{
		cout << *it << endl;
	}

	return 0;
}

