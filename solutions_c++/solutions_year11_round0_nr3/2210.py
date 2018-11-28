// ProblemC.cpp : Defines the entry point for the console application.
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
	//ifstream in("C-small-attempt2.in");
 //   ofstream out("C-small-attempt2.out");

	ifstream in("C-large.in");
    ofstream out("C-large.out");

    int iTasks;
	in >> iTasks;
	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		int N;
		in >> N;
		vector<int> vCandy(N);
		vector<int> v1, v2;
		for( int i = 0; i < N; i++ )
			in >> vCandy[i];
		sort(vCandy.begin(), vCandy.end());

		int nPile1 = 0;
		int nPile2 = 0;
		
		for( size_t i = 0; i < vCandy.size(); i++ )
		{
			nPile2 ^= vCandy[i];
			nPile1 += vCandy[i];
		}

		out << "Case #" << iCount << ": ";
		if( nPile2 != 0 )
			out << "NO";
		else
			out << nPile1 - vCandy[0];
		out << endl;
	}
	return 0;
}
