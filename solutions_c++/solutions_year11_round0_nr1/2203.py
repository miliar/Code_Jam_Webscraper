// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	//ifstream in("A-small-attempt0.in");
 //   ofstream out("A-small-attempt0.out");

	ifstream in("A-large.in");
    ofstream out("A-large.out");

    int iTasks;
	in >> iTasks;
	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		int nOPos = 1, nBPos = 1, nSeconds = 0;
		int nLastBTime = 0, nLastOTime = 0;
		int nSteps;
		in >> nSteps;
		char c;
		for( int i = 0; i < nSteps; i++ )
		{
			
			in >> c;
			int nNextBtn;
			in >> nNextBtn;
			if( c == 'O' )
			{
				nLastOTime += abs(nNextBtn - nOPos) + 1; 
				if( nLastBTime >= nLastOTime )
					nLastOTime = nLastBTime + 1;
				nOPos = nNextBtn;
				nSeconds = nLastOTime;
			}
			else if( c == 'B' )
			{
				nLastBTime += abs(nNextBtn - nBPos) + 1; 
				if( nLastOTime >= nLastBTime )
					nLastBTime = nLastOTime + 1;
				nBPos = nNextBtn;
				nSeconds = nLastBTime;
			}
		}
		out << "Case #" << iCount << ": " << nSeconds << endl;
	}
	return 0;
}

