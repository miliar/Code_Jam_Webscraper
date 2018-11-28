#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[]) {

	ifstream input("B-large.in");

	string line;

	getline(input, line);
	int numCases = atoi(line.c_str());

	int nGoogler, nSurprising, bestAtLeast;
	int total;

	for (int i = 1; i <= numCases; ++i) {
		stringstream converter;
		getline(input, line);
		converter << line;

		converter >> nGoogler;
		converter >> nSurprising;
		converter >> bestAtLeast;

		int leastTotalNonSurp = 3*bestAtLeast - 2;
		int leastTotalSurp = 3*bestAtLeast - 4;

		if (leastTotalNonSurp < 0) leastTotalNonSurp = bestAtLeast;
		if (leastTotalSurp < 0) leastTotalSurp = bestAtLeast;
		
		int maxOut = 0;
		
		for (int j = 0; j < nGoogler; ++j) {
			converter >> total;
		
			if (total >= leastTotalNonSurp)
				++maxOut;
			else if (total >= leastTotalSurp && nSurprising	> 0) {
				++maxOut;
				--nSurprising;
			}
		}
		
		/* print case output */
		cout << "Case #" << i << ": " << maxOut << endl;
	}

	input.close();

	return 0;
}
