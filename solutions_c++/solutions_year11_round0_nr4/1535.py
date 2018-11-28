#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>

int CalcExpectedShuffles(int* numArr, int numInArr);

int CalcExpectedShuffles(int* numArr, int numInArr){
	int countOutofOrder = 0;
	for(int i = 0; i <numInArr; i++) {
		if(numArr[i] != i + 1) ++countOutofOrder;
	}
	return countOutofOrder;
}

int main(int argc, const char *argv[])
{
	
    FILE *op=fopen("D-large.in","r");
	FILE *np=fopen("GoroOutputLarge.txt","w");
    int numInArr,numCases = 0;
    int* numArr;
    fscanf(op,"%i",&numCases);
    for(int i = 1; i <=numCases; i++) {
		fscanf(op,"%i",&numInArr);
		numArr = (int*)malloc(4*numInArr);
		for(int j = 0; j <numInArr; j++) {
			fscanf(op,"%i\t", &numArr[j]) ;
		}
		int expected = CalcExpectedShuffles(numArr, numInArr);
		fprintf(np, "Case #%i: %f\n", i,(float)expected);
		free(numArr);
    }
    fclose(op);
	fclose(np);	
    return 0;
}
