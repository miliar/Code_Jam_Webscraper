#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

const int MAX_NAME = 100; // Maximum length of search engine name

int
main()
{
	char buffer[MAX_NAME];

	// Read number of numCases
	int numCases, numEngines, numSearches;
	cin >> numCases;

	for (int c = 1; c != numCases + 1; ++c) {
		// Read search numEngines
		cin >> numEngines;
		map<string,int> engines;
		cin.ignore();	// Ignore newline at end of numEngines
		for (int i = 0; i != numEngines; ++i) {
			// Tokenise the names of search engines
			cin.getline(buffer, MAX_NAME);
			string name(buffer);
///cout << "Engine " << i << " is " << name << endl;
			engines[name] = i;
		}

		// Read searches
		cin >> numSearches;
		int *searches = new int[numSearches];
		cin.ignore();	// Ignore newline at end of numSearches
		for (int i = 0; i != numSearches; ++i) {
			cin.getline(buffer, MAX_NAME);
			string query(buffer);
///cout << "Search " << i << " is " << query << endl;
			searches[i] = engines[query];
		}

		int *start = searches, numSwitches = 0;
		int **furthestPos = new int*[numEngines];
		while (true) {
			// Find maximum forward distance for search engines
			for (int i = 0; i != numEngines; ++i)
				furthestPos[i] = find(start, searches + numSearches, i);
			
			// Take the maximum forward distance
			start = *max_element(furthestPos, furthestPos + numEngines);

///cout << "Start: " << start << endl;

			// Switch if there's more searches
			if (start != searches + numSearches)
				++numSwitches;
			else
				break;
		}
		
		// Output
		cout << "Case #" << c << ": " << numSwitches << endl;
		
		delete[] searches, furthestPos;
	}

	return 0;
}
