#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned long long uint64;

int main() {
	uint64 totalCases = 0, count = 1;
	cin >> totalCases;

	while (totalCases) {
		int numberOfGroups;
		uint64 numberOfRounds, totalCapacity;
		cin >> numberOfRounds >> totalCapacity >> numberOfGroups;

		uint64* group = new uint64[numberOfGroups];
		//vector<uint64> group(numberOfGroups);

		for (uint64 i = 0; i < numberOfGroups; i++) {
			uint64 groupSize;
			cin >> groupSize;
			group[i] = groupSize;
		}

		uint64 moneyMade = 0;
		uint64 i = 0;
		

		while (numberOfRounds) {
			uint64 totalDone = 0;
			uint64 previousValue = i;
			while (true) {
				if (totalDone + group[i] > totalCapacity) {
					break;
				}
				totalDone += group[i++];
				if (i == numberOfGroups) {
					i = 0;
				}
				if (i == previousValue) {
					break;
				}
			}
			moneyMade += totalDone;
			if (i == previousValue) {
				moneyMade *= numberOfRounds;
				numberOfRounds = 1;
			}
			numberOfRounds--;
		}
		cout << "Case #" << count++ << ": " << moneyMade << endl;
		totalCases--;
	}

	return 0;
}