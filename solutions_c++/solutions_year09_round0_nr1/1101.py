// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <deque>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

void RemoveUnMatched(const string& sChoice, int iWhere, deque<string>& vTmp)
{
	deque<string>::iterator itBeg = vTmp.begin();

	for( ;itBeg != vTmp.end(); )
	{
		if( sChoice.find((*itBeg)[iWhere]) == string::npos )
			itBeg = vTmp.erase(itBeg);
		else
			++itBeg;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("A-large.in");//A-small-attempt0.in");
    ofstream out("A-large.out");//A-small-attempt0.out");
    int  iTasks;
	int L, D; 
	in >> L >> D;
	in >> iTasks;
	deque<string> vWords(D);
	for( int i = 0; i < D; i++ )
	{
		in >> vWords[i];
	}
    for( int  iCount = 1; iCount <= iTasks; iCount++ )
    {
		string sPattern;
		in >> sPattern;
		int iSymbol = 0;
		bool bOpen = false;
		string sChoice;
		deque<string> vTmp;
		vTmp.assign(vWords.begin(), vWords.end());
		for( size_t i = 0; i < sPattern.length(); i++ )
		{
			if( !bOpen )
				sChoice.clear();
			switch(sPattern[i])
			{
			case '(':
				bOpen = true;
				break;
			case ')':
				bOpen = false;
				break;
			default:
				sChoice += sPattern[i];
				break;
			}
			if( !bOpen )
			{
				RemoveUnMatched(sChoice, iSymbol, vTmp);
				iSymbol++;
			}
		}
		out<<"Case #"<< iCount <<": "<< vTmp.size() << '\n';
	}

	return 0;
}

