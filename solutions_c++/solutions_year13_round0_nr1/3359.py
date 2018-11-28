#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <fstream>
#include <map>
#include <algorithm>

using namespace std;

#define DIM_X		4
#define DIM_Y		4

static char grid[DIM_X][DIM_Y];

bool hasWon(const char x) {
	int score = 0;
	/* Check lines */
	for(int j = 0; j < DIM_Y; j++) {
		score = 0;
		for(int i = 0; i < DIM_X; i++) {
			if(grid[i][j] == x || grid[i][j] == 'T') {
				score++;
			}
		}
		if(score == 4) {return true;}
	}

	/* Check column */
	for(int i = 0; i < DIM_X; i++) {
		score = 0;
		for(int j = 0; j < DIM_Y; j++) {
			if(grid[i][j] == x || grid[i][j] == 'T') {
				score++;
			}
		}
		if(score == 4) {return true;}
	}

	/* Check diagonal */
	score = 0;
	for(int i = 0; i < DIM_X; i++) {
		if(grid[i][i] == x || grid[i][i] == 'T') {
			score++;
		}
	}
	if(score == 4) {return true;}

	/* Other diaognal */
	score = 0;
	for(int i = 0; i < DIM_X; i++) {
		if(grid[i][3-i] == x || grid[i][3-i] == 'T') {
			score++;
		}
	}
	if(score == 4) {return true;}

	return false;
}

bool hasEmptySlot() {
	for(int j = 0; j < DIM_Y; j++) {
		for(int i = 0; i < DIM_X; i++) {
			if(grid[i][j] == '.') {
				return true;
			}
		}
	}
	return false;
}

int main(int argc, char* argv[]) {
	string inTestName, outTestName;

	cout << "Enter the in test file name : " << endl;
	cin >> inTestName;
	cout << endl;

	size_t found = inTestName.find_last_of(".");
	outTestName = inTestName.substr(0, found) + ".out";

	/* Open file */
	ifstream inFile(inTestName.c_str());
	if(!inFile.is_open()) {
		cout << "Can't open input file" << endl;
		system("PAUSE");
		return 1;
	}

	ofstream outFile(outTestName.c_str());
	if(!outFile.is_open()) {
		cout << "Can't open output file" << endl;
		system("PAUSE");
		return 1;
	}

	int T; /*number of tests */
	inFile >> T;

	cout << "Start : "<< endl;
	for(int t = 0; t < T; t++) {
		cout << "\rProcess test " << t << " out of " << T;

		/* Fill grid */
		for(int j = 0; j < DIM_Y; j++) {
			for(int i = 0; i < DIM_X; i++) {
				inFile >> grid[i][j];
			}
		}

		/* Check if X won */
		outFile << "Case #" << t + 1;
		if(hasWon('X')) {
			 outFile << ": X won" << endl;
		}
		else if(hasWon('O')) {
			outFile << ": O won" << endl;
		}
		else if(hasEmptySlot()) {
			outFile << ": Game has not completed" << endl;
		}
		else {
			outFile << ": Draw" << endl;
		}
	}
	outFile.close();
	inFile.close();

	cout << endl << "Stop" << endl;

	system("PAUSE");
	return 0;
}
