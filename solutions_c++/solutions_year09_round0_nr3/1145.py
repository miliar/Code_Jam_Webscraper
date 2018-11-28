// ProblemC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;
string sPattern = "welcome to code jam";//"abc";//"abc";//
int iSum = 0;


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("C-large.in");//C-small-attempt0.in");//
    ofstream out("C-large.out");//C-small-attempt0.out");//
    int  iTasks;
	in >> iTasks;
	string stmp;
	getline(in, stmp);
	
    for( int  iCount = 1; iCount <= iTasks; iCount++ )
    {
		string sInput;
		getline(in, sInput);
		iSum = 0;

		//sInput = "abacbcc";
		//sInput = "aabb";
		
		vector<vector<pair<int,int>>> vvFreq;
		vvFreq.push_back(vector<pair<int, int>>());
		vvFreq[0].push_back(pair<int, int>(-1, 0));
		for( size_t i = 0; i < sPattern.length(); i++ )
		{
			vvFreq.push_back(vector<pair<int, int>>());
			for( size_t j = 0; j < sInput.length(); j++ )
			{
				if( sInput[j] == sPattern[i] )
				{
					if( i == sPattern.length() - 1 )
						vvFreq[i + 1].push_back(pair<int, int>(j, 1));
					else
						vvFreq[i + 1].push_back(pair<int, int>(j, 0));
				}
			}
		}
	
		for( int i = vvFreq.size() - 2; i >= 0; i-- )
		{
			for(size_t j = 0; j < vvFreq[i].size(); j++ )
			{
				for( size_t k = 0; k < vvFreq[i + 1].size(); k++ )
					if( vvFreq[i][j].first < vvFreq[i + 1][k].first )
					{
						vvFreq[i][j].second += vvFreq[i + 1][k].second;
						if( vvFreq[i][j].second > 9999 )
							vvFreq[i][j].second -= 10000;
					}
			}
		}

		iSum = vvFreq[0][0].second;			
		out<<"Case #"<< iCount << ": ";
		if( iSum < 1000 )
			out << "0";
		if( iSum < 100 )
			out << "0";
		if( iSum < 10 )
			out << "0";
		out << iSum << '\n';
	}

	return 0;
}


