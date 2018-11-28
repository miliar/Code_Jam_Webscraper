#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
	int N, currentCase = 1;
	for (cin >> N; N; N--) {
		set<string> searchEngines;
		int S;
		string searchEngine;
		cin >> S;
		getline(cin, searchEngine); //Read the newline character
		while (S--) {
			getline(cin, searchEngine);
			searchEngines.insert(searchEngine);
		}

		int switches = 0;
		set<string> remainingSearchEngines(searchEngines);
		int Q;
		cin >> Q;
		getline(cin, searchEngine); //Read the newline character
		while (Q--) {
			getline(cin, searchEngine);
			remainingSearchEngines.erase(searchEngine);
			if (remainingSearchEngines.empty()) {
				switches++;
				remainingSearchEngines = set<string>(searchEngines);
				remainingSearchEngines.erase(searchEngine);
			}
		}
		cout << "Case #" << currentCase++ << ": " << switches << '\n';
	}
}

