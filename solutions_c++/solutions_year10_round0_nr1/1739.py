// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("A-large.in");//A-small-attempt0.in");
    ofstream out("A-large.out");//A-small-attempt0.out");
    string str;
    int  nTasks;
	in >> nTasks;

    for( int  iCount = 1; iCount <= nTasks; iCount++ )
    {
		int N, K;
		in >> N >> K;
		string sMode = "OFF";
		int P  = _Pow_int(2, N);
		if( ((K + 1) % P) == 0 )
		{
			sMode = "ON";
		}

		out<<"Case #"<< iCount <<": " << sMode << '\n';
	}
	return 0;
}

