#pragma once
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <list>
#include <queue>
using namespace std;

class Problem1A
{
public:
	void Solve(const string& inputFileName, const string& outputFileName)
	{
		cout.precision(2);
		fstream inFile(inputFileName, ios::in);
		string curLine;
		inFile >> curLine;
		int totalLines = atoi(curLine.c_str());
		vector<double> result(totalLines);

		for(size_t i = 0; i < totalLines; ++i)
		{
			int A, B;
			inFile >> A >> B;
			vector<double> scores(A);
			for(size_t j = 0; j < scores.size(); ++j)
			{
				inFile >> scores[j];
			}

			result[i] = CalcMean(A, B, scores);
		}

		ofstream outFile(outputFileName);
		for(size_t i = 0; i < result.size(); ++i)
		{
			outFile << "Case #" << i + 1 << ": " << fixed << result[i] << endl;
		}
		return;
	}

	

	double CalcMean(int A, int B, const vector<double>& scores)
	{
		double product = 1;
		for(size_t i = 0; i < scores.size(); ++i)
		{
			product *= scores[i];
		}
		double keepTyping = (B - A + 1) * product + (B - A + 1 + B + 1) * (1 - product);
		double pressEnterRightAway = B + 2;
		double backspaceMin = 10000000;
		for(size_t step = 1; step <= A; ++step)
		{
			double lastkProbability = 1;
			double prev = 1;
			for(size_t i = 0; i < A - step; ++i)
			{
				prev *= scores[i];
			}
			
			for(int j = A - 1; A - 1 - j < step; --j)
			{
				lastkProbability *= scores[j];
			}

			double currentProbability = (B - A + 1 + 2 * step + B + 1) - (B + 1) * (prev * (1 - lastkProbability) + product);
			if(currentProbability < backspaceMin)
			{
				backspaceMin = currentProbability;
			}
		}

		return min(backspaceMin, min(keepTyping, pressEnterRightAway));
	}
};