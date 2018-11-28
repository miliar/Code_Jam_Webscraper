#include <fstream>
using namespace std;

const int RIDE_BITS = 30;
const int MAX_GROUPS = 1100;

// Describes the outcome of N rides starting from a certain group
struct MultiRide {
	int NextGroup;		// Next group in the queue
	__int64 Cost;		// Total cost of these N rides
};


int main() {
	ifstream fin("rollercoaster.in");
	ofstream fout("rollercoaster.out");

	int nTestCases;
	fin >> nTestCases;

	for (int testNo = 0; testNo < nTestCases; testNo++) {
		unsigned int rides, capacity, nGroups; 
		fin >> rides >> capacity >> nGroups;

		int groupSize[MAX_GROUPS];
		for (int groupNo = 0; groupNo < nGroups; groupNo++) 
			fin >> groupSize[groupNo];

		MultiRide ridesFor[RIDE_BITS][MAX_GROUPS];

		// Fill in the results of the first ride
		for (int startingGroup = 0; startingGroup < nGroups; startingGroup++) {
			int peopleSeated = groupSize[startingGroup];
			int nextGroup = (startingGroup + 1) % nGroups;

			while ((peopleSeated + groupSize[nextGroup] <= capacity)		// Can accomodate these people too ...
				&& (nextGroup != startingGroup)) {							// ... and not all the groups are loaded

				peopleSeated += groupSize[nextGroup];
				nextGroup = (nextGroup + 1) % nGroups;
			}

			ridesFor[0][startingGroup].Cost = peopleSeated;
			ridesFor[0][startingGroup].NextGroup = nextGroup;
		}

		// Calculate the results for 2, 4, 8 rides etc.
		for (int previousBatch = 0; previousBatch < (RIDE_BITS - 1); previousBatch++) {
			int currentBatch = previousBatch + 1;

			for (int startingGroup = 0; startingGroup < nGroups; startingGroup++) {
				int secondGroup = ridesFor[previousBatch][startingGroup].NextGroup;
				__int64 batchCost = ridesFor[previousBatch][startingGroup].Cost + ridesFor[previousBatch][secondGroup].Cost;
				int nextGroup = ridesFor[previousBatch][secondGroup].NextGroup;

				ridesFor[currentBatch][startingGroup].NextGroup = nextGroup;
				ridesFor[currentBatch][startingGroup].Cost = batchCost;
			}
		}

		__int64 totalCost = 0;
		int frontGroup = 0;

		// Calculate the final results
		for (int bitIndex = 0; bitIndex < RIDE_BITS; bitIndex++) {
			int mask = 1 << bitIndex;
			if ((rides & mask) == mask) {
				totalCost += ridesFor[bitIndex][frontGroup].Cost;
				frontGroup = ridesFor[bitIndex][frontGroup].NextGroup;
			}
		}


		fout << "Case #" << testNo+1 << ": " << totalCost << endl;

	}


	return 0;
}