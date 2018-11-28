#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>

#define NDEBUG
#include <cassert>

using namespace std;

const int boardSize = 4;

int xy2idx(int x, int y)
{
	assert(x >= 0);
	assert(x < boardSize);
	assert(y >= 0);
	assert(y < boardSize);
	return x + y * boardSize;
}

void getInputFile(int argc, char* argv[], ifstream &inputFile)
{
	if (argc != 2) {
		cerr << "Require one argument (input file); exiting ...\n";
		exit(1);
	}
	string filename = argv[1];
	inputFile.exceptions(ifstream::failbit);
	inputFile.open(filename.c_str());
}

void getOutputFile(int argc, char* argv[], ofstream &outputFile)
{
	string filename = argv[1];
	unsigned dotIndex = filename.find_last_of('.');
	if (dotIndex != string::npos)
		filename.erase(dotIndex);
	filename += ".out";
	outputFile.exceptions(ofstream::failbit);
	outputFile.open(filename.c_str());
}

bool winningConfig(const vector<char>& state, char player, int x0, int y0, int dx, int dy)
{
	for (int i=0; i<boardSize; ++i) {
		char pos = state[xy2idx(x0+i*dx, y0+i*dy)];
		if ((pos != player) && (pos != 'T'))
			return false;
	}
	return true;
}

bool playerHasWon(const vector<char>& state, char player)
{
	for (int x=0; x<boardSize; ++x)
		if (winningConfig(state, player, x, 0, 0, 1))
			return true;
	for (int y=0; y<boardSize; ++y)
		if (winningConfig(state, player, 0, y, 1, 0))
			return true;
	if (winningConfig(state, player, 0, 0, 1, 1))
		return true;
	if (winningConfig(state, player, 0, boardSize-1, 1, -1))
		return true;
	return false;
}

bool boardIsFull(const vector<char>& state)
{
	for (int i=0; i<boardSize*boardSize; ++i)
		if (state[i] == '.')
			return false;
	return true;
}

void processCase(istream& inputFile, ostream& outputFile)
{
	vector<char> state(16);
	for (int y=0; y<boardSize; ++y)
		for (int x=0; x<boardSize; ++x) {
			inputFile >> state[xy2idx(x,y)];
		inputFile >> ws;
	}
	inputFile >> ws;

	if (playerHasWon(state, 'X'))
		outputFile << "X won";
	else if (playerHasWon(state, 'O'))
		outputFile << "O won";
	else if (boardIsFull(state))
		outputFile << "Draw";
	else
		outputFile << "Game has not completed";
}

int main(int argc, char *argv[])
{
	ifstream inputFile;
	getInputFile(argc, argv, inputFile);
	ofstream outputFile;
	getOutputFile(argc, argv, outputFile);

	int numCases;
	inputFile >> numCases >> ws;
	for (int caseIndex = 0; caseIndex < numCases; ++caseIndex) {
		outputFile << "Case #" << caseIndex+1 << ": ";
		cout << "Case #" << caseIndex+1 << "\n";
		processCase(inputFile, outputFile);
		outputFile << "\n";
	}
}


