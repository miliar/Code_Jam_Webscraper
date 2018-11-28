// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

static const int dx[] = {0, 1, 0, 1};
static const int dy[] = {0, 0, 1, 1};
static const char ch[] = {'/', '\\', '\\', '/'};
void solve(string sFileIn, string sFileOut)
{
	char buf[1024];
	int T, R, C;
	ifstream fi(sFileIn.c_str());
	ofstream fo(sFileOut.c_str());
	fi >> T;
	for (int i=0;i<T;i++)
	{
		vector<string> dt;
		fi >> R >> C;
		fi.getline(buf, 1024);
		for (int j=0;j<R;j++)
		{
			fi.getline(buf, 1024);
			dt.push_back(buf);
		}
		bool bfit = true;
		for (int y=0;y<R;y++)
		{
			for (int x=0;x<C;x++)
				if (bfit && dt[y][x]=='#')
				{
					int cnt = 0;
					for (int d=0;d<4;d++)
					{
						int ox = x+dx[d];
						int oy = y+dy[d];
						if (ox>=0 && ox<C && oy>=0 && oy<R && dt[oy][ox]=='#')
						{
							cnt++;
						}
					}
					if (cnt==4)
					{
						for (int d=0;d<4;d++)
						{
							int ox = x+dx[d];
							int oy = y+dy[d];
							dt[oy][ox] = ch[d];
						}
					} else
					{
						bfit = false;
						break;
					}
				}
		}
		fo << "Case #" << (i+1) << ":"  << endl;
		if (!bfit)
			fo << "Impossible" << endl;
		else
		for (int j=0;j<R;j++)
		{
			fo << dt[j] << endl;
		}
	}
	fi.close();
	fo.close();
}

int _tmain(int argc, _TCHAR* argv[])
{
	//solve("test.in", "test.out");
	//solve("A0.in", "A0.out");
	solve("A1.in", "A1.out");

	return 0;
}

