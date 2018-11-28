#include "stdio.h"
#include "stdlib.h"
#include "iostream.h"
#include "fstream.h"

/*
 * Messy, but at least it works... (I hope)
 */

int findLastUsedEngineIndex(char engineNames[][256], int numEngines, char query[][256], int numQueries);

void output(int testCase, int numSwitches, ofstream outputFile);

void initBool(bool* bools, int numBools, bool val);

int main(int argv, char argc[]){
	char url[] = "A-large.in";
	ifstream input;
	input.open(url);
	if(!input){
		printf("Error opening input file!\n");
		return 1;
	}
	
	ofstream outputFile;
	outputFile.open("Universe.out");
	
	char line[256];
	int numCases;
	int numEngines;
	int numQueries;
	char engineNames[100][256];
	char query[1000][256];
	
	input.getline(line, 256);
	numCases = atoi(line);
	//printf("numCases = %i\n", numCases);
	
	//loop through each case
	for(int c = 0; c < numCases; c++){
		input.getline(line, 256);
		numEngines = atoi(line);
		printf("numEngines = %i\n", numEngines);
		//load all engine names
		for(int e = 0; e < numEngines; e++){
			input.getline(engineNames[e], 256);
			printf("Engine #%i = %s\n", e, engineNames[e]);
		}
		
		input.getline(line, 256);
		numQueries = atoi(line);
		printf("numQueries = %i\n", numQueries);
		//load all queries
		for(int e = 0; e < numQueries; e++){
			input.getline(query[e], 256);
			printf("Query #%i = %s\n", e, query[e]);
		}
		
		int numSwitches = 0;
		int curQ = 0;
		while(curQ < numQueries){
			int luei = findLastUsedEngineIndex(engineNames, numEngines, query + curQ, numQueries - curQ);
			if(luei == -1){
				goto output;
			}
			curQ += luei;
			printf("switch needed\n");
			numSwitches ++;
		}
		output:
		int outputCase = c + 1;
		printf("Case #%i: %i\n", outputCase, numSwitches);
		outputFile << "Case #" << outputCase << ": " << numSwitches << "\n";
	}
	
	return 0;
}

int findLastUsedEngineIndex(char engineNames[][256], int numEngines, char query[][256], int numQueries){
	bool engineUsed[numEngines];
	initBool(engineUsed, numEngines, false);
	int numUsedEngines = 0;
	for(int q = 0; q < numQueries; q++){
		for(int e = 0; e < numEngines; e++){
			if(strcmp(query[q], engineNames[e]) == 0){
				if(engineUsed[e] == false){
					//printf("Engine not yet used\n");
					engineUsed[e] = true;
					numUsedEngines ++;
					if(numUsedEngines == numEngines){
						printf("q = %i\n", q);
						return q;
					}
				}
			}
		}
	}
	return -1;
}

void initBool(bool* bools, int numBools, bool val){
	for(int i = 0; i < numBools; i++){
		bools[i] = val;
	}
}
