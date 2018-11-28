/*
 * train.cpp
 *
 *  Created on: Jul 17, 2008
 *      Author: AliJ
 */

#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>



using namespace std;

int getMinutes(string s) {

	return atoi(s.substr(0,2).c_str())*60 + atoi(s.substr(3,2).c_str());

}

int howManyTrains(int *departures, int numDepartures, int *arrivals, int numArrivals) {

	int needed = 0;
	int curDep = 0;
	int curArr = 0;

	while ((curDep < numDepartures) && (curArr < numArrivals)) {

		if (departures[curDep] >= arrivals[curArr]) {
			curArr++;
		} else {
			needed++;
		}

		curDep++;
	}

	if (curDep < numDepartures)
		needed += numDepartures - curDep;


	return needed;

}

void processCase(int caseNum) {

	int numA, numB;
	numA = 0;
	numB = 0;

	int turnAround;
	cin >> turnAround;

	int tripsFromA, tripsFromB;

	cin >> tripsFromA;
	cin >> tripsFromB;

	int *departuresA = new int[tripsFromA];
	int *arrivalsA = new int[tripsFromB];

	int *departuresB = new int[tripsFromB];
	int *arrivalsB = new int[tripsFromA];


	string start, finish;
	int startMinutes, finishMinutes;

	for (int i = 0; i < tripsFromA; i++) {
		cin >> start;
		cin >> finish;
		startMinutes = getMinutes(start);
		finishMinutes = getMinutes(finish);

		departuresA[i] = startMinutes;
		arrivalsB[i] = finishMinutes + turnAround;
	}

	sort(departuresA, departuresA + tripsFromA);
	sort(arrivalsB, arrivalsB + tripsFromA);

	for (int j = 0; j <tripsFromB; j++) {
		cin >> start;
		cin >> finish;
		startMinutes = getMinutes(start);
		finishMinutes = getMinutes(finish);

		departuresB[j] = startMinutes;
		arrivalsA[j] = finishMinutes + turnAround;
	}

	sort(departuresB, departuresB + tripsFromB);
	sort(arrivalsA, arrivalsA + tripsFromB);

	numA = howManyTrains(departuresA, tripsFromA, arrivalsA, tripsFromB);
	numB = howManyTrains(departuresB, tripsFromB, arrivalsB, tripsFromA);



	cout << "Case #" << caseNum << ": " << numA <<  " " << numB << endl;

	delete [] departuresA;
	delete [] departuresB;
	delete [] arrivalsA;
	delete [] arrivalsB;
}


int main() {
	int numCases;

	cin >> numCases;


	for (int i = 0; i < numCases; i++) {
		processCase(i+1);
	}

	return 0;
}

