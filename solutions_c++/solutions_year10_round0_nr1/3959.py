#include <iostream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

// Libraries easily and freely downloadable from cs106b.stanford.edu
// Also, way easy to use.
#include "genlib.h"
#include "simpio.h"
#include "stack.h"
#include "vector.h"
#include "scanner.h"

string executeCase(FILE* fp);


string executeCase(FILE* fp) {
	unsigned long long N, K; //jic
	fscanf(fp, "%llu %llu\n", &N, &K);
	bool answer = true;
	for(unsigned long long i = 0; i < N; i++) {
		if (((K >> i) & 1) == 0) {
			answer = false;
		}
	}
	
	return (answer) ? "ON" : "OFF";
	
}


int main() {
	FILE* fp = fopen("A.in", "r");
	FILE* fpOut = fopen("A.out", "w");
	
	// get num cases
	int numCases;
	fscanf(fp, "%d", &numCases);
	// go go go!
	string answer;
	for (int i = 0; i < numCases; i++) {
		answer = executeCase(fp);
		fprintf(fpOut, "Case #%d: %s\n", i+1, answer.c_str());
	}
	
	fclose(fp);
	fclose(fpOut);
	return 0;
}