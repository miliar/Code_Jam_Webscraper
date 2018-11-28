#include <iostream>

int main() {
	long long nCases;
	std::cin >> nCases;
	for (long long i = 0; i < nCases; ++i) {
		long long nMinimal, nMaximal, nFactor;
		std::cin >> nMinimal;
		std::cin >> nMaximal;
		std::cin >> nFactor;

//		long long powers[100];
		long long nPowersCount = 0;
		long long nAcc = nMinimal * nFactor;
		while (nAcc < nMaximal) {
//			powers[++nPowersCount] = nAcc;
			++nPowersCount;
			nAcc *= nFactor;
		}
		++nPowersCount;

		long long nTries = 0;
		std::cerr << "nPowersCount is " << nPowersCount << std::endl;
		while (nPowersCount > 1) {
			if (nPowersCount % 2)
				++nPowersCount;
			nPowersCount /= 2;
			++nTries;
		}
		std::cout << "Case #" << i + 1 << ": " << nTries << std::endl;
		
		
	}
}
