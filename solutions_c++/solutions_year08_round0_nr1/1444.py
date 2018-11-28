/*
 * search.cpp
 *
 *  Created on: Jul 17, 2008
 *      Author: AliJ
 */

#include <iostream>
#include <string>



using namespace std;
int MAX_Q = 9999;
int processCase() {

	int numEngines;
	int numQueries;
	int prevBest, curBest;
	string junk;

	cin >> numEngines;
	getline(cin, junk);

	string *theEngines = new string[numEngines];
	int *theScores = new int[numEngines];

	for (int j = 0; j < numEngines; j++) {
		getline(cin, theEngines[j]);
		theScores[j] = 0;
	}


	cin >> numQueries;
	getline(cin, junk);


	prevBest = 0;
	curBest = 0;

	for (int i = 0; i < numQueries; i++) {
		string theQuery;
		getline(cin, theQuery);

		prevBest = curBest;
		curBest = MAX_Q;

		for (int k = 0; k < numEngines; k++) {
			if (theQuery == theEngines[k]) {
				theScores[k] = MAX_Q;
			} else if (theScores[k] == MAX_Q) {
				theScores[k] = prevBest+1;
			}

			if (theScores[k] < curBest)
				curBest = theScores[k];

		}
	}

	delete[] theEngines;
	delete[] theScores;


	return curBest;

}


int main() {
	int numCases;

	cin >> numCases;


	for (int i = 0; i < numCases; i++) {
		int result = processCase();
		cout << "Case #" << (i+1) << ": " << result << endl;
	}

	return 0;
}
