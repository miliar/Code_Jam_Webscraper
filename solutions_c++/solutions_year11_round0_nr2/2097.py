// ProblemB.cpp : Defines the entry point for the console application.
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
	//ifstream in("B-small-attempt4.in");
 //   ofstream out("B-small-attempt4.out");

	ifstream in("B-large.in");
    ofstream out("B-large.out");

    int iTasks;
	in >> iTasks;
	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		map<string, char> mpComb;
		map<char, string> mpOppos;
		string sRes;
		int nComb, nOppos, nSpellLen;
		in >> nComb;
		for( int i = 0; i < nComb; i++ )
		{
			string s;
			in >> s;
			string sComb = s.substr(0, s.length() - 1) ;
			mpComb[sComb] = s[s.length()-1];

			reverse(sComb.begin(), sComb.end());
			mpComb[sComb] = s[s.length()-1];
		}
		in >> nOppos;
		for( int i = 0; i < nOppos; i++ )
		{
			string s;
			in >> s;
			mpOppos[s[0]] += s[1];
			mpOppos[s[1]] += s[0];
		}
		in >> nSpellLen;
		string sSpell;
		in >> sSpell;

		for( size_t i = 0; i < sSpell.length(); i++ )
		{
			if( !sRes.empty() )
			{
				string sTestComb;
				sTestComb += sRes[sRes.length()-1];
				sTestComb += sSpell[i];
				map<string, char>::iterator iter = mpComb.find(sTestComb);
				if( iter != mpComb.end() )
				{
					sRes[sRes.length()-1] = iter->second;
				}				
				else
				{
					map<char, string>::iterator iterOp = mpOppos.find(sSpell[i]);
					bool bBreak = false;
					if( iterOp != mpOppos.end() )
					{
						for( size_t j = 0; j < iterOp->second.length() && !bBreak; j++ )
						{
							if( sRes.find(iterOp->second[j]) != string::npos )
							{
								sRes.clear();
								bBreak = true;
								break;
							}
						}
					}
					if( !bBreak )
						sRes += sSpell[i];
				}
			}
			else
				sRes += sSpell[i];
		}

		out << "Case #" << iCount << ": " << "[";
		if( !sRes.empty() )
		{
			size_t i = 0;
			for( i = 0; i < sRes.length() - 1; i++ )
			{
				out << sRes[i] << ", ";
			}
			out << sRes[i];
		}
		out << "]" << endl;
	}
	return 0;
}
