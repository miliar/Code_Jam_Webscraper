#include <iostream>
#include <string>
#include "stdio.h"
using namespace std;

int main() {
	int numTests;
	cin >> numTests;

	for (int t = 1; t <= numTests; t++) {
		int numRows;
		int numCols;

		cin >> numRows >> numCols;

		char** table = new char*[numRows+1];
		for (int i = 0; i < numRows; i++) {
			table[i] = new char[numCols + 1];
			table[i][numCols] = 0;
		}
		table[numRows] = new char[numCols+1];
		for (int i = 0; i < numCols; i++) {
			table[numRows][i] = 0;
		}

		string token;
		for (int i = 0; i < numRows; i++) {
			cin >> token;
			strncpy(table[i], token.c_str(), numCols);
		}

		bool isPossible = true;
		for (int i = 0; i < numRows; i++) {
			for (int j = 0; j < numCols; j++) {
				if (table[i][j] == '#') {
					//Blue found - try to replace with 2x2 red

					if ((table[i][j+1] == '#') && (table[i+1][j] == '#') && (table[i+1][j+1] == '#')) {
						//Red possible
						table[i][j] = '/';
						table[i][j+1] = '\\';
						table[i+1][j] = '\\';
						table[i+1][j+1] = '/';
					}
					else {
						isPossible = false;
						break;
					}
				}
			}

			if (!isPossible) {
				break;
			}
		}

		printf("Case #%d:\n", t);
		if (isPossible) {
			for (int i = 0; i < numRows; i++) {
				printf("%s\n", table[i]);
			}
		}
		else {
			printf("Impossible\n");
		}
	}
}