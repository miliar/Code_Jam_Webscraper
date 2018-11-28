// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve(string sFileIn, string sFileOut)
{
	int N, T;
	ifstream fi(sFileIn.c_str());
	ofstream fo(sFileOut.c_str());
	fi >> T;
	for (int i=0;i<T;i++)
	{
		fi >> N;
		vector<int> dt(N);
		for (int j=0;j<N;j++)
			fi >> dt[j];

		vector<int> dtsort = dt;
		sort(dtsort.begin(), dtsort.end());
		int tel = 0;
		for (int j=0;j<N;j++)
			if (dt[j]!=dtsort[j])
				tel++;

		fo << "Case #" << (i+1) << ": " << tel << ".000000" << endl;
	}
	fi.close();
	fo.close();


}

int _tmain(int argc, _TCHAR* argv[])
{
	//solve("test.in", "test.out");
	//solve("D0.in", "D0.out");
	solve("D1.in", "D1.out");

	return 0;
}

