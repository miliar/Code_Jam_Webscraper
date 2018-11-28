// ProblemB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
#include <functional>

using namespace std;
bool Not0(int i )
{
	return i != 0;
}
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("B-large.in");//B-small-attempt6.in");//
    ofstream out("B-large.out");//B-small-attempt6.out");//
    int  iTasks;
	in >> iTasks;

    for( int  iCount = 1; iCount <= iTasks; iCount++ )
    {
		vector<int> vNumber;
		string str;
		in >> str;
//		str = "908151";
		for( size_t i = 0; i < str.size(); i++ )
		{
			string stmp;
			stmp += str[i];
			vNumber.push_back(atoi(stmp.c_str()));
		}
		bool bChanged = false;
		for( int i = (int)vNumber.size()-2; i >= 0; i-- )
		{
			for( int j = (int)vNumber.size()-1; j > i; j-- )
			{
				if( vNumber[j] > vNumber[i] )
				{
					swap(vNumber[j], vNumber[i]);

					sort(vNumber.begin() + i + 1, vNumber.end());
					bChanged = true;
					break;
				}
			}
			if( bChanged )
				break;
		}
		if( !bChanged )
		{
			vNumber.push_back(0);
			sort(vNumber.begin(), vNumber.end());
			vector<int>::iterator iter = find_if(vNumber.begin(), vNumber.end(), Not0);
			rotate(vNumber.begin(), iter, iter+1);
		}
		out << "Case #" << iCount << ": ";
		for(size_t i = 0; i < vNumber.size(); i++ )
			out << vNumber[i];
		out << "\n";
	}
	return 0;
}