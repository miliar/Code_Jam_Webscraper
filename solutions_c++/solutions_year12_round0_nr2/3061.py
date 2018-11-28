// QualificationB.cpp : Defines the entry point for the console application.
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
//	ifstream in("B-small-attempt2.in");
//    ofstream out("B-small-attempt2.out");

	ifstream in("B-large.in");
    ofstream out("B-large.out");

    int iTasks;
	in >> iTasks;
	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		int nGooglers, nSurpising, nBestP;
		in >> nGooglers >> nSurpising >> nBestP;
		int nPassed = 0;
		for( int i = 0; i < nGooglers; i++ )
		{
			int nPoints;
			in >> nPoints;
			if( nPoints == 0 )
			{
				if( nBestP == 0 )
					nPassed++;
				continue;
			}
			int res = nPoints / 3;
			int rem = nPoints % 3;
			if( rem > 0 )
				res++;
			if( res >= nBestP )
			{
				nPassed++;
			}
			else
			{
				if( (rem & 1) == 0 && nSurpising > 0 )
				{
					if( res + 1 >= nBestP )
					{
						nSurpising--;
						nPassed++;
					}
				}
			}
		}
		out << "Case #" << iCount << ": " << nPassed << endl;
	}
	return 0;
}
