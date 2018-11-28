
#include <vector>
#include <iostream>
#include <assert.h>


void HandleCase() {
	int nWidth, nHeight;
	std::cin >> nHeight;
	std::cin >> nWidth;
	std::vector<int> vecHeights; vecHeights.reserve(nWidth * nHeight);
	std::vector<int> vecFlows(nWidth * nHeight, 0);
	std::vector<int> vecTranslations(nWidth * nHeight + 1, 0);
	int i;
	for (i = 0; i < nWidth * nHeight; ++i) {
		int n; std::cin >> n;
		vecHeights.push_back(n);
	}
	int nFlowIndex = 1;
	for (i = 0; i < nWidth * nHeight; ++i, ++nFlowIndex) {
		int nRow = i / nWidth, nCol = i % nWidth;
		while (1) {
			int nWhere = 4;
//			std::cerr << "To err: " << nRow << " " << nCol << "\n";
			if (vecFlows[nRow * nWidth + nCol] != 0) {
				vecTranslations[nFlowIndex - 1] =
				    vecTranslations[vecFlows[nRow * nWidth + nCol] - 1];
				break;
			} else {
				vecFlows[nRow * nWidth + nCol] = nFlowIndex;
			}
			bool bHasTop = nRow > 0;
			bool bHasLeft = nCol > 0;
			bool bHasBottom = nRow < nHeight - 1;
			bool bHasRight = nCol < nWidth - 1;
			int nMin = vecHeights[nRow * nWidth + nCol];
			if (bHasTop && vecHeights[(nRow - 1) * nWidth + nCol] < nMin) {
				nMin = vecHeights[(nRow - 1) * nWidth + nCol];
				nWhere = 0;
			}
			if (bHasLeft && vecHeights[nRow * nWidth + (nCol - 1)] < nMin) {
				nMin = vecHeights[nRow * nWidth + (nCol - 1)];
				nWhere = 1;
			}
			if (bHasRight && vecHeights[nRow * nWidth + (nCol + 1)] < nMin) {
				nMin = vecHeights[nRow * nWidth + (nCol + 1)];
				nWhere = 2;
			}
			if (bHasBottom && vecHeights[(nRow + 1) * nWidth + nCol] < nMin)
			{
				nMin = vecHeights[(nRow + 1) * nWidth + nCol];
				nWhere = 3;
			}
			switch (nWhere) {
			case 0: --nRow; break;
			case 1: --nCol; break;
			case 2: ++nCol; break;
			case 3: ++nRow; break;
			case 4: vecTranslations[nFlowIndex - 1] = nFlowIndex; break;
			default: abort();
			}

		}
	}
	for (int i = 0; i < nWidth * nHeight; ++i) {
		assert(vecFlows[i] > 0);
		vecFlows[i] = vecTranslations[vecFlows[i] - 1];
	}
	// I am not sure if I need this, but I am writing this code in the last
	// minute, sorry guys... please don't hate me much :)
	char nNext = 'a';
	std::vector<char> vecLexiTrans(nWidth * nHeight + 1, 0);
	for (int i = 0; i < nWidth * nHeight; ++i) {
		if (vecLexiTrans[vecFlows[i]] == 0)
			vecLexiTrans[vecFlows[i]] = nNext++;
		std::cout << vecLexiTrans[vecFlows[i]];
		if (i % nWidth == nWidth - 1)
			std::cout << '\n';
		else
			std::cout << ' ';
	}
}


int main() {
	int nCases;
	std::cin >> nCases;
	for (int i = 0; i < nCases; ++i) {
		std::cout << "Case #" << (i + 1) << ":" << "\n";
		HandleCase();
	}
}
