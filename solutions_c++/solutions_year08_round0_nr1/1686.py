// Saving the Universe.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
#include "stdafx.h"

using namespace std;
int findIn(string toFind, vector<string>& vec, vector<int>& truthArray) {
	int x;
	int found = 0;
	for(x = 0; x < vec.size(); x++) {
		if(toFind == vec[x]) {
			found = 1;
			truthArray[x] = 1;
		}
	}
	return found;
}

int allOne(vector<int>& vec) {
	int x;
	for(x = 0; x < vec.size(); x++) {
		if(0 == vec[x]) return 0;
	}
	return 1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int numCases, caseIter;
	int numSearchEngines, numSearches;
	int iter;
	int num_switches = 0;
	int posn;
	ifstream fin;
	fin.open("C:\\A-large.in", ifstream::in);
	fin>>numCases;
	int iter2;
	vector<string> searchEngines;
	vector<string> searches;
	vector<int> truthArray;
	string lastitem;
	string input;
	for(caseIter=1; caseIter <= numCases; caseIter++) {
		fin >> numSearchEngines;
		truthArray.resize(numSearchEngines);
		searchEngines.resize(0);
		searches.resize(0);
		fin.ignore(255, '\n');
		for(iter = 1; iter <= numSearchEngines; iter++) {
			getline(fin, input);
			searchEngines.push_back(input);
		}
		fin >> numSearches;
		fin.ignore(255, '\n');
		for(iter = 1; iter <= numSearches; iter++) {
			getline(fin, input);
			searches.push_back(input);
		}

		for(iter = 0; iter < numSearchEngines; iter++) {
			truthArray[iter] = 0;
		}
		num_switches = 0;
		lastitem = "";
		//keep on finding
		iter=0;
		while(iter < numSearches) {
			if(findIn(searches[iter], searchEngines, truthArray)) {
				if(allOne(truthArray)) {
					for(iter2 = 0; iter2 < numSearchEngines; iter2++) {
						truthArray[iter2] = 0;
					}
					num_switches++;
					lastitem = searches[iter];
					findIn(lastitem, searchEngines, truthArray);
				}
			}
			
			iter++;
		}
		cout << "Case #" << caseIter << ": " << num_switches << "\n";
	}

	return 0;
}

