// Round1A.cpp : Defines the entry point for the console application.
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
	//ifstream in("A-small-attempt1.in");
 //   ofstream out("A-small-attempt1.out");

	ifstream in("A-large.in");
    ofstream out("A-large.out");

    int iTasks;
	in >> iTasks;
	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		__int64 N, Pd, Pg;
		in >> N >> Pd >> Pg;
		string sResult = "Broken";

		if( Pg > 0 && Pg < 100 )
		{
			int i = 1;
			for( i = 1; i <= N && i <= 100; i++ )
			{
				if( (i * Pd) % 100  == 0 )
				{
					sResult = "Possible";
					break;
				}
			}

		}
		else if( Pg == Pd )
		{
			sResult = "Possible";
		}
		out << "Case #" << iCount << ": " << sResult << endl;
	}
	return 0;
}

