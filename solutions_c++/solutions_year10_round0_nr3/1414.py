#include <iostream>

typedef unsigned long long U64;



int main() {
#define int fail
	U64 nCases;
	std::cin >> nCases;
	for (U64 i = 0; i < nCases; ++i) {
		U64 sarGroups[10000] = {0};
		U64 nRuns;
		U64 nCapacity;
		U64 nGroupCount;
		std::cin >> nRuns >> nCapacity >> nGroupCount;
		for (U64 j = 0; j < nGroupCount; ++j) std::cin >> sarGroups[j];
		U64 nGroupIndex = 0;
		U64 nTotal = 0;
		for (U64 r = 0; r < nRuns; ++r) {
			U64 nTotalForRun = 0;
			U64 nOrigGroupIndex = nGroupIndex;
			while (1) {
				if (nTotalForRun + sarGroups[nGroupIndex] <= nCapacity) {
					nTotalForRun += sarGroups[nGroupIndex];
				} else break;
				++nGroupIndex;
				if (nGroupIndex == nGroupCount) nGroupIndex = 0;
				if (nGroupIndex == nOrigGroupIndex) break;
			}
			nTotal += nTotalForRun;
		}
		std::cout << "Case #" << (i + 1) << ": " << nTotal << std::endl;
	}
}
