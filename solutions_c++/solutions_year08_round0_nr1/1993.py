// SearchEngine.cpp : Defines the entry point for the console application.
//
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

struct testcase {
	vector<string> engines;
	vector<string> queries;
};

vector<testcase> readInput(char *fileName) {
	vector<testcase>testCases;
	fstream fp;
	int nCases = 0, nEngines = 0, nQueries = 0;
	fp.open(fileName, ios::in);
	fp>>nCases;
	for (int i=0; i<nCases; i++) {

		testcase newCase;

		fp>>nEngines;
		vector<string> engines;
		string engineName;
		getline(fp, engineName);
		for (int j=0; j<nEngines; j++) {			
			getline(fp, engineName);
			newCase.engines.push_back(engineName);
		}

		fp>>nQueries;
		string query;
		getline(fp, query);
		for (int k=0; k<nQueries; k++) {
			getline(fp, query);
			newCase.queries.push_back(query);
		}

		testCases.push_back(newCase);
	}
	return testCases;
}

int processTestCase(testcase t) {

	int nSwitches = 0;
	int foundIndex = -1;

	bool entryTable[100];
	unsigned int count = 0;
	while (count < t.queries.size()) {
		for(unsigned int i=0; i<t.engines.size(); i++) {
			entryTable[i] = false;
		}
		unsigned int foundCount = 0;
		if (foundIndex != -1) {
			entryTable[foundIndex] = true;
			foundCount = 1;
		}

		for(unsigned int j = count; j< t.queries.size(); j++) {
			for(unsigned int k=0; k< t.engines.size(); k++) {
				if (t.queries[j] == t.engines[k] ) {
					if (entryTable[k] == false) {
						entryTable[k] = true;
						foundCount ++;
						foundIndex = k;
					}
					break;
				}
			}
			if (foundCount >= t.engines.size() ) {
				count = j+1;
				break;
			}
		}
		if(foundCount<t.engines.size() )
			break;
		nSwitches ++ ;
	}

	return nSwitches;
}

int main(int argc, char* argv[]) {
	vector<testcase> myTestCases = readInput("C:\\setest.txt");
	fstream fout;
	fout.open("c:\\seout.txt", ios::out);
	for(unsigned int i=0; i < myTestCases.size();  i++) {
		int r = processTestCase(myTestCases[i]) ;
		 cout << "Case #"<<i+1<< ": "<< r <<endl;
		 fout << "Case #"<<i+1<< ": "<< r <<endl;
	}
}
