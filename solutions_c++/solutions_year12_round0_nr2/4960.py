// DancingWithTheGooglers.cpp : Defines the entry point for the console application.
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

#define			InputFileName		"B-small-attempt0.in"
#define			OutputFileName		"B-small-attempt0.out"

struct GooglersScoreType 
{
	unsigned int totalScore;
	unsigned int maxNoSurprising;
	unsigned int maxSurprising;
	bool isSurprising;
	bool canBeatMinBest;
	bool isTaken;
};

void BubbleSort(vector<GooglersScoreType> &num, int Select)
{
	int i, j, flag = 1;		// set flag to 1 to start first pass
	GooglersScoreType temp; // holding variable
	int numLength = num.size(); 

	if (Select == 1)
	{
		for(i = 1; (i <= numLength) && flag; i++)
		{
			flag = 0;
			for (j=0; j < (numLength -1); j++)
			{
				if (num[j+1].maxNoSurprising > num[j].maxNoSurprising)      
				{ 
					temp = num[j];          
					num[j] = num[j+1];
					num[j+1] = temp;
					flag = 1;               
				}
			}
		}
	}
	else
	{
		for(i = 1; (i <= numLength) && flag; i++)
		{
			flag = 0;
			for (j=0; j < (numLength -1); j++)
			{
				if (num[j+1].maxSurprising < num[j].maxSurprising)      
				{ 
					temp = num[j];          
					num[j] = num[j+1];
					num[j+1] = temp;
					flag = 1;               
				}
			}
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	// Initializing input/output
	ifstream	inputFile(InputFileName);
	ofstream	outputFile(OutputFileName);

	// Variables
	int			numberCases = 0;
	// Process variables
	unsigned int numberGooglers = 0;
	unsigned int numberSurprisingScores = 0;
	unsigned int minBestScore = 0;
	unsigned int numberTaken = 0;
	GooglersScoreType GooglersScore[100];
	vector <GooglersScoreType> filterGooglersScore;

	unsigned int result = 0;

	// Read input file
	inputFile >> numberCases;
	for (int i = 0; i < numberCases; i++)
	{
		memset(GooglersScore, 0, sizeof(GooglersScore));
		filterGooglersScore.clear();
		numberTaken = 0;
		result = 0;

		inputFile >> numberGooglers;
		inputFile >> numberSurprisingScores;
		inputFile >> minBestScore;

		for (int j = 0; j < numberGooglers; j++)
		{
			inputFile >> GooglersScore[j].totalScore;
			
			if (GooglersScore[j].totalScore % 3 == 2)
			{
				GooglersScore[j].maxNoSurprising = GooglersScore[j].totalScore / 3 + 1;
				GooglersScore[j].maxSurprising = GooglersScore[j].totalScore / 3 + 2;
			}
			else if (GooglersScore[j].totalScore % 3 == 1)
			{
				GooglersScore[j].maxNoSurprising = GooglersScore[j].totalScore / 3 + 1;
				GooglersScore[j].maxSurprising = GooglersScore[j].totalScore / 3 + 1;
			}
			else
			{
				GooglersScore[j].maxNoSurprising = GooglersScore[j].totalScore / 3;
				GooglersScore[j].maxSurprising = GooglersScore[j].totalScore / 3 + 1;
			}

			if (GooglersScore[j].totalScore == 0)
			{
				GooglersScore[j].maxNoSurprising = 0;
				GooglersScore[j].maxSurprising = 0;
			}

			if (max(GooglersScore[j].maxNoSurprising, GooglersScore[j].maxSurprising) >= minBestScore) 
			{
				GooglersScore[j].canBeatMinBest = true;
				filterGooglersScore.insert(filterGooglersScore.begin(), GooglersScore[j]);
			}
		}

		if (numberSurprisingScores >= filterGooglersScore.size())
		{
			result = filterGooglersScore.size();
		}
		else
		{
			// Sort MaxSurprise
			BubbleSort(filterGooglersScore, 2);
			for (int j = 0; j < filterGooglersScore.size(); j++)
			{
				if ((filterGooglersScore[j].maxSurprising >= minBestScore) && (numberTaken < numberSurprisingScores))
				{
					result++;
					numberTaken++;
					filterGooglersScore[j].isTaken = true;
				}
			}

			// Sort MaxNoSurprise
			BubbleSort(filterGooglersScore, 1);
			for (int j = 0; j < filterGooglersScore.size(); j++)
			{
				if ((filterGooglersScore[j].maxNoSurprising >= minBestScore) && (!filterGooglersScore[j].isTaken))
				{
					result++;
					filterGooglersScore[j].isTaken = true;
				}
			}
		}

		outputFile << "Case #" << i + 1 << ": " << result << endl;
	}

	return 0;
}

