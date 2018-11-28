/*
 *  main.cpp
 *  SnapperChain
 *
 *  Created by Shobhit Gupta on 08/05/10.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */


#include <iostream.h>
//#include "genlib.h"
//#include "simpio.h"
#include <cmath>

#define HIGHEST_NUM_SNAPPER 26

void findAndDisplayResult(int testCaseId) {
	
	int numSnapper, timeSnapped;
	cin >> numSnapper >> timeSnapped;
	
	if (numSnapper > HIGHEST_NUM_SNAPPER) {
		cout << "Case #" << testCaseId << ": OFF" << endl;
	} else {
		// One more than actual minimum snaps required.
		long minSnapRequired = (long)pow(2.0, numSnapper);
		
		if (((timeSnapped + 1) % minSnapRequired) == 0) {
			cout << "Case #" << testCaseId << ": ON" << endl;
		} else {
			cout << "Case #" << testCaseId << ": OFF" << endl;
		}

	}

	
}

int main() {
	
	int testCases;
	cin >> testCases;
	
	for (int i = 0; i < testCases; i++) {
		findAndDisplayResult(i + 1);
	}
	
	return 0;
	
}

