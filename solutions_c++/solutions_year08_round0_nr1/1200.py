#include <iostream>
#include <string>
#include <vector>

using namespace std;


//-----------------------------------------------------------------------------
int measure(const vector<int>& querySet, int engine, int index)
{
	int distance = 0;
	while (index < querySet.size()) {
		if (querySet[index] == engine) {
			return distance;
		} else {
			distance++;
			index++;
		}
	}

	return distance;
}



//-----------------------------------------------------------------------------
int countswitches(const vector<int>& querySet, int engineCount)
{
	int index = 0;
	int iter = 0;

	do {

		int distance = 0;
		int engine = 0;

		// Measure all the engines, find the longest one
		distance = measure(querySet, 0, index);
		for (int i=1; i < engineCount; i++) {
			int n = measure(querySet, i, index);
			if (n > distance) {
				distance = n;
				engine = i;
			}
		}

		// Step
		iter++;
		index += distance;

	} while (index != querySet.size());


	return (iter - 1);
}



//-----------------------------------------------------------------------------
int main(int argc, char* argv[])
{
	vector<int> querySet;
	const int lineLength = 100;
	char line[lineLength];

	int testCases;


	cin.getline(line, lineLength);
	testCases = atoi(line);


	for (int tc=0; tc < testCases; tc++) {
		int searchEngineCount;
		int queryCount;


		cin.getline(line, lineLength);
		searchEngineCount = atoi(line);

		vector<string> engines;
		for (int i=0; i < searchEngineCount; i++) {
			cin.getline(line, lineLength);
			engines.push_back(line);
		}

		cin.getline(line, lineLength);
		queryCount = atoi(line);

		for (int i=0; i < queryCount; i++) {
			string search;
			cin.getline(line, lineLength);
			search = line;
			for (int j=0; j < engines.size(); j++) {
				if (engines[j] == search) {
					querySet.push_back(j);
					break;
				}
			}
		}	


		if (queryCount) {
			int result = countswitches(querySet, searchEngineCount);
			cout << "Case #" << (tc + 1) << ": " << result << endl;
		} else {
			cout << "Case #" << (tc + 1) << ": " << 0 << endl;
		}


		querySet.clear();
	}
}

