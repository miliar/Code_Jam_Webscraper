// ProblemC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#include <map>

using namespace std;
int R, K, N;
//__int64 nEarned = 0;


int GetRideCount(int& nStart, vector<int>& vGroups, map<int, pair<int, int>>& mpToRide, bool& bFound)
{
	int nToRide = 0;
	int nGroups = 0;
	map<int, pair<int, int>>::iterator itFound = mpToRide.find(nStart);
	if( itFound != mpToRide.end() )
	{
		nStart = itFound->second.second;
		bFound = true;
		return itFound->second.first;
	}
	else
	{
		int nCurStart = nStart;
		while( nToRide + vGroups[nStart] <= K )
		{
			nToRide += vGroups[nStart];
			nStart++;
			if( nStart >= N )
				nStart = 0;
			nGroups++;
			if( nGroups == N )
				break;
		}
		mpToRide.insert(make_pair(nCurStart, make_pair(nToRide, nStart)));
	}
	return nToRide;
}

int _tmain(int argc, _TCHAR* argv[])
{
	fstream in("C-large.in");//C-small-attempt0.in");
    ofstream out("C-large.out");//C-small-attempt0.out");
    string str;
    int  nTasks;
	in >> nTasks;

    for( int  iCount = 1; iCount <= nTasks; iCount++ )
    {
		in >> R >> K >> N;
		vector<int> vGroups(N);
		for( int k = 0; k < N; k++ )
			in >> vGroups[k];
		__int64 nEarned = 0;
		__int64 nEarnedCycle = 0;
		__int64 nEarnedCycleAll = 0;
		map<int, pair<int, int>> mpToRide;
		int i = 0;
		int j = 0;
		int nCycleCount = 0;
		bool bFound = false;
		for( ; j < R; j++ )
		{
			int Oldi = i;
			int nToRide = GetRideCount(i, vGroups, mpToRide, bFound);
			if( bFound )
			{
				map<int, pair<int, int>>::iterator itFound = mpToRide.find(Oldi);
				map<int, pair<int, int>>::iterator itFound2 = itFound;
				nCycleCount = 0;
				do
				{
					nEarnedCycle += itFound2->second.first;
					itFound2 = mpToRide.find(itFound2->second.second);
					nCycleCount++;
				}
				while( itFound != itFound2 );
				i = Oldi;
				break;
			}
			nEarnedCycleAll += nToRide;
		}
		if( nCycleCount == 0 )
			nCycleCount = j;
		int nFullCycles = ( R - j ) / nCycleCount;
		nFullCycles += 1;
		nEarned = nEarnedCycle * nFullCycles;
		for( j = nFullCycles * nCycleCount + j - nCycleCount; j < R; j++ )
		{
			nEarned += GetRideCount(i, vGroups, mpToRide, bFound);
		}
		nEarned += nEarnedCycleAll - nEarnedCycle;
		out<<"Case #"<< iCount <<": " << nEarned << '\n';
	}
	return 0;
}

