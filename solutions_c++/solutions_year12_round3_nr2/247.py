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

class Problem2_1C
{
public:
	void Solve(const string& inputFileName, const string& outputFileName)
	{
		cout.precision(2);
		fstream inFile(inputFileName, ios::in);
		string curLine;
		inFile >> curLine;
		int totalLines = atoi(curLine.c_str());
		vector<vector<double>> result(totalLines);

		for(size_t i = 0; i < totalLines; ++i)
		{
			double D;
			int N, A;
			inFile >> D >> N >> A;
			
			vector<pair<double, double>> coordinates(N);
			vector<double> accelerations(A);

			for(size_t j = 0; j < N; ++j)
			{
				pair<double, double> c;
				inFile >> c.first >> c.second;
				coordinates[j] = c;
			}

			for(size_t j = 0; j < A; ++j)
			{
				inFile >> accelerations[j];
			}

			result[i] = CalcAccelerations(D, coordinates, accelerations);
		}

		ofstream outFile(outputFileName);
		outFile.precision(7);
		for(size_t i = 0; i < result.size(); ++i)
		{
			outFile << "Case #" << i + 1 << ":" << endl;
			for(size_t j = 0; j < result[i].size(); ++j)
			{
				outFile << fixed << result[i][j] << endl;
			}
		}
		return;
	}

	vector<double> CalcAccelerations(double D, const vector<pair<double, double>>& coordinates, const vector<double>& accelerations)
	{
		vector<double> result(accelerations.size());
		for(size_t i = 0; i < accelerations.size(); ++i)
		{
			result[i] = CalcForSingleAcceleration(D, coordinates, accelerations[i]);
		}
		return result;
	}

	double CalcForSingleAcceleration(double D, const vector<pair<double, double>>& c, double a)
	{
		double time = 0;
		double prevVelocity = 0;
		double prevStoppedDistance = 0;

		if(c.size() == 1)
		{
			return sqrt(2 * D / a);
		}
		
		for(size_t i = 1; i < c.size(); ++i)
		{
			double curDistance = c[i].second;
			if(curDistance < D)
			{

				double myArrive = ((sqrt(prevVelocity * prevVelocity + 2 * a * (curDistance - prevStoppedDistance)) - prevVelocity) / a) + time;
				if(myArrive <= c[i].first)//Если я раньше догнал
				{
					time = c[i].first;
					prevVelocity = (c[i].second - c[i-1].second)/(c[i].first - c[i - 1].first);
					prevStoppedDistance = curDistance;
				}
				continue;
			}

			if(curDistance >= D)
			{
				double velocity = (c[i].second - c[i-1].second)/(c[i].first - c[i - 1].first);
				double arrive = (D - c[i - 1].second)/velocity + c[i-1].first;
				double myArrive = ((sqrt(prevVelocity * prevVelocity + 2 * a * (D - prevStoppedDistance)) - prevVelocity) / a) + time;

				return max(arrive, myArrive);
			}
		}
		return time;
	}
};