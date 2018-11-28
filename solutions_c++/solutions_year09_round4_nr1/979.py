#include <iostream>
#include <algorithm>
#include <cctype>
#include <cassert>

int FindExchange(int nStartRow, int nSize, int leading[50]) {
	int nRow;
	for (nRow = nStartRow ; nRow < nSize; ++nRow)
		if (leading[nRow] <= nStartRow)
			return nRow;
	abort();
}

int main() {
	int nCases;
	int nCounter = 1;
	std::cin >> nCases;
	while (nCases--) {
		int matrix[50][50] = {0};
		int leading[50]; for (int i = 0; i < 50; ++i) leading[i] = -1;
		int nSize;
		std::cin >> nSize;
		int nRow, nCol;
		for (nRow = 0; nRow < nSize; ++nRow)
			for (nCol = 0; nCol < nSize; ++nCol) {
				char c = '\n';
				while (isspace(c)) std::cin >> c;
				assert(c == '1' || c == '0');
				matrix[nRow][nCol] = c - '0';
			}
		for (nRow = 0; nRow < nSize; ++nRow)
			for (nCol = 0; nCol < nSize; ++nCol)
				if (matrix[nRow][nCol] == 1) leading[nRow] = nCol;
		int nSteps = 0;
		for (nRow = 0; nRow < nSize; ++nRow) {
			if (leading[nRow] > nRow) {
				int x = FindExchange(nRow, nSize, leading);
				for (int y = x; y > nRow; --y) {
					std::swap(leading[y], leading[y - 1]);
					++nSteps;
				}
			}
		}
		std::cout << "Case #" << nCounter++ << ": " << nSteps << std::endl;
	}
}
