// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

void solve(string sFileIn, string sFileOut)
{
	string RB = "OB";
	int N, T;
	ifstream fi(sFileIn.c_str());
	ofstream fo(sFileOut.c_str());
	fi >> T;
	for (int i=0;i<T;i++)
	{
		int C, D;
		fi >> C;
		char tbl[256][256];
		char tblo[256][256];
		memset(tbl, 0, sizeof(tbl));
		memset(tblo, 0, sizeof(tblo));
		for (int j=0;j<C;j++)
		{
			char a,b,c;
			fi >> a >> b >> c;
			tbl[a][b] = c;
			tbl[b][a] = c;
		}
		fi >> D;
		for (int j=0;j<D;j++)
		{
			char a,b;
			fi >> a >> b;
			tblo[a][b] = 1;
			tblo[b][a] = 1;
		}
		fi >> N;
		vector<char> invoke(N);
		for (int j=0;j<N;j++)
		{
			fi >> invoke[j];
		}
		vector<char> res;
		for (int j=0;j<N;j++)
		{
			res.push_back(invoke[j]);
			if (res.size()>1)
			{
				char a = res[res.size()-1];
				char b = res[res.size()-2];
				if (tbl[a][b]!=0)
				{
					res.pop_back();
					res.pop_back();
					res.push_back(tbl[a][b]);
				}
			}
			for (int z=0;z<res.size()-1;z++)
				if (tblo[res[z]][res.back()])
				{
					res.resize(0);
					break;
				}
		}
		fo << "Case #" << (i+1) << ": [";
		for (int j=0;j<res.size();j++)
		{
			fo << res[j];
			if (j!=res.size()-1)
				fo << ", ";
		}
		fo << "]" << endl;
	}
	fi.close();
	fo.close();


}

int _tmain(int argc, _TCHAR* argv[])
{
	//solve("test.in", "test.out");
	//solve("B0.in", "B0.out");
	solve("B1.in", "B1.out");

	return 0;
}

