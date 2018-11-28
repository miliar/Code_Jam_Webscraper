#include <iostream>
#include <fstream>

#include <cmath>

using namespace std;

int allCnt;


int BuildReleasedList(bool isReleased[], int releaseList[], int n, int i, int releasedList[], int releaseListAll[][100])
{
	int j, cntSum;
	if (i == n)
	{
		for (j = 0; j < n; ++j)
		{
			releaseListAll[allCnt][j] = releasedList[j];
		}
		++allCnt;
	}
	else
	{
		for (j = 0; j < n; ++j)
		{
			if (!isReleased[j])
			{
				isReleased[j] = true;
				releasedList[i] = releaseList[j];
				BuildReleasedList(isReleased, releaseList, n, i + 1, releasedList, releaseListAll);
				isReleased[j] = false;
			}
		}
	}
	return allCnt;
}


int main()
{
	ifstream inputFile("input.txt");
	ofstream outputFile("output.txt");

	int T, X;

	int P, Q;

	int releaseList[100];
	int releasedList[100];

	bool isReleased[5];
	int releasedListAll[120][100];

	int biggerCellNum, smallerCellNum;
	int diffList[100];
	int sectorSizeList[100];
	int minDiff;

	int releasePrisonInd;
	int remainPrisonNum;
	int cost;
	int minCost;

	int allPossible;
	
	int i, j, k;

	inputFile>>T;
	for (X = 1; X <= T; ++X)
	{
		inputFile>>P>>Q;
		for (i = 0; i < Q; ++i)
		{
			inputFile>>releaseList[i];
			isReleased[i] = false;
		}

		allCnt = 0;
		allPossible = BuildReleasedList(isReleased, releaseList, Q, 0, releasedList, releasedListAll);

		minCost = P * Q;
		for (j = 0; j < allPossible; ++j)
		{
			cost = 0;
			for (i = 0; i < Q; ++i)
			{
				biggerCellNum = P + 1;
				for (k = 0; k < i; ++k)
					if (releasedListAll[j][k] > releasedListAll[j][i] && releasedListAll[j][k] < biggerCellNum)
						biggerCellNum = releasedListAll[j][k];
				smallerCellNum = 0;
				for (k = 0; k < i; ++k)
					if (releasedListAll[j][k] < releasedListAll[j][i] && releasedListAll[j][k] > smallerCellNum)
						smallerCellNum = releasedListAll[j][k];

				cost += biggerCellNum - smallerCellNum - 2;
			}
			if (cost < minCost)
				minCost = cost;
		}


		outputFile<<"Case #"<<X<<": "<<minCost<<endl;
	}

	inputFile.close();
	outputFile.close();
}
