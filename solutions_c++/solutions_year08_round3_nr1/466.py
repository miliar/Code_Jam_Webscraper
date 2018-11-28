//============================================================================
// Name        : a.cpp
// Author      : Aitor
// Version     :
// Copyright   : GNU!
// Description : Problem A for the google code jam
//============================================================================

#include <cstdio>
#include <algorithm>

#define PI 3.1415926535898

using namespace std;

int main()
{
	char inputFile[256], outputFile[256];
	FILE * inputF, *outputF;
	int N;

	strcpy(inputFile, "A-large.in");
	strcpy(outputFile, "A-large.out");

	//Load the input file:
	inputF = fopen(inputFile, "r+");
	outputF = fopen(outputFile, "w+");
	if(inputF == NULL)
	{
		printf("Input file not found!\n");
		return -1;
	}

	fscanf(inputF, "%d", &N);
	printf("Records: %d\n", N);

	//Loop to read the file
	for(int j = 1; j <= N; j++)
	{
		double result = 0;
		long n;
		long P, K, L;
		fscanf(inputF,"%ld %ld %ld", &P, &K, &L);
		
		long *letters = new long[L];
		for(int i = 0; i < L ; i++)
			fscanf(inputF,"%ld", &letters[i]);
		sort(letters, letters + L);
		if(P * K < L)
		{
			fprintf(outputF,"ERRRO!");
			return -1;
		}
		for(int i = L-1; i >= 0 ; i--)
		{
			int j = L - i -1;
			long position = (long)j / (long)K;
			result = result + (double)letters[i] * (double)(position+1);
		}

		printf("Case #%d: %lld\n", j, result);
		fprintf(outputF, "Case #%d: %.0f\n", j, result);
		delete [] letters;
	}
	fclose(inputF);
	fclose(outputF);
	
}
