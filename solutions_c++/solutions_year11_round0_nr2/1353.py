// Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string.h>
#include <vector>

using namespace std;

struct stCombine
{
	char cSrc1;
	char cSrc2;
	char cDst;
};

struct stOpposed
{
	char cEle1;
	char cEle2;
};

void opposed(vector<char>& rvecEleList, vector<stOpposed>& rvecOpposed)
{
	size_t length = rvecEleList.size();
	if (length <2)
		return;

	char Ele1 = rvecEleList[length-1];

	vector<stOpposed>::iterator it = rvecOpposed.begin();
	while(it != rvecOpposed.end())
	{
		stOpposed& rstOpposed = *it;
		char Ele2 = '1';
		int flag = 0;

		if (Ele1 == rstOpposed.cEle1)
		{
			flag = 1;
			Ele2 = rstOpposed.cEle2;
		}

		if (Ele1 == rstOpposed.cEle2)
		{
			flag = 1;
			Ele2 = rstOpposed.cEle1;
		}

		if (flag)
		{
			for(int i=0;i<length-1;i++)
			{
				if (rvecEleList[i] == Ele2)
				{
					rvecEleList.clear();
					return;
				}
			}
		}

		it++;
	}
}

void combine(vector<char>& rvecEleList, vector<stCombine>& rvecCombine)
{
	size_t length = rvecEleList.size();
	if (length <2)
		return;

	char Ele1 = rvecEleList[length-1];
	char Ele2 = rvecEleList[length-2];

	vector<stCombine>::iterator it = rvecCombine.begin();
	while(it != rvecCombine.end())
	{
		stCombine& rstCombine = *it;

		if ( (Ele1 == rstCombine.cSrc1 && Ele2 == rstCombine.cSrc2) ||
			 (Ele2 == rstCombine.cSrc1 && Ele1 == rstCombine.cSrc2) )
		{
			rvecEleList.pop_back();
			rvecEleList.pop_back();

			rvecEleList.push_back(rstCombine.cDst);

			combine(rvecEleList, rvecCombine);
			return;
		}

		it++;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{

	int T;
	cin >> T;

	for(int i=0;i<T;i++)
	{
		vector<stCombine> vecCombine;
		vector<stOpposed> vecOpposed;

		int C;
		cin >> C;
		for(int j=0;j<C;j++)
		{
			stCombine Combine;

			cin >> Combine.cSrc1;
			cin >> Combine.cSrc2;
			cin >> Combine.cDst;

			vecCombine.push_back(Combine);
		}

		int D;
		cin >> D;
		for(int j=0;j<D;j++)
		{
			stOpposed Opposed;

			cin >> Opposed.cEle1;
			cin >> Opposed.cEle2;

			vecOpposed.push_back(Opposed);
		}

		vector<char> vecEleList;
		int N;
		cin >> N;
		for(int j=0;j<N;j++)
		{
			char cEle;
			cin >> cEle;
			vecEleList.push_back(cEle);

			// combine
			combine(vecEleList, vecCombine);

			// opposed
			opposed(vecEleList, vecOpposed);
		}

		printf("Case #%d: [", i+1);
		int length = vecEleList.size();
		for(int j=0;j<length;j++)
		{
			printf("%c", vecEleList[j]);
			if (j != length -1)
			{
				printf(", ");
			}
		}
		printf("]\n");
	}

	return 0;
}

