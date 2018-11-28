#include <iostream>
#include <vector>
#include <utility>
#include <assert.h>
#include <stdlib.h>

std::vector< std::pair< int, std::pair<int, int> > > HandleCase() {
	bool board[512][512];
	int board_rects[512][512];
	int nRowCount, nColCount;
	std::cin >> nRowCount;
	std::cin >> nColCount;
	assert(nColCount % 4 == 0);
	int nBoardValue;
	for (int nRow = 0; nRow < nRowCount; ++nRow) {
		for (int nCol = 0; nCol < nColCount; ++nCol) {
			if (nCol % 4 == 0) {
				char c;
				std::cin >> c;
				switch (c) {
				case '0': case '1': case '2': case '3': case '4':
				case '5': case '6': case '7': case '8': case '9':
					nBoardValue = c - '0'; break;
				case 'A': case 'B': case 'C': case 'D': case 'E': case 'F':
				case 'a': case 'b': case 'c': case 'd': case 'e': case 'f':
					nBoardValue = toupper(c) - 'A' + 10; break;
				default:
					abort();
				}
			}
			board[nRow][nCol] = nBoardValue & (1 << (3 - (nCol % 4)));
			board_rects[nRow][nCol] = 0;
		}
	}
	for (int nRow = 0; nRow < nRowCount; ++nRow) {
		for (int nCol = 0; nCol < nColCount; ++nCol) {
			if (nRow == 0 && nCol == 0) {
				int x = 5;
			}
			const int nMaxSize = std::min(nColCount - nCol, nRowCount - nRow);
			const bool bWhite = board[nRow][nCol];
			int nSize;
			for (nSize = board_rects[nRow][nCol] + 1; nSize <= nMaxSize; ++nSize) {
				// std::cerr << "Trying (" << nRow << "," << nCol << ") for size "
				//           << nSize << std::endl;
				bool bNewWhite = nSize % 2 ? bWhite : !bWhite;
				bool bFailed = false;
				for (int nDiff = 0; nDiff < nSize; ++nDiff) {
					if (board[nRow + nDiff][nCol + nSize - 1] != bNewWhite) {
						bFailed = true;
						goto after_checks;
					}
					bNewWhite = !bNewWhite;
				}
				bNewWhite = !bNewWhite;
				for (int nDiff = nSize - 1; nDiff >= 0; --nDiff) {
					if (board[nRow + nSize - 1][nCol + nDiff] != bNewWhite) {
						bFailed = true;
						break;
					}
					bNewWhite = !bNewWhite;
				}
			after_checks:
				if (bFailed)
					break;
			}
			--nSize;
			// code to update board_rects
			for (int nDiffRow = 0; nDiffRow < nSize; ++nDiffRow)
				for (int nDiffCol = 0; nDiffCol < nSize; ++nDiffCol) {
					// std::cerr << "Assigning " << nSize - std::max(nDiffRow, nDiffCol)
					//           << std::endl;
					board_rects[nRow + nDiffRow][nCol + nDiffCol] =
					    nSize - std::max(nDiffRow, nDiffCol);
				}
			
			
		}
	}
	{
//		std::cerr << "DEBUG OF RECTS" << std::endl;
		for (int nRow = 0; nRow < nRowCount; ++nRow) {
			for (int nCol = 0; nCol < nColCount; ++nCol) {
//				std::cerr << board_rects[nRow][nCol] << ",";
			}
//			std::cerr << std::endl;
		}
	}
	std::vector< std::pair< int, std::pair<int, int> > > vecSolutions;
	while (1) {
		int nMaxRow = 0, nMaxCol = 0, nMaxRect = 0;
		for (int nRow = 0; nRow < nRowCount; ++nRow) {
			for (int nCol = 0; nCol < nColCount; ++nCol) {
				if (board_rects[nRow][nCol] > nMaxRect) {
					nMaxRow = nRow; nMaxCol = nCol; nMaxRect = board_rects[nRow][nCol];
				}
			}
		}
		// we should now find a rectangle
		if (nMaxRect > 0) {
			vecSolutions.push_back(std::make_pair(nMaxRect,
			                                      std::make_pair(nMaxRow, nMaxCol)));
			for (int nRow = nMaxRow; nRow < nMaxRow + nMaxRect; ++nRow) {
				for (int nCol = nMaxCol; nCol < nMaxCol + nMaxRect; ++nCol) {
					board_rects[nRow][nCol] = 0;
				}
			}
			for (int nRow = 0; nRow < nMaxRow + nMaxRect; ++nRow) {
				for (int nCol = 0; nCol < nMaxCol + nMaxRect; ++nCol) {
					const int nRowDist = nRow >= nMaxRow ? 0 : nMaxRow - nRow;
					const int nColDist = nCol >= nMaxCol ? 0 : nMaxCol - nCol;
					const int nDist = std::max(nRowDist, nColDist);
					board_rects[nRow][nCol] = std::min(board_rects[nRow][nCol], nDist);
				}
			}
		} else break;
	}
	return vecSolutions;
}

int main() {
	int nCases;
	std::cin >> nCases;
	for (int i = 0; i < nCases; ++i) {
		const std::vector< std::pair< int, std::pair<int, int> > > vecSolutions =
		    HandleCase();
		std::vector< std::pair< int, std::pair<int, int> > >::const_iterator it =
		    vecSolutions.begin();
		int sarSizes[1000] = {0};
		int nLastSize = 27852785;
		int nUniqueSizes = 0;
		for (; it != vecSolutions.end(); ++it) {
			if (it->first != nLastSize) {
				nLastSize = it->first;
				++nUniqueSizes;
			}
			++sarSizes[it->first];
		}
		std::cout << "Case #" << (i + 1) << ": " << nUniqueSizes << std::endl;
		for (int i = 1000 - 1; i >= 0; --i) {
			if (sarSizes[i] > 0)
				std::cout << i << " " << sarSizes[i] << std::endl;
		}
	}
}
