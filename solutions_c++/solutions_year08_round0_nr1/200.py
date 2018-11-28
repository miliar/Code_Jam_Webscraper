#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

unsigned getunsignedeger() {
	stringstream converter;
	string line;
	getline(cin, line);
	converter << line;
	unsigned result;
	converter >> result;
	return result;
}

static const unsigned HUGE = (unsigned) -1;
unsigned minSwitches(string providers[], unsigned nProviders,
					 string queries[], unsigned nQueries) {
	unsigned table[nProviders][nQueries];
	unsigned mins[nQueries];
	
	for (unsigned col = 0; col < nQueries; col++) {
		unsigned least = HUGE;
		
		for (unsigned row = 0; row < nProviders; row++) {
			if (providers[row] == queries[col]) {
				table[row][col] = HUGE;
			} else if (col == 0) {
				table[row][col] = 0;
			} else {
				table[row][col] = min(table[row][col - 1], mins[col - 1] + 1);
			}
			least = min(least, table[row][col]);
		}
		
		mins[col] = least;
		if (least == HUGE) return HUGE;
	}

	return mins[nQueries - 1];
}

int main() {
	unsigned nCases = getunsignedeger();
	for (unsigned n = 1; n <= nCases; n++) {
		unsigned nProviders = getunsignedeger();
		string providers[nProviders];
		for (unsigned i = 0; i < nProviders; i++) {
			getline(cin, providers[i]);
		}
	
		unsigned nQueries = getunsignedeger();
		string queries[nQueries];
		for (unsigned i = 0; i < nQueries; i++) {
			getline(cin, queries[i]);
		}
		
		cout << "Case #" << n << ": "
  			 << minSwitches(providers, nProviders, queries, nQueries) << endl;
	}	
	
	return 0;
}