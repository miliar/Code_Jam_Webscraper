// RecycledNumbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <windows.h>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

#define			InputFileName		"C-small-attempt0.in"
#define			OutputFileName		"C-small-attempt0.out"

bool checkRecycled(unsigned int n, unsigned int m, unsigned int range)
{
	bool ret = false;
	int temp = 0;

	for (int i = 0; i < range; i++)
	{
		temp = n % 10;
		n /= 10;
		n += temp * (int)pow((double)10, (double)(range - 1));
		if (m == n)
		{
			ret = true;
		}
	}

	return ret;
}

int _tmain(int argc, _TCHAR* argv[])
{
	// Initializing input/output
	ifstream	inputFile(InputFileName);
	ofstream	outputFile(OutputFileName);

	// Variables
	int			numberCases = 0;
	// Process variables
	unsigned int minRange = 0;
	unsigned int maxRange = 0;
	unsigned int result = 0;

	// Read input file
	inputFile >> numberCases;
	for (int i = 0; i < numberCases; i++)
	{
		result = 0;

		inputFile >> minRange;
		inputFile >> maxRange;

		for (int numberN = minRange; numberN <= maxRange; numberN++)
		{
			int nRange = 0;
			int fRange = numberN;
			int mRange = 0;
			do 
			{
				nRange++;
				fRange /= 10;
			} while (fRange > 0);

			mRange = min((int)pow((double)10, (double)nRange), maxRange + 1);

			if (numberN != (int)pow((double)10, (double)nRange) - 1)
			{
				for (int numberM = numberN + 1; numberM < mRange; numberM++)
				{
					if (checkRecycled(numberN, numberM, nRange))
					{
						result++;
					}
				}
			}
		}

		outputFile << "Case #" << i + 1 << ": " << result << endl;
	}

	return 0;
}

