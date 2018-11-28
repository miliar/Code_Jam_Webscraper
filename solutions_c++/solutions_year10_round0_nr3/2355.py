//============================================================================
// Name        : themepark.cpp
// Author      : Kiran
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <limits>
using namespace std;

int main() {
	int numCases = 0;
	scanf("%d", &numCases);
	unsigned long results[30];
	results[0] = 1;

	for (int i=0;i<numCases;i++) {
		int Rounds; // R <= 10^8
		unsigned long long capacity; // k <= 10^9
		int numGroups; // N <= 1000
		unsigned int queue[1000]; // Gi <= 10^7

		unsigned long long euros=0;

		int queueStart = 0;

		scanf("%d %llu %d", &Rounds, &capacity, &numGroups);
		for (int j=0;j<numGroups;j++) {
			scanf("%u", &queue[j]);
		}
		for (int j=0;j<Rounds;j++) {
			unsigned long long usedCapacity=0;
			int markQueueStart = queueStart;
			while (true) {
				unsigned int curGroup = queue[queueStart];
				if (curGroup+usedCapacity > capacity) {
					break;
				}
				usedCapacity += curGroup;
				euros += curGroup;
				queueStart++;
				if (queueStart == numGroups)
					queueStart = 0;
				if (markQueueStart == queueStart) {
					break;
				}
			}
		}
		printf("Case #%d: %llu\n", i+1, euros);
	}
	return 0;
}
