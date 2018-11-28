#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

#include "CJUtils.cpp"

const string INPUT_FILE = "A-large.in";
const string OUTPUT_FILE = "A-large.out";

void readBoard(ifstream& infile, vector<char>& board) {
	string line;
	for (int i = 0; i < 4; ++i) {
		getline(infile, line);
		for (int j = 0; j < 4; ++j) {
			board.push_back(line[j]);
		}
	}
	getline(infile, line); // Get rid of the blank line
}

bool isWinningCharacter(char ch, char player) {
	return ch == player || ch == 'T';
}

bool characterWon(vector<char>& board, char player) {
	bool allGood = false;
	// Check rows
	for (int row = 0; row < 4; ++row) {
		if (isWinningCharacter(board[row * 4 + 0], player) &&
			isWinningCharacter(board[row * 4 + 1], player) &&
			isWinningCharacter(board[row * 4 + 2], player) &&
			isWinningCharacter(board[row * 4 + 3], player)) return true;
	}

	// Check columns
	for (int col = 0; col < 4; ++col) {
		if (isWinningCharacter(board[0 * 4 + col], player) &&
			isWinningCharacter(board[1 * 4 + col], player) &&
			isWinningCharacter(board[2 * 4 + col], player) &&
			isWinningCharacter(board[3 * 4 + col], player)) return true;
	}

	// Check diagonals
	if (isWinningCharacter(board[0 * 4 + 0], player) &&
		isWinningCharacter(board[1 * 4 + 1], player) &&
		isWinningCharacter(board[2 * 4 + 2], player) &&
		isWinningCharacter(board[3 * 4 + 3], player)) return true;
	if (isWinningCharacter(board[0 * 4 + 3], player) &&
		isWinningCharacter(board[1 * 4 + 2], player) &&
		isWinningCharacter(board[2 * 4 + 1], player) &&
		isWinningCharacter(board[3 * 4 + 0], player)) return true;

	return false;
}

string doTestCase(ifstream& infile) {
	vector<char> board;
	readBoard(infile, board);
	


	// Check if X won
	if (characterWon(board, 'X'))
		return "X won";
	// Check if O won
	else if (characterWon(board, 'O'))
		return "O won";

	// Now, check if the game has not completed
	for (int i = 0; i < 16; ++i) {
		if (board[i] == '.') return "Game has not completed";
	}
	 
	// If neither of them won, it's a draw
	return "Draw";
}

int main(int argc, char *argv[]) {
	cout << "Hello, world!" << endl;

	ifstream infile(INPUT_FILE.c_str());
	if (!infile.good()) {
		cout << "Error opening input file." << endl;
		return -1;
	}
	ofstream outfile(OUTPUT_FILE.c_str());

	string line;

	// Read the number of test cases
	getline(infile, line);
	size_t T = StringToInteger(line);
	cout << "Test cases " << T << endl;
	for (size_t i = 0; i < T; ++i) {
		string answer = doTestCase(infile);
		outfile << "Case #" << i + 1 << ": " << answer << endl;
	}


	_sleep(1000);
	return 0;
}