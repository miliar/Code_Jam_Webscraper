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
	int N, L, H, T;
	ifstream fi(sFileIn.c_str());
	ofstream fo(sFileOut.c_str());
	fi >> T;
	for (int i=0;i<T;i++)
	{
		fi >> N >> L >> H;
		vector<int> freq(N);
		for (int j=0;j<N;j++)
		{
			fi >> freq[j];
		}
		int bf = -1;
		for (int f=L;f<=H;f++)
		{
			bool ok = true;
			for (int j=0;j<N;j++)
			{
				if ( (freq[j]%f)==0 || (f%freq[j])==0 )
				{

				}
				else
				{
					ok = false;
					break;
				}
			}
			if (ok) 
			{
				bf = f;
				break;
			}
		}


		fo << "Case #" << (i+1) << ": ";
		if (bf<0) fo << "NO" << endl;
		else fo << bf << endl;
	}
	fi.close();
	fo.close();


}

int _tmain(int argc, _TCHAR* argv[])
{
	//solve("test.in", "test.out");
	solve("C0.in", "C0.out");
	//solve("C1.in", "C1.out");

	return 0;
}

