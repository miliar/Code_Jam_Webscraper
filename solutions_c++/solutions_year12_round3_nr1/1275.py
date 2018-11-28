// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;
vector<vector<int> > vNumbers;
vector<int> vVist;

bool DFS(int Vert)
{
	vVist[Vert] = 1;
	for( int i = 0; i < vVist.size(); i++ )
	{
		if( vNumbers[Vert][i] == 0 )
			continue;
		if( vVist[i] == 0 )
		{
			if( DFS(i) )
			{
				return true;
			}
		}
		else
			return true;
	}
	return false;
}

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
		vNumbers.clear();
		vVist.clear();
		int N = 0;
		in >> N;
		vNumbers.resize(N);
		vVist.resize(N);
		vVist.assign(N, 0);
		for( int i = 0; i < N; i++ )
		{
			int M = 0;
			in >> M;
			vNumbers[i].resize(N);
			vNumbers[i].assign(N, 0);
			for( int j = 0; j < M; j++ )
			{
				int K = 0;
				in >> K;
				if( K > 0 )
					vNumbers[i][K-1] = 1;
			}
		}
		
		bool bFound = false;
		for( int i = 0 ; i < N; i++ )
		{
			vVist.assign(N, 0);
			bFound = DFS(i);
			if( bFound )
			{
				break;
			}
		}
		out << "Case #" << iCount << ": ";
		if( bFound )
			out << "Yes" << endl;
		else
			out << "No" << endl;
	}

	return 0;
}

