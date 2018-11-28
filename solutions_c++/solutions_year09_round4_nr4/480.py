#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <assert.h>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
#include <math.h>

#define INDEX_MAX 41 

using namespace std;

int X[100];
int Y[100];
int R[100];

///////////////////////

double dist(int p1, int p2) {
	int diff1 = X[p1]-X[p2];
	int diff2 = Y[p1]-Y[p2];
	double d = sqrt(diff1*diff1+diff2*diff2); 
	return d;
}

//////////////////////
int main () {
	int nCases = 0;
	scanf("%d",&nCases);
	
	for (int caseNum = 1; caseNum <= nCases; caseNum++) {
		int nPlants;
		scanf("%d",&nPlants);
		
		for (int p = 0; p < nPlants; p++) {
			scanf("%d %d %d", &X[p],&Y[p],&R[p]);
		}
		
		double min;
		if (nPlants == 3) {
			double d2 = (dist(0,1)+R[0]+R[1])/2;
			if (d2 < R[2])
				d2 = R[2];

			double d1 = (dist(0,2)+R[0]+R[2])/2;
			if (d1 < R[1])
				d1 = R[1];
	
			double d0 = (dist(1,2)+R[1]+R[2])/2;
			if (d0 < R[0])
				d0 = R[0];
	
			min = d2;
			if (d1 < min)
				min = d1;
			if (d0 < min)
				min = d0;
		} else if (nPlants == 2) {
			min = R[0];
			if (R[1] > min)
				min = R[1];
		} else {
			min = R[0];	
		}
		printf("Case #%d: %.9f\n",caseNum,min);
	}
}
