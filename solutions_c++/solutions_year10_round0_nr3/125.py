#include "stdafx.h"
#include <vector>

using namespace std;

void PrintUsage(const char* exeName)
{
	cout << "Usage: " << exeName << " infile [outfile]" << endl;
}

int main(int argc, char* argv[])
{
	if (argc < 2)
	{
		PrintUsage(argv[0]);
		return -1;
	}
	string inName = argv[1];
	
	string outName = argc > 2 ? argv[2] : inName + ".out";
	
	ifstream inFile(inName);
	if (!inFile.is_open())
	{
		cout << "Bad input file: " << inName.c_str() << endl;
		return -2;
	}
	ofstream outFile(outName);
	if (!outFile.is_open())
	{
		cout << "Bad output file: " << outName.c_str() << endl;
		return -3;
	}

	int casesNumber;
	inFile >> casesNumber;
	if (inFile.fail())
	{
		cout << "Bad input data" << endl;
		return -4;
	}
	cout << "Number of cases: " << casesNumber;
	for (int i = 1; i <= casesNumber; ++i)
	{
		int rides; int capacity; int groupsNumber;
		inFile >> rides >> capacity >> groupsNumber;
		vector<int> group(groupsNumber);
		__int64 totalUsers = 0;
		for (int j = 0; j < groupsNumber; ++j)
		{
			int size;
			inFile >> size;
			group[j] = size;
			totalUsers += size;
		}
		if (inFile.fail())
		{
			cout << "Bad input data" << endl;
			return -4;
		}
		if (totalUsers <= capacity) //all groups could come aboard
		{
			outFile << "Case #" << i << ": " << totalUsers * rides << endl;
			continue;
		}

		vector<int> batch(groupsNumber);
		vector<int> nextGroup(groupsNumber, -1);
		int startIndex = 0;
		int endIndex = startIndex;
		int batchSize = 0;
		while (startIndex < groupsNumber)
		{
			int groupSize = group[endIndex];
			int newBatchSize = batchSize + groupSize;
			if (newBatchSize <= capacity)
			{
				batchSize = newBatchSize;
				++endIndex;
				endIndex %= groupsNumber;
				//endIndex == startIndex unreachable due to the fact totalUsers > capacity
			}
			else
			{
				if (startIndex == endIndex) //dead point. rides will stop here
					break;
				batch[startIndex] = batchSize;
				batchSize -= group[startIndex];
				nextGroup[startIndex] = endIndex;
				++startIndex;
			}
		}
		vector<int> visitedAfter(groupsNumber, -1);
		vector<__int64> hadMoney(groupsNumber);

		__int64 money = 0;
		int currentIndex = 0;
		for (int r = 0; r < rides;)
		{
			int beenThereAfter = visitedAfter[currentIndex];
			if (beenThereAfter == -1)
			{
				int batchSize = batch[currentIndex];
				if (batchSize == 0) //dead end
					break;
				visitedAfter[currentIndex] = r;
				hadMoney[currentIndex] = money;
				money += batchSize;
				currentIndex = nextGroup[currentIndex];
				++r;
			}
			else
			{
				//we have reached a loop
				int loopLength = r - beenThereAfter;
				int possibleLoopsLeft = (rides - beenThereAfter) / loopLength - 1;
				money += possibleLoopsLeft * (money - hadMoney[currentIndex]);
				r += loopLength * possibleLoopsLeft;
				visitedAfter.swap(vector<int>(groupsNumber, -1)); //clear the "visited" map to allow handling of a tail
			}
		}
		outFile << "Case #" << i << ": " << money << endl;
	}
	//todo: rest

	return 0;
}
