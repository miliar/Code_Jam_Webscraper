/*
 * googleDancer.cpp
 *
 *  Created on: Apr 13, 2012
 *      Author: Danny
 */

#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int main(int argc, char* argv[])
{
	if(argc < 2)
	{
		cout << "Not enough arguments." << endl;
		return 1;
	}

	ifstream fin;
	fin.open(argv[1]);

	ofstream fout;
	fout.open("Output2.txt");

	if(!fin.is_open())
	{
		cout << "File open failed." << endl;
	}

	int numCases = 0, i, j, numDancers, numSurp, goalScore;

	int score, numGoal = 0, num, surpCount = 0, maxScore;

	fin >> numCases;

	cout << numCases << endl;

	for(i = 0; i < numCases; i++)
	{
		numGoal = 0;
		surpCount = 0;

		fout << "Case #" << i+1 << ": ";
		fin >> numDancers;
		fin >> numSurp;
		fin >> goalScore;

		for(j = 0; j < numDancers; j++)
		{
			fin >> score;

			num = score/3;
			if(num >= goalScore)
			{
				numGoal++;
				continue;
			}

			if(score == 0)
			{
				continue;
			}

			if(score % 3 == 0)//0 remainder
			{
				//max number is 1 over num
				if(surpCount < numSurp)
				{
					//can be surprising
					maxScore = num+1;

					if(maxScore >= goalScore)
					{
						surpCount++;
						numGoal++;
					}

				}
				else
				{
					continue;
				}
			}
			else if(score % 3 == 1)//1 remainder
			{
				//max number is 1 over num
				maxScore = num + 1;
				if(maxScore >= goalScore)
				{
					numGoal++;
				}
			}
			else//2 remainder
			{
				maxScore = num+1;
				if(maxScore >= goalScore)
				{
					numGoal++;
					continue;
				}

				if(surpCount < numSurp && num != 9)
				{
					//can be surprising
					maxScore = num+2;
					if(maxScore >= goalScore)
					{
						numGoal++;
						surpCount++;
					}
				}

			}

		}

		fout << numGoal;
		fout << endl;

		//cout << goalScore;

		if(surpCount != numSurp && goalScore == numGoal)
		{
			cout << i+1 << " " << surpCount << " " << numSurp << endl;
		}
	}
}


