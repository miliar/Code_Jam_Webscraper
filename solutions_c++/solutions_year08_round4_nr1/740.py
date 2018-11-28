/*
 * q1.cpp
 *
 *  Created on: Aug 2, 2008
 *      Author: AliJ
 */

#include <iostream>
#include <vector>

using namespace std;

long howMany(vector<int> nodeGates, vector<int> changeable, vector<int> values, int want, int index) {
	if (values[index] == want) {
		//cout << "index: " << index << " numChanges " << "0" << endl;
		return 0;
	} else if ((unsigned int) index >= (values.size() -1)/2) {
		//cout << "index: " << index << " numChanges " << "20000" << endl;
		return 20000;
	}

	long numChanges = 0;

	if (changeable[index] == 1) {
		if ((want == 0) && (nodeGates[index] == 0)) {
			numChanges = 1;
			numChanges += min(howMany(nodeGates, changeable, values, 0, 2*index+1),
								   howMany(nodeGates, changeable, values, 0, 2*index+2));
		} else if (want == 0) {
			numChanges += min(howMany(nodeGates, changeable, values, 0, 2*index+1),
					   howMany(nodeGates, changeable, values, 0, 2*index+2));
		} else if ((want == 1) && (nodeGates[index] == 1)) {
			numChanges = 1;
			numChanges += min(howMany(nodeGates, changeable, values, 1, 2*index+1),
					   howMany(nodeGates, changeable, values, 1, 2*index+2));
		} else {
			numChanges += min(howMany(nodeGates, changeable, values, 1, 2*index+1),
								   howMany(nodeGates, changeable, values, 1, 2*index+2));
		}
	} else {
		if ((want == 0) && (nodeGates[index]== 0)) {
			numChanges += howMany(nodeGates, changeable, values, 0, 2*index+1) +
			   howMany(nodeGates, changeable, values, 0, 2*index+2);
		} else if (want == 0) {
			numChanges += min(howMany(nodeGates, changeable, values, 0, 2*index+1),
								   howMany(nodeGates, changeable, values, 0, 2*index+2));
		} else if ((want == 1) && (nodeGates[index]== 1)) {
			numChanges += howMany(nodeGates, changeable, values, 1, 2*index+1)+
											   howMany(nodeGates, changeable, values, 1, 2*index+2);
		} else {
			numChanges += min(howMany(nodeGates, changeable, values, 1, 2*index+1),
											   howMany(nodeGates, changeable, values, 1, 2*index+2));
		}
	}
	//cout << "index: " << index << " numChanges " << numChanges << endl;
 	return min(numChanges, (long) 20000);
}

long processCase(int i) {
	int numNodes;
	int wantValue;

	cin >> numNodes;
	cin >> wantValue;

	vector<int> nodeGates;;
	vector<int> changeable;
	vector<int> values;
	int j;
	for (j = 0; j < (numNodes - 1)/2; j++) {
		int gateType;
		int canChange;
		cin >> gateType;
		cin >> canChange;
		nodeGates.push_back(gateType);
		changeable.push_back(canChange);
		values.push_back(0);
	}

	for (; j < numNodes; j++) {
		int gateVal;
		cin >> gateVal;
		values.push_back(gateVal);
	}

	//evaluate circuit.
	for (j = (numNodes-1)/2 - 1; j >=0; j--) {
		if ((nodeGates[j]-values[2*j+1] - values[2*j+2]) < 0)
			values[j] = 1;
		else
			values[j] = 0;
	}

	//done?
	if (values[0] == wantValue) {
		return 0;
	}


	return howMany(nodeGates, changeable, values, wantValue, 0);
}

int main() {
	int numCases;

	cin >> numCases;


	for (int i = 0; i < numCases; i++) {
		long result = processCase(i);
		if (result < 20000) {
			cout << "Case #" << (i+1) << ": " << result << endl;
		} else {
			cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
