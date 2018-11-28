#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <new>
#include <cassert>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

#define N 1000

struct circleSort {
	int radius;
	int index;
};

bool mySort(circleSort a, circleSort b) { return (a.radius > b.radius); }



int main(void) {	
	int numCases;
	cin >> numCases;
	
	int circles, width, length;
	int i, isLengthWidthSwapped, index, cutx, cuty, newCutx, oldCuty, consumedY;
	int *radius, *posx, *posy;
	circleSort *cs;
	
	radius = new int[N];
	posx = new int[N];
	posy = new int[N];
	cs = new circleSort[N];
	
	for (int caseNum = 1; caseNum <= numCases; caseNum++) {
		cin >> circles >> width >> length;
		for (i=0; i<circles; i++) cin >> radius[i];
		for (i=0; i<circles; i++) {
			cs[i].radius = radius[i];
			cs[i].index = i;
		}
		sort(cs, &(cs[circles]), mySort);
		
		isLengthWidthSwapped = 0;
		if (length < width) {
			swap(length, width);
			isLengthWidthSwapped = 1;
		}
		
		//place as boxes
		//top surface
		index = cs[0].index;	//put largest circle at top left corner
		posx[index] = 0;
		posy[index] = 0;
		cutx = radius[index];
		cuty = radius[index];
		if (cuty > width) cuty = width;
		//working within cuty from the top, place boxes along x
		i = 1;
		while (i<circles && cutx+radius[cs[i].index] <= length) {
			//place along top
			index = cs[i].index;
			posx[index] = cutx + radius[index];
			posy[index] = 0;
			newCutx = cutx + 2*radius[index];
			consumedY = radius[index];
			i++;
			while (i<circles && 2*radius[cs[i].index]+consumedY <= cuty) {
				index = cs[i].index;
				posx[index] = cutx + radius[index];
				posy[index] = consumedY + radius[index];
				consumedY += 2*radius[index];
				i++;
			}
			cutx = newCutx;
		}
		
		//work with new top surface, note can't go off the top anymore
		oldCuty = cuty;
		while (i<circles) {
			index = cs[i].index;
			posx[index] = 0;
			posy[index] = oldCuty + radius[index];
			cutx = radius[index];
			cuty = oldCuty + 2*radius[index];
			i++;
			//go across
			while (i<circles && cutx+radius[cs[i].index] <= length) {
				index = cs[i].index;
				posx[index] = cutx + radius[index];
				posy[index] = oldCuty + radius[index];
				newCutx = cutx + 2*radius[index];
				consumedY = oldCuty + 2*radius[index];
				i++;
				//go down within cutx to newCutx
				while (i<circles && 2*radius[cs[i].index]+consumedY <= cuty) {
					index = cs[i].index;
					posx[index] = cutx + radius[index];
					posy[index] = consumedY + radius[index];
					consumedY += 2*radius[index];
					i++;
				}
				cutx = newCutx;
			}
			oldCuty = cuty;
		}
		
		//check that all y coordinates are within width
		for (i=0; i<circles; i++) if (posy[i] > width || posx[i] > length) {
			fprintf(stderr, "failed case %d, circle index %d, radius %d, posx %d, posy %d\n", caseNum, i, radius[i], posx[i], posy[i]);
			exit(1);
		}
		
		//*
		int j, dx, dy, sumR;
		for (i=0; i<circles; i++) for (j=i+1; j<circles; j++) {
			dx = abs(posx[i]-posx[j]);
			dy = abs(posy[i]-posy[j]);
			sumR = radius[i]+radius[j];
			if (dx < sumR && dy < sumR) {
				fprintf(stderr, "case %d\n", caseNum);
				fprintf(stderr, "fail i %d, j %d, x %d %d, y %d %d, r %d %d\n", i, j, posx[i], posx[j], posy[i], posy[j], radius[i], radius[j]);
				exit(1);
			}
		}
		// */
		
		
		
		printf("Case #%d:", caseNum);
		if (isLengthWidthSwapped==1) {
			for (i=0; i<circles; i++) printf(" %.1lf %.1lf", (double)posx[i], (double)posy[i]);
		}
		else {
			for (i=0; i<circles; i++) printf(" %.1lf %.1lf", (double)posy[i], (double)posx[i]);
		//	for (i=0; i<circles; i++) printf(" %d %d", posy[i], posx[i]);
		}
		printf("\n");
	}
	
	
	return 0;
}
