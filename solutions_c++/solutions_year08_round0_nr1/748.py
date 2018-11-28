
#include <stdio.h>
#include <string.h>
#pragma warning (disable: 4786)
#include <map>
#include <string>
#include <iostream>
#include <fstream>
#include <strstream>

using namespace std;

int instances[100];
int queries[1000];
int numEngines;
int numQueries;

/* finds the least number of switches from queries[start] to queries[end - 1] inclusive */
int findSwitches(int start, int end) {

	int switchCount = 2000;
	int instancesTemp[100];

	if (0 == end - start) return 0;

	memset(instancesTemp, 0, sizeof(instancesTemp));
	for (int queryLoop = start; queryLoop < end; queryLoop++) {
		instancesTemp[queries[queryLoop]]++;
	}
	for (int wantInstances = 0; wantInstances < end - start; wantInstances++) {
		/* try to find a item with only wantInstances instances in the query range */
		for (int item = 0; item < numEngines; item++) {
			if (wantInstances == instancesTemp[item]) {
				if (0 == wantInstances) return 0;
				/* found one, engine item, now for each instance, recurse for sub range, if the total is less than previous total, keep it, then keep going */
//				int thisStart = start;
//				for (int loop = 0; loop < wantInstances; loop++) {
					for (int nextStart = start; nextStart < end; nextStart++) {
						/* search queries till we get to 'item' */
						if (queries[nextStart] == item) {
							nextStart++;
							break;
						}
					}
					int temp = findSwitches(nextStart, end);
//					thisStart = nextStart;
					if (temp + 1 < switchCount) switchCount = temp + 1;
//				}
			}
		}
	}
	return switchCount;
}

int findMaxStreak(int start, int engineCantUse) {

	if (start >= numQueries - 1) return 0;

//	int streaks[100];
	int maxStreak = -1;
	int usingEngine = -1;
	int switchCount = 0;

	do {
		/* find longest streak, and recurse */
		for (int engine = 0; engine < numEngines; engine++) {
			if (engine == engineCantUse) continue;
			/* how far does this go? */
			for (int streak = 0; streak < numQueries - start; streak++) {
				if (engine == queries[start + streak]) break;
			}
			if (streak > maxStreak) {
				maxStreak = streak;
				usingEngine = engine;
			}
		}
		if (maxStreak == numQueries - start) return switchCount;
		switchCount += 1 + findMaxStreak(start + maxStreak, usingEngine);
	} while (false);
	return switchCount;
}

int main(int argc, char** argv) {


	/* First argument is the file to open and process */
	ifstream fin(argv[1]);
	int numCases;

	char name[200];

	/* first token is number of test cases */
	fin >> numCases;
	fin.getline(name, sizeof(name));

	FILE* outputFile = fopen("C:\\output.txt", "w");
	for (int loop = 0; loop < numCases; loop++) {

		map<string, int>	mapEngineToCode;
		memset(instances, 0, sizeof(instances));
		fin >> numEngines;
		fin.getline(name, sizeof(name));
		for (int engineLoop = 0; engineLoop < numEngines; engineLoop++) {
			fin.getline(name, sizeof(name));
			string nameString(name);
			/* give it an ID we can easily use for searching later */
			mapEngineToCode.insert(pair<string,int>(nameString, engineLoop));
		}
		fin >> numQueries;
		fin.getline(name, sizeof(name));
		for (int queryLoop = 0; queryLoop < numQueries; queryLoop++) {
			fin.getline(name, sizeof(name));
			string nameString(name);
			queries[queryLoop] = mapEngineToCode.find(nameString)->second;
			instances[queries[queryLoop]]++;
		}
		/* now have queries in array, do search algorithm */
//		int numSwitches = findSwitches(0, numQueries);
		int numSwitches = findMaxStreak(0, -1);
		fprintf(stdout, "Case #%d: %d\n", loop + 1, numSwitches);
		fprintf(outputFile, "Case #%d: %d\n", loop + 1, numSwitches);
	}
	fclose(outputFile);

	return 0;
}