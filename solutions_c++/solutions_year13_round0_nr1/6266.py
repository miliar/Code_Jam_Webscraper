#include <memory>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <set>
#include <algorithm>

typedef std::vector< std::string > Board;

void solveCase(std::ifstream& in, std::ofstream& out)
{
	using namespace std;
	string line;
	Board board;

	for (int i = 0; i < 4; i++) {
		in >> line;
		board.push_back(line);
		//cout << endl;
	}


	bool xWin = false, oWin = false, hasDot = false;
	//check line
	for (int i = 0; i < 4; i++) {
		int x = 0,o = 0,t = 0;
		for (int j = 0; j < 4; j++) {
			if (board[i][j] == 'X')x++;
			if (board[i][j] == 'O')o++;
			if (board[i][j] == 'T')t++;
			if (board[i][j] == '.')hasDot = true;
		}
		if (t+x == 4) xWin = true;
		if (t+o == 4) oWin = true;
	}

	// check columns
	for (int i = 0; i < 4; i++) {
		int x = 0,o = 0,t = 0;
		for (int j = 0; j < 4; j++) {
			if (board[j][i] == 'X')x++;
			if (board[j][i] == 'O')o++;
			if (board[j][i] == 'T')t++;
		}
		if (t+x == 4) xWin = true;
		if (t+o == 4) oWin = true;
	}

	// check diagonals
	{
		int x = 0,o = 0,t = 0;
		for (int i = 0; i < 4; i++) {
			if (board[i][i] == 'X')x++;
			if (board[i][i] == 'O')o++;
			if (board[i][i] == 'T')t++;
		}
		if (t+x == 4) xWin = true;
		if (t+o == 4) oWin = true;
	}
	{
		int x = 0,o = 0,t = 0;
		for (int i = 0; i < 4; i++) {
			if (board[i][3-i] == 'X')x++;
			if (board[i][3-i] == 'O')o++;
			if (board[i][3-i] == 'T')t++;
		}
		if (t+x == 4) xWin = true;
		if (t+o == 4) oWin = true;
	}

	if (xWin) {
		out << "X won";
	} else if (oWin) {
		out << "O won";
	} else {
		if (hasDot) {
			out << "Game has not completed";
		} else {
			out << "Draw";
		}
	}
}

int main()
{
	std::string baseDir = "problems2013/";
	std::string testFile = "A-large";

	std::ifstream in(baseDir + testFile + ".in");
	std::ofstream out(baseDir + testFile + ".out");
	std::string t = baseDir + testFile + ".in";

	std::cout << "Starting solving cases..." << std::endl;

	int numberOfCases = 0;
	int currCase = 0;

	in >> numberOfCases;

	while(currCase++ < numberOfCases) {
		out << "Case #" << currCase << ": ";
		try {
			solveCase(in, out);
		} catch (std::exception& e) {
			std::cout << "Error on Case #" << currCase << " " << e.what() << std::endl;
		}
		if (currCase < numberOfCases) {
			out << std::endl;
		}
		std::cout << "Cases solved (" << currCase << "/" << numberOfCases << ")" << std::endl;
	}

	std::cout << "All cases solved!";
	return 0;
}
