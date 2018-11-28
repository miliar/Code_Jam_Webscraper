// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <math.h>
#include <vector>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("A-large.in");//small-attempt2.in");
    ofstream out("A-large.out");//-small-attempt2.out");
    string str;
    int  nTasks;
	in >> nTasks;

    for( int  iCount = 1; iCount <= nTasks; iCount++ )
    {
		int N;
		in >> N;
		vector<int> A(N), B(N);
		for(int i = 0; i < N; i++)
		{
			in >> A[i] >> B[i];
		}
		int iRes = 0;
		for( int i = 0; i < N; i++ )
		{
			for( int j = i + 1; j < N; j++ )
			{
				if( (A[i] > A[j] && B[i] < B[j]) ||
					(A[i] < A[j] && B[i] > B[j]) )
					iRes++;
			}
		}
		out<<"Case #"<< iCount <<": " << iRes << '\n';
	}
	return 0;
}

