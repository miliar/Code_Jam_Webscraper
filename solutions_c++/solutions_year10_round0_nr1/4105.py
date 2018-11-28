/*
 *  Snappers.cpp
 *  Snappers
 *
 *  Created by Brian Howald on 5/8/10.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fstream> 
#include <iostream>
#include "math.h"
using namespace std;


int main(int argc, char* argv[]) {
	
	
	char* inputFile = argv[1];
	char* outputFile = argv[2];
	
	int testCases = 7;
	
	int N;
	int K;

	ofstream os;
	os.open(outputFile);
	
	ifstream is;
	is.open(inputFile, ifstream::in);
	
	is >> testCases;
	
	for (int i = 1; i <= testCases; i++) {
		is >> N;
		is >> K;
		
		if (((K + 1) % (int)(pow((double)2, (double)N))) == 0) {
			os << "Case #" << i << ": ON" << endl;
		} else {
			os << "Case #" << i << ": OFF" << endl;
		}
	}
	
	os.close();
	
	return 0;
}
