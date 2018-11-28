#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
	if (argc != 2) {
		cerr << "Usage: solver <input-file>" << endl;
		cerr << "Wrong number of arguments!" << endl;
		return 1;
	}
	ifstream inputFile;
	inputFile.open(argv[1], ifstream::in);
	if (!inputFile.is_open()) {
		cerr << "Could not open '" << argv[1] << "'." << endl;
		return 1;
	}
	int T;
	inputFile >> T;
	//cout << "Processing " << T << " cases:" << endl;
	for (int t = 1; t <= T; t++) {
		char map[4][4];
		for (int y = 0; y < 4; y++) {
			for (int x = 0; x < 4; x++) {
				inputFile >> map[x][y];
			}
			inputFile.ignore(1);
		}
		// Solve the current map
		cout << "Case #" << t << ": ";
		int sumDots = 0;
		int nDots = 0;
		int nX = 0;
		int nO = 0;
		int nT = 0;
		// Horizontal lines
		for (int y = 0; y < 4; y++) {
			nDots = nX = nO = nT = 0;
			for (int x = 0; x < 4; x++) {
				switch (map[x][y]) {
					case '.':
						nDots++;
						break;
					case 'X':
						nX++;
						break;
					case 'O':
						nO++;
						break;
					case 'T':
						nT++;
						break;
				}
			}
			if ((nO + nT) == 4) {
				cout << "O won" << endl;
				goto testDone;
			}
			if ((nX + nT) == 4) {
				cout << "X won" << endl;
				goto testDone;
			}
			sumDots += nDots;
		}
		// Vertical lines
		for (int x = 0; x < 4; x++) {
			nDots = nX = nO = nT = 0;
			for (int y = 0; y < 4; y++) {
				switch (map[x][y]) {
					case '.':
						nDots++;
						break;
					case 'X':
						nX++;
						break;
					case 'O':
						nO++;
						break;
					case 'T':
						nT++;
						break;
				}
			}
			if ((nO + nT) == 4) {
				cout << "O won" << endl;
				goto testDone;
			}
			if ((nX + nT) == 4) {
				cout << "X won" << endl;
				goto testDone;
			}
		}
		// Diagonal line
		nDots = nX = nO = nT = 0;
		for (int i = 0; i < 4; i++) {
			switch (map[i][i]) {
				case '.':
					nDots++;
					break;
				case 'X':
					nX++;
					break;
				case 'O':
					nO++;
					break;
				case 'T':
					nT++;
					break;
			}
		}
		if ((nO + nT) == 4) {
			cout << "O won" << endl;
			goto testDone;
		}
		if ((nX + nT) == 4) {
			cout << "X won" << endl;
			goto testDone;
		}
		// Other diagonal line
		nDots = nX = nO = nT = 0;
		for (int i = 0; i < 4; i++) {
			switch (map[i][3 - i]) {
				case '.':
					nDots++;
					break;
				case 'X':
					nX++;
					break;
				case 'O':
					nO++;
					break;
				case 'T':
					nT++;
					break;
			}
		}
		if ((nO + nT) == 4) {
			cout << "O won" << endl;
			goto testDone;
		}
		if ((nX + nT) == 4) {
			cout << "X won" << endl;
			goto testDone;
		}
		// No wins so far?
		if (sumDots == 0) {
			cout << "Draw" << endl;
		} else {
			cout << "Game has not completed" << endl;
		}
testDone:;
	}
	return 0;
}
