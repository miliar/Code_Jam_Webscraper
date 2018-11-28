#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;
	for (int i = 0; i < numCases; ++i) {
		cout << "Case #" << i + 1 << ": ";
		int numDancers, numSurprisingScores, minBestResult;
		cin >> numDancers >> numSurprisingScores >> minBestResult;
		int limitWithSurprise = max(minBestResult * 3 - 4, minBestResult);
		int limitWithoutSurprise = max(minBestResult * 3 - 2, minBestResult);
		int numWithMinBestResult = 0;
		vector<int> totalScores(numDancers);
		for (vector<int>::iterator it = totalScores.begin(); it != totalScores.end(); ++it) {
			cin >> *it;
			if (*it >= limitWithoutSurprise || *it >= limitWithSurprise && numSurprisingScores-- > 0) {
				numWithMinBestResult += 1;
			}
		}
		cout << numWithMinBestResult << endl;
	}
}
