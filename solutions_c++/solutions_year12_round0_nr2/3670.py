/*
 * driver.cpp
 *
 *  Created on: Apr 13, 2012
 *      Author: crand6
 */
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool evaluateScore(int totalScore, int bestResult, int& surprises)
{
	if(totalScore % 3 == 0)
	{
		if(totalScore == 0)
		{
			if(bestResult == 0)
				return true;
			else
				return false;
		}

		int individual = totalScore / 3;
		if(individual >= bestResult)
			return true;
		else if(individual + 1 >= bestResult)
		{
			if(surprises > 0)
			{
				surprises--;
				return true;
			}
			else
				return false;
		}
			return false;
	}

	if(totalScore % 3 == 1)
	{
		int individual = totalScore / 3;
		if(individual + 1 >= bestResult)
			return true;
		else
			return false;
	}

	if(totalScore % 3 == 2)
	{
		int individual = totalScore / 3;
		if(individual + 1 >= bestResult)
			return true;

		else if(individual + 2 >= bestResult)
		{
			if(surprises > 0)
			{
				surprises--;
				return true;
			}
			else
				return false;
		}
		else
			return false;
	}

	return false;
}

int main()
{
	int lineNum;

	ifstream inFile("B-large.in");
	ofstream outFile("B_LARGE_OUT.out");
	if(!inFile.is_open())
	{
		cout << "ERROR" << endl;
		return 1;
	}

	inFile >> lineNum;

	for(int i = 0; i < lineNum; i++)
	{
		int N, S, p;
		inFile >> N;
		inFile >> S;
		inFile >> p;
		//vector<int> scores;
		int finalAnswer = 0;

		//read in scores for googlers
		for(int n = 0; n < N; n++)
		{
			int temp;
			inFile >> temp;
			if(evaluateScore(temp, p, S))
			{
				finalAnswer++;
			}
		}

		outFile << "Case #" << i + 1 << ": ";
		outFile << finalAnswer << endl;
		//outFile << "N: " << N << endl;
		//outFile << "S: " << S << endl;
		//outFile << "p: " << p << endl;
	}

	cout << "done" << endl;

	return 0;
}
