// A1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	int numCases;
	int caseIter;

	fstream fin("C:\\A-small-attempt0(2).in");
	fin >> numCases;
	vector<int> frequencies;
	int places;
	int numKeys;
	int keyCounter;
	int placeCounter;
	int letters;
	int x, y;
	int counter;
	for(caseIter = 1; caseIter <= numCases; caseIter++) {
		fin >> places >> numKeys >> letters;
		frequencies.resize(0);
		for(x = 0; x < letters; x++) {
			fin >> y;
			frequencies.push_back(y);
		}
		sort(frequencies.rbegin(), frequencies.rend());
		placeCounter = 1;
		keyCounter = 0;
		counter = 0;
		for(x = 0; x < frequencies.size(); x++, keyCounter++) {
			if(keyCounter == numKeys) {
				placeCounter++;
				keyCounter = 0;
			}
			counter += frequencies[x]*placeCounter;
		}
		cout << "Case #" << caseIter << ": " << counter << "\n";
	}
	return 0;
}

