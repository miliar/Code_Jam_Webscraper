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
		vector<long long> values(N);
		for (int j=0;j<N;j++)
		{
			fi >> values[j];
		}
		sort(values.begin(), values.end());

		long long best = -1;
		for (int z=1;z<=N-1;z++)
		{
			long long left = 0;
			long long right = 0;
			long long sum = 0;
			long long cntl = 0;
			long long cntr = 0;
			for (int j=0;j<N;j++)
				if (j<z)
				{
					cntl++;
					left = left ^ values[j];
				}
				else
				{
					cntr++;
					sum += values[j];
					right = right ^ values[j];
				}
			if (left==right && cntl>=1 && cntr>=1)
			{
				best = max(sum, best);
			}
		}
		fo << "Case #" << (i+1) << ": ";
		if (best==-1) fo << "NO" << endl; else fo << best << endl;
	}
	fi.close();
	fo.close();


}

int _tmain(int argc, _TCHAR* argv[])
{
	//solve("test.in", "test.out");
	//solve("C0.in", "C0.out");
	solve("C1.in", "C1.out");

	return 0;
}

