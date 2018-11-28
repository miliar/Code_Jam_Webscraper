// GoogleCodeJam2013QualifiersA.cpp : Defines the entry point for the console application.
//


// This code was written in Visual Studio 2012 for Desktop but compiled using GCC 4.7.2
// using the command line flag -std=c++11


//#include "stdafx.h"
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string outcomes[] = { "X won", "O won", "Draw", "Game has not completed" };

inline string checkBoard(const vector<string>& board) {
	bool GameFinished = true;
	bool xWon = false;

	// check columns
	for (int k = 0; k < 4; ++k) {
		// debug
		//std::cout << "Checking column: " << (k + 1) << endl;

		if ('.' != board[0][k] && '.' != board[1][k]) {
			char toReplicate = ('T' == board[0][k]) ? board[1][k] : board[0][k];
			bool isThereAWinnerP = true;

			for (int j = 1; j < 4; ++j) {
				if (toReplicate != board[j][k] && 'T' != board[j][k]) {
					isThereAWinnerP = false;
					break;
				}
			}

			if (isThereAWinnerP) {
				if ('X' == toReplicate) {
					return outcomes[0];
				} else {
					return outcomes[1];
				}
			}
		}
	}

	// check rows
	for (int j = 0; j < 4; ++j) {
		// debug
		//cout << "Checking row: " << (j + 1) << endl;

		if ('.' != board[j][0] && '.' != board[j][1]) {
			char toReplicate = ('T' == board[j][0]) ? board[j][1] : board[j][0];

			// debug
			//cout << toReplicate << endl;

			bool isThereAWinnerP = true;

			for (int k = 1; k < 4; ++k) {
				if (toReplicate != board[j][k] && 'T' != board[j][k]) {
					isThereAWinnerP = false;
					break;
				} 

				// debug
				/*else 
				{
					cout << (j + 1) << " " << (k + 1) << " " << board[j][k] << endl;
				}*/
			}

			if (isThereAWinnerP) {
				if ('X' == toReplicate) {
					return outcomes[0];
				} else {
					return outcomes[1];
				}
			}
		}
	}

	// check diagonals: d1 starts at top-left, d2 starts at top-right
	{


		bool isThereAWinnerP = true;

		// debug
		//cout << "Checking diagonal: " << 1 << endl;

		if ('.' != board[0][0] && '.' != board[1][1]) {
			char toReplicateD1 = ('T' == board[0][0]) ? board[1][1] : board[0][0];

			// check d1
			for (int z = 1; z < 4; ++z) {
				if (toReplicateD1 != board[z][z]  && 'T' != board[z][z]) {
					isThereAWinnerP = false;
					break;
				}
			}

			if (isThereAWinnerP) {
				if ('X' == toReplicateD1) {
					return outcomes[0];
				} else {
					return outcomes[1];
				}
			}
		}

		isThereAWinnerP = true;

		// debug
		// cout << "Checking diagonal: " << 2 << endl;

		if ('.' != board[0][3] && '.' != board[1][2]) {
			char toReplicateD2 = ('T' == board[0][3]) ? board[1][2] : board[0][3];
			// check d2
			for (int z = 1; z < 4; ++z) {
				if (toReplicateD2 != board[z][3 - z] && 'T' != board[z][3 - z]) {
					isThereAWinnerP = false;
					break;
				}
			}

			if (isThereAWinnerP) {
				if ('X' == toReplicateD2) {
					return outcomes[0];
				} else {
					return outcomes[1];
				}
			}
		}
	}

	// debug
	//cout << "Checking if game was finished." << endl;
	
  for (int j = 0; j < 4; ++j) {
    for (int k = 0; k < 4; ++k) {
      if ('.' == board[j][k]) {
        GameFinished = false;

        // debug
        // cout << "Disovered game was not finished on row: " << (j + 1) << " and column: " << (k + 1) << endl;
      }
    }
  }

	if (GameFinished) {
		return outcomes[2];
	} else {
		return outcomes[3];
	}
}

int main()
{
	ios::sync_with_stdio(0);
	//#pragma warning(disable : 4996)
	freopen("A-large.in", "r", stdin);
	//#pragma warning(disable : 4996)
	freopen("a.out", "w", stdout);

	int numberOfTestCases;
	cin >> numberOfTestCases;
	cin.ignore(1);

	vector<string> ticTacToeBoardHolder;

	for (int i = 0; i < numberOfTestCases; ++i)
	{
		for (int j = 0; j < 4; ++j) {
			string s;
			getline(cin, s);

			ticTacToeBoardHolder.push_back(s);

			//cout << ticTacToeBoardHolder[j] << endl;
		}

		cout << "Case #" << (i + 1) << ": " << checkBoard(ticTacToeBoardHolder) << endl;
		cin.ignore(1);

		ticTacToeBoardHolder.clear();
	}

	return 0;
}
