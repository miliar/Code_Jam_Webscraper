// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <math.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("A-large.in");//A-small-attempt1.in");//
    ofstream out("A-large.out");//A-small-attempt1.out");//
    int  iTasks;
	in >> iTasks;
    for( int  iCount = 1; iCount <= iTasks; iCount++ )
    {
		string str;
		in >> str;
		vector<__int64> vNumber(str.length());
		map<char, __int64> mpDigits;
		int iCur = 1;
		for( int i = 0 ; i < (int)str.length(); i++ )
		{
			typedef map<char, __int64>::iterator mapiter;
			pair< mapiter, bool > pair = mpDigits.insert(make_pair<char, __int64>(str[i], iCur));
			vNumber[i] = mpDigits[str[i]];
			if( pair.second )
			{
				if( iCur == 1 )
					iCur = 0;
				else if( iCur == 0 )
					iCur = 2;
				else
					iCur++;
			}
		}
		int iPower = 0;
		__int64 iBase = mpDigits.size();
		if( iBase == 1 )
			iBase = 2;
		__int64 iRes = 0;
		for( int i = (int)vNumber.size() - 1; i >= 0; i-- )
		{
			__int64 iTmp = vNumber[i] * _Pow_int(iBase, (int)vNumber.size() - 1 - i);
			iRes += iTmp;
		}
		out<<"Case #"<< iCount <<": " << iRes << "\n";
	}
	return 0;
}

