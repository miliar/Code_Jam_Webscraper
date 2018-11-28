/*
 * q1.cpp
 *
 *  Created on: Jul 25, 2008
 *      Author: AliJ
 */



#include <iostream>
#include <string>
#include <algorithm>



using namespace std;

int processCase() {
	int n;
	cin >> n;
	int *x = new int[n];
	int *y = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> x[i];
	}

	for (int j = 0; j < n; j++) {
		cin >> y[j];
		y[j] *= -1;
	}
	sort(x, x+n);
	sort(y, y+n);

	int result = 0;

	for (int k = 0; k < n; k++) {
		result -= x[k]*y[k];
	}

	return result;
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
