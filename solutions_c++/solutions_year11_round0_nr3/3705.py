// CandySplitting.cpp : Defines the entry point for the console application.
//

#include <cstdio>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
using namespace std;
/* qsort int comparison function */ 
int int_cmp(const void *a, const void *b) 
{ 
	const int *ia = (const int *)a; // casting pointer types 
	const int *ib = (const int *)b;
	return *ia  - *ib; 
	/* integer comparison: returns negative if b > a 
	and positive if a > b */ 
} 
int main(int argc, char *argv[]) 
{
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);

	int T, i;
	scanf("%d", &T);

	int N, *inputArray, xorsum, run, addsum, result;

	run = 0;
	addsum = 0;
	while(scanf("%d", &N) != EOF) 
	{
		run ++;
		inputArray = new int[N];

		xorsum = 0;
		addsum = 0;
		for(i = 0; i< N; i++)
		{
			scanf("%d", &inputArray[i]);
			xorsum = xorsum ^ (inputArray[i]);
			addsum = addsum + (inputArray[i]);
		}

		if(xorsum != 0) {
			printf("Case #%d: NO\n", run);
		} else {
			qsort(inputArray, N, sizeof(int), int_cmp);
			result = addsum - inputArray[0];
			printf("Case #%d: %d\n", run, result);
		}

		delete[] inputArray;
	}


	//printf("3 & 5 & 6: %d\n", 3 ^ 5 ^ 6);
	//printf("5 & 4: %d\n", 5 ^ 4);
	//printf("7 & 9: %d\n", 7 ^ 9);
	//printf("50 & 10: %d\n", 50 ^ 10);
}