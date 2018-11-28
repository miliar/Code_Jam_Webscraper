#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <fstream>

#include "Utilities.h"
#include "PrimeManager.h"

using namespace std;

int maxSean;
int candyNum;
int depth;
int sumOfAllCandies;
int realSumOfAllCandies;
vector<int> candies;
vector<int> bag;

void Backtracking(int index)
{
	if (bag.size() == depth)
	{
		//Stop
		int sumBagA = 0;
		int sumBagB = sumOfAllCandies;

		for (int j = 0;j < bag.size();j++)
		{
			sumBagA ^= candies[bag[j]];
			sumBagB ^= candies[bag[j]];
		}

		if (sumBagA == sumBagB)
		{
			int realSumBagA = 0;

			for (int j = 0;j < bag.size();j++)
			{
				realSumBagA += candies[bag[j]];
			}

			if (realSumBagA > realSumOfAllCandies / 2)
			{
				if (realSumBagA > maxSean)
				{
					maxSean = realSumBagA;
				}
			}
			else
			{
				if (realSumOfAllCandies - realSumBagA > maxSean)
				{
					maxSean = realSumOfAllCandies - realSumBagA;
				}
			}
		}
	}
	else
	{
		for (int i = index;i < candies.size();i++)
		{
			bag.push_back(index++);
			Backtracking(index);
			bag.pop_back();
		}
	}
}

int main()
{
    int cases;

    ifstream inputFileStream("G:\\GoogleCodeJam\\C-small-attempt0.in");
    ofstream ouputFileStream("G:\\GoogleCodeJam\\C-small-attempt0.out");

    while (inputFileStream >> cases)
    {
        for (int c = 0;c < cases;c++)
        {
			realSumOfAllCandies = 0;
			sumOfAllCandies = 0;
			candies.clear();

			inputFileStream >> candyNum;

			while (candyNum--)
			{
				int candy;

				inputFileStream >> candy;

				sumOfAllCandies ^= candy;
				realSumOfAllCandies += candy;

				candies.push_back(candy);
			}

			maxSean = -1;

			for (int i = 0;i < candies.size() / 2;i++)
			{
				depth = i + 1;
				Backtracking(0);
			}

			//Output
			if (maxSean != -1)
			{
				ouputFileStream << "Case #" << (c + 1) << ": " << maxSean << endl;
			}
			else
			{
				ouputFileStream << "Case #" << (c + 1) << ": NO" << endl;
			}
        }
    }

    return 0;
}