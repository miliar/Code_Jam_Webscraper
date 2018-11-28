#include <iostream>
#include <fstream>
#include <vector>
#include <list>
using namespace std;

string checkLine(string line[4]) {
	// make a list for the magic
	std::list<string> lineList(line, line + 4);
	// are there any unfilled spaces?
	lineList.remove(".");	
	if(lineList.size() < 4) { return "n"; }
	// are there more than 2 unique characters?
	lineList.unique();
	if(lineList.size() > 2) { return "n"; }
	// there can only be 2 characters at this point. if not T, then X and O are present and there's no winner
	lineList.remove("T");
	if(lineList.size() == 2) { return "n"; }
	// at this point there were no unfilled spots, there are only 2 characters and one of them is T, so we have a winner. remove X to find out who.
	lineList.remove("X");
	if(lineList.size() == 0) { return "X"; } else { return "O"; }
}

int main() {
	// read file, create vector
	ifstream inFile("A-small-attempt1.in");
	ofstream outFile("A-small-attempt1.out");
	string line;
	std::vector<string> inFileVector;
	if(inFile.is_open()) {
		while(inFile.good()) {
			getline(inFile, line);
			inFileVector.push_back(line);
		}
	}
	
	// splice number of tests
	int T = atoi(inFileVector.front().c_str());
	inFileVector.erase(inFileVector.begin());

	// splice test cases into matrix arrays
	for(int t = 1; t <= T; t++) {
		// write a matrix
		string Matrix[4][4];
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
			// write a matrix
			Matrix[i][j] = inFileVector.front()[j];
			}
			// delete row of matrix inFileVector
			inFileVector.erase(inFileVector.begin());
		}
		
		// now work on matrix
		bool someoneWon = false;
		
		// did anyone win a row or column
		for(int k = 0; k < 4; k++) {
			// write the line
			string row[4], col[4];//, diag1[4], diag2[4];
			for(int i = 0; i < 4; i++) {
				// a row
				row[i] = Matrix[k][i];
				// a column
				col[i] = Matrix[i][k];
			}
			if(checkLine(row) != "n") { outFile << "Case #" << t << ": " << checkLine(row) << " won" << endl; someoneWon = true; break; }
			if(checkLine(col) != "n") { outFile << "Case #" << t << ": " << checkLine(col) << " won" << endl; someoneWon = true; break; }
		}
		// if no one has won yet, check diagonals
		if(someoneWon == false) {
			string diag1[4];
			string diag2[4];
			for(int i = 0; i < 4; i++) {
				diag1[i] = Matrix[i][i];
				diag2[i] = Matrix[i][3-i];
			}
			if(checkLine(diag1) != "n") { outFile << "Case #" << t << ": " << checkLine(diag1) << " won" << endl; someoneWon = true; }
			if(checkLine(diag2) != "n") { outFile << "Case #" << t << ": " << checkLine(diag2) << " won" << endl; someoneWon = true; }
		}
		// if someone hasn't won, find out what happened: if board is unfinished, game is still going; if finished, game is a draw
		if(someoneWon == false) {
			bool foundADot = false;
			for(int i = 0; i < 4; i++) {
				for(int j = 0; j < 4; j++) {
					if(Matrix[i][j] == ".") { foundADot = true; break; }
				}
				if(foundADot) { break; }
			}
			if(foundADot) { outFile << "Case #" << t << ": Game has not completed" << endl; }
			else { outFile << "Case #" << t << ": Draw" << endl; }
		}
		
		// delete blank space between test cases
		inFileVector.erase(inFileVector.begin());
	}

	return 0;
}
