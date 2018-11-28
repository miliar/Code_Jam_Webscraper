#include <stdio.h>
#include <stdlib.h>
#include <cstring>

#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <list>

FILE* fp;
FILE* fout;

#define JAM_DEBUG

#define MAX_CHAR 100

#ifdef JAM_DEBUG
#define TEST_IN fp
#define TEST_OUT fout
#else
#define TEST_IN stdin
#define TEST_OUT stdout
#endif


std::multiset<int> AStartTime;
std::multiset<int> AEndTime;
std::multiset<int> BStartTime;
std::multiset<int> BEndTime;

int turntime;

int Input()
{
	int nNumA;
	int nNumB;
	
	AStartTime.clear();
	AEndTime.clear();
	BStartTime.clear();
	BEndTime.clear();

	fscanf(TEST_IN, "%d\n", &turntime);
	fscanf(TEST_IN, "%d %d\n", &nNumA, &nNumB);
	for (int i=0; i<nNumA; i++)
	{
		int h1,m1;
		int h2,m2;
		fscanf(TEST_IN, "%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
		AStartTime.insert(h1*60+m1);
		AEndTime.insert(h2*60+m2);
	}
	for (int i=0; i<nNumB; i++)
	{
		int h1,m1;
		int h2,m2;
		fscanf(TEST_IN, "%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
		BStartTime.insert(h1*60+m1);
		BEndTime.insert(h2*60+m2);
	}
	return 0;
}

int Compute(int& A, int& B)
{
	int nTrainInA = 0;
	std::multiset<int> StayInA;
	std::multiset<int>::iterator AIter;
	std::multiset<int>::iterator StayInAIter;
	std::multiset<int>::iterator BEndIter;
	for (AIter=AStartTime.begin(); AIter!=AStartTime.end(); AIter++)
	{
		int time = *AIter;

		while ((BEndIter=BEndTime.begin()) != BEndTime.end())
		{
			int arrivetime = *BEndIter;
			if (arrivetime <= time)
			{
				StayInA.insert(arrivetime + turntime);
				BEndTime.erase(BEndIter);
			}
			else
			{
				break;
			}
		}

		StayInAIter = StayInA.begin();
		if (StayInAIter != StayInA.end())
		{
			int readytime = *StayInAIter;
			if (readytime <= time)
			{
				StayInA.erase(StayInAIter);
				continue;
			}
		}
		nTrainInA++;
	}

	int nTrainInB = 0;
	std::multiset<int> StayInB;
	std::multiset<int>::iterator BIter;
	std::multiset<int>::iterator StayInBIter;
	std::multiset<int>::iterator AEndIter;
	for (BIter=BStartTime.begin(); BIter!=BStartTime.end(); BIter++)
	{
		int time = *BIter;

		while ((AEndIter=AEndTime.begin()) != AEndTime.end())
		{
			int arrivetime = *AEndIter;
			if (arrivetime <= time)
			{
				StayInB.insert(arrivetime + turntime);
				AEndTime.erase(AEndIter);
			}
			else
			{
				break;
			}
		}

		StayInBIter = StayInB.begin();
		if (StayInBIter != StayInB.end())
		{
			int readytime = *StayInBIter;
			if (readytime <= time)
			{
				StayInB.erase(StayInBIter);
				continue;
			}
		}
		nTrainInB++;
	}

	A = nTrainInA;
	B = nTrainInB;

	return 0;
}

int Program()
{
	int A,B;
	int nNumCase;
	fscanf(TEST_IN, "%d\n", &nNumCase);
	for (int i=0; i<nNumCase; i++)
	{
		Input();
		Compute(A,B);
		fprintf(TEST_OUT, "Case #%d: %d %d\n",i+1,A,B);
	}
	return 0;
}

int main()
{
	fp = fopen("B-large.in", "r");
	fout = fopen("output2.txt", "w");
	Program();
	fclose(fp);
	fclose(fout);
#ifdef JAM_DEBUG
	system("pause");
#endif
	return 0;
}

