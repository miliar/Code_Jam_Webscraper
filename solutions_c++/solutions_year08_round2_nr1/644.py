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

	strcpy(inputFile, "A-small.in");
	strcpy(outputFile, "A-small.out");

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
		long long result = 0;
		int n;
		int A, B, C, D, x0, y0, M;
		fscanf(inputF,"%d %d %d %d %d %d %d %d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		long long *X = new long long[n];
		long long *Y = new long long[n];
		X[0] = (long long)x0;
		Y[0] = (long long)y0;
		for(int i = 1; i < n; i++)
		{
			X[i] = (long long)(A * X[i-1] + B) % (long long)M;
			Y[i] = (long long)(C * Y[i-1] + D) % (long long)M;
		}

		for(int i = 0; i < n; i++)
		{
			printf("%lld , %lld\n", X[i], Y[i]);
		}
		
		for(int i = 0; i < n; i++)
		{
			for(int k = i + 1; k < n; k++)
			{
				for(int l = k + 1; l < n; l++)
				{
					long long xc, yc;
					xc = ((X[i] + X[k] + X[l]) / 3);
					yc = ((Y[i] + Y[k] + Y[l]) / 3);
					double xcd, ycd;
					xcd = (((double)X[i] + (double)X[k] + (double)X[l]) / 3.0);
					ycd = (((double)Y[i] + (double)Y[k] + (double)Y[l]) / 3.0);
					if((double)xc == xcd && (double)yc == ycd)
						result++;
				}
			}
		}

		printf("Case #%d: %lld\n", j, result);
		fprintf(outputF, "Case #%d: %lld\n", j, result);
		delete [] X;
		delete [] Y;
	}
	fclose(inputF);
	fclose(outputF);
	
}
