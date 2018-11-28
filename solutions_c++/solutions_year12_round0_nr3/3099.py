// QualificationC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>

using namespace std;
map<pair<int, int>, int> mpMap;

void GetPairs(int nStart, int nEnd)
{
	int Number = nStart;
	vector<int> vDigits;
	while( Number > 0 )
	{
		vDigits.push_back(Number%10);
		Number /= 10;
	}
	reverse(vDigits.begin(), vDigits.end());
	vector<int> vNewNumbers;
	for( size_t j = 0; j < vDigits.size(); j++ )
	{
		int nNewNumber = 0;
		int nMult = 1;
		for( size_t i = vDigits.size(); i > 0; i-- )
		{
			nNewNumber += vDigits[i - 1] * nMult;
			nMult *= 10;
		}
		if( nNewNumber > nStart && nNewNumber <= nEnd )
			mpMap[make_pair(nStart, nNewNumber)] = 1;
		rotate(vDigits.begin(), vDigits.begin ( ) + 1, vDigits.end());
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("C-small-attempt0.in");
    ofstream out("C-small-attempt0.out");

	//ifstream in("C-large.in");
 //   ofstream out("C-large.out");

    int iTasks;
	in >> iTasks;
	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		mpMap.clear();
		int A, B;
		in >> A >> B;
		int nPairs = 0;
		for ( int i = A; i <= B; i++ )
		{
			GetPairs(i, B);
		}
		nPairs = mpMap.size();
		out << "Case #" << iCount << ": " << nPairs << endl;
	}
	return 0;
}