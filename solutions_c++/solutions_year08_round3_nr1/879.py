#include <stdio.h>
#include <tchar.h>
#include <string>
#include <math.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std ;
typedef pair<int, int> INTPAIR ;
typedef vector<INTPAIR> INTPAIRVECTOR ;

bool sorter(INTPAIR& rhs, INTPAIR& lhs)
{
	return rhs.second < lhs.second ;
}
//
bool sorter1(INTPAIR& rhs, INTPAIR& lhs)
{
	return rhs.first > lhs.first ;
}
//
int SolveCase(ifstream& fpIn)
{
	int p, k, l ;
	fpIn >> p >> k >> l ;
	INTPAIRVECTOR frequencies, keys ;
	int freq ;
	for(int i = 0; i < l; ++i)
	{
		fpIn >> freq ;
		frequencies.push_back(INTPAIR(freq, 0)) ;
	}
	sort(frequencies.begin(), frequencies.end(), sorter1) ;
	//
	for(int i = 0; i < k; ++i)
		keys.push_back(pair<int, int>(i, 1)) ;
	int n = 0 ;
	for(int i = 0; i < l; ++i)
	{
		sort(keys.begin(), keys.end(), sorter) ;
		frequencies[i].second = keys[0].second++ ;
		n += frequencies[i].first * frequencies[i].second ;
	}
	return n ;
}
//
int _tmain(int argc, _TCHAR* argv[])
{
	if(argc == 1)
	{
		printf("Usage: exe inputfile\n") ;
		return 0 ;
	}

	ifstream fpIn(argv[1], ios::in) ;
	if(fpIn.is_open())
	{
		int nCases ;
		fpIn >> nCases ;
		string szOut = argv[1] ;
		szOut += ".out" ;
		ofstream fpOut(szOut.c_str()) ;
		for(int i = 0; i < nCases; ++i)
			fpOut << "Case #" << i+1 << ": " << SolveCase(fpIn) << endl ;
	}

	return 0;
}

