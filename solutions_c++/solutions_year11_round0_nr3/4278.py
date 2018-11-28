// CodejamCandy.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>

#define INPUT_FILE "large_input.txt"
//#define INPUT_FILE "small_input.txt"
#define OUTPUT_FILE "output.txt"
#define MAX_N 1000

int getSeanCandyNum();
inline int getXorSum(std::vector< int > vector);
inline int getSum(std::vector< int > vector);

FILE *fp;
FILE *fpout;
int* pInputCandyArray;
std::vector< int > vSean;
std::vector< int > vPatrick;

int main(int argc, char* argv[])
{
	fp = fopen(INPUT_FILE, "r");

	if(!fp) 
	{
		printf("Error : file input\n");
		return 0;
	}

	fpout = fopen(OUTPUT_FILE, "w");

	if(!fpout)
	{
		printf("Error : file output\n");
		return 0;
	}

	int T;	// num of test cases
	fscanf(fp, "%d", &T);

	int i;
	int candyNum = 0;
	int maxCandyNum = 0;

	pInputCandyArray = (int*)calloc(MAX_N, sizeof(int));

	for(i=0; i<T; i++)
	{
		candyNum = getSeanCandyNum();

		if(candyNum == -1)
			fprintf(fpout, "Case #%d: NO\n", i+1);
		else
			fprintf(fpout, "Case #%d: %d\n", i+1, candyNum);
	}

	fclose(fp);
	fclose(fpout);

	free(pInputCandyArray);

	return 0;
}

int getSeanCandyNum()
{
	int N;	// num of candies
	fscanf(fp, "%d", &N);
	
	int i, j;
	int tmpNum;
	for(i=0; i<N; i++)  
	{	
		fscanf(fp, "%d", &tmpNum);
		pInputCandyArray[i] = tmpNum;
	}

	int maxValue = -1;

	for(i=0; i<N; i++)
	{
		int xorSum = 0;
		int SeanSum = 0;

		for(j = 0; j < N; j++)
		{
			if(i != j)
			{
				xorSum = xorSum ^ pInputCandyArray[j];
				SeanSum = SeanSum + pInputCandyArray[j];
			}
		}

		if(xorSum == pInputCandyArray[i])
		{
			if(SeanSum > maxValue)
			{
				maxValue = SeanSum;
			} 
		}
	}

	return maxValue;
}

inline int getXorSum(std::vector< int > v)
{
	int sum = 0;

	for(int i=0; i<v.size(); i++)
	{
		sum = sum ^ v[i];
	}

	return sum;
}

inline int getSum(std::vector< int > v)
{
	int sum = 0;

	for(int i=0; i<v.size(); i++)
	{
		sum = sum + v[i];
	}

	return sum;
}

