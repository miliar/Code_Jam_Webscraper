/*
 * q2.cpp
 *
 *  Created on: Aug 2, 2008
 *      Author: AliJ
 */


#include <iostream>

using namespace std;

long processCase(int i) {
	long A;
	long N;
	long M;

	cin >> N;
	cin >> M;
	cin >> A;

	long x2;
	long x3;
	long y2;
	long y3;
	//cout << "Processing " << endl;

	for (x2 = 0; x2 <= N; x2++) {
		for (y2 = 0; y2 <= M; y2++) {
			for (y3 = 0; y3 <= M; y3++) {
				//cout << "Inside" << endl;
				long firstProd = x2*y3;
				long diff = firstProd - A;
				if (y2 == 0) {
					if (firstProd == A) {
						x3 = 0;
						cout << "Case #" << (i+1) << ": 0 0 " << x2 << " " << y2 << " " << x3 << " " << y3  << endl;
					}
					continue;
				}
				if ((diff % y2) == 0) {
					x3 = diff/y2;
					if ((x3 >= 0) && (x3 <= N)) {
						//cout << "Returning" << endl;
						cout << "Case #" << (i+1) << ": 0 0 " << x2 << " " << y2 << " " << x3 << " " << y3  << endl;
						return 0;
					}
				}
				long sum = firstProd + A;
				if ((sum % y2)==0) {
					x3 = sum/y2;
					if ((x3 >= 0) && (x3 <= N)) {
						//cout << "REturnng" << endl;
						cout << "Case #" << (i+1) << ": 0 0 " << x2 << " " << y2 << " " << x3 << " " << y3  << endl;
						return 1;
					}
				}


			}
		}
	}

	cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
	return 2;
}

int main() {
	int numCases;

	cin >> numCases;


	for (int i = 0; i < numCases; i++) {
		processCase(i);
		//cout << "Case #" << (i+1) << ": " << result << endl;
	}

	return 0;
}

