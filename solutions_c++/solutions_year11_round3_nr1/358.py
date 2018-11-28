#include      <iostream>
#include      <algorithm>
#include      <string>
#include      <fstream>
#include      <list>
#include      <map>

using namespace std;

int main(int argc, char **argv) {
	int nTests;
	int nRows, nCols;
	bool bPosible;

	char achOriginal[50][50];
	char achMade[50][50];

	std::ifstream in("in");
	in >> nTests;

	for (int nTest = 1; nTest <= nTests; ++nTest) {
		in >> nRows >> nCols;

		bPosible = true;

		for (int i = 0; i < nRows; ++i) {
			for (int j = 0; j < nCols; ++j) {
				in >> achOriginal[i][j];
			}
		}

		for (int i = 0; i < nRows; ++i) {
			for (int j = 0; j < nCols; ++j) {
				achMade[i][j] = '_';
			}
		}

		for (int i = 0; i < nRows; ++i) {
			for (int j = 0; j < nCols; ++j) {
				if (achOriginal[i][j] == '.') {
					achMade[i][j] = '.';
				} else if (achOriginal[i][j] == '#') {
					if (achMade[i][j] == '_') {
						achMade[i][j] = '/';

						if (j + 1 < nCols && achOriginal[i][j + 1] == '#') {
							achMade[i][j + 1] = '\\';
						} else {
							bPosible = false;
						}

						if (j + 1 < nCols && i + 1 < nRows && achOriginal[i + 1][j + 1] == '#') {
							achMade[i + 1][j + 1] = '/';
						} else {
							bPosible = false;
						}

						if (i + 1 < nRows && achOriginal[i + 1][j] == '#') {
							achMade[i + 1][j] = '\\';
						} else {
							bPosible = false;
						}
					}
				}
			}
		}

		cout << "Case #" << nTest << ":" << endl;

		if (bPosible == false) {
			cout << "Impossible" << endl;
		} else {
			for (int i = 0; i < nRows; ++i) {
				for (int j = 0; j < nCols; ++j) {
					cout << achMade[i][j];
				}

				cout << endl;
			}
		}
	}

	in.close();

	return 0;
}
