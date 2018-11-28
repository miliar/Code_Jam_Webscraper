// PasswordProblem.cpp : Defines the entry point for the console application.
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

#define			InputFileName		"A-small-attempt0.in"
#define			OutputFileName		"A-small-attempt0.out"

vector <double> probA;
vector <double> probKeystroke;
int numA;
int numB;

void probCalculate(int pos, double prob)
{
	if (pos != (numA - 1))
	{
		probCalculate(pos + 1, prob*probA[pos]);
		probCalculate(pos + 1, prob*(1 - probA[pos]));
	}
	else
	{
		probKeystroke.push_back(prob*probA[pos]);
		probKeystroke.push_back(prob*(1 - probA[pos]));
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	// Initializing input/output
	ifstream	inputFile(InputFileName);
	ofstream	outputFile(OutputFileName);

	// Variables
	int			numberCases = 0;
	double		dTemp = 0.0;
	double		minKeystroke = 0;
	double		keyStroke = 0;
	int			iTemp1 = 0;
	int			iTemp2 = 0;
	int			iMask = 0;

	// Read input file
	inputFile >> numberCases;
	for (int i = 0; i < numberCases; i++)
	{
		// Clear
		probA.clear();
		probKeystroke.clear();
		minKeystroke = 100000;

		// Read
		inputFile >> numA;
		inputFile >> numB;

		for (int j = 0; j < numA; j++)
		{
			inputFile >> dTemp;
			probA.push_back(dTemp);
		}

		// Process
		probCalculate(0, 1);

		// Continue typing
		keyStroke = 0;
		keyStroke += (numB - numA + 1) * probKeystroke[0];
		for (int j = 1; j < probKeystroke.size(); j ++)
		{
			keyStroke += (numB*2 - numA + 2) * probKeystroke[j];
		}
		minKeystroke = (minKeystroke > keyStroke) ? keyStroke : minKeystroke;
		// Enter right away
		keyStroke = 0;
		keyStroke += (numB + 2);
		minKeystroke = (minKeystroke > keyStroke) ? keyStroke : minKeystroke;
		// Max back space
		keyStroke = 0;
		keyStroke += numA + (numB + 1);
		minKeystroke = (minKeystroke > keyStroke) ? keyStroke : minKeystroke;

		for (int j = 0; j < numA - 1; j++)
		{
			keyStroke = 0;
			iTemp1 = j + 1 + (numB - numA + j + 1) + 1;
			iTemp2 = iTemp1 + numB + 1;
			iMask = (int)pow((double)2, (double)j);
			for (int k = 0; k <= iMask; k++)
			{
				keyStroke += iTemp1 * probKeystroke[k];
			}
			for (int k = iMask + 1; k < probKeystroke.size(); k++)
			{
				keyStroke += iTemp2 * probKeystroke[k];
			}
			minKeystroke = (minKeystroke > keyStroke) ? keyStroke : minKeystroke;
		}
		outputFile.setf(ios::fixed,ios::floatfield);
		outputFile.precision(6);
		outputFile << "Case #" << i + 1 << ": " << minKeystroke << endl;
	}

	return 0;
}

