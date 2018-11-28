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
		fi >> N;
		vector<char> robot(N);
		vector<int> button(N);
		for (int j=0;j<N;j++)
		{
			fi >> robot[j] >> button[j];
		}
		int pos[2];
		int target[2];
		pos[0] = pos[1] = 1;
		target[0] = target[1] = 1;

		int steps = 0;
		int idx = 0;
		int tidx[2];
		tidx[0] = -1;
		tidx[1] = -1;
		for (int j=0;j<N;j++)
			if (robot[j]=='O')
			{
				tidx[0] = j; 
				target[0] = button[j];
				break;
			}
		for (int j=0;j<N;j++)
			if (robot[j]=='B')
			{
				tidx[1] = j; 
				target[1] = button[j];
				break;
			}
		
		for (;;)
		{
			//cout << pos[0] << " " << pos[1] << " " << idx << endl;
			bool bMove = false;
			for (int r=0;r<2;r++)
			{
				if (pos[r]<target[r]) pos[r]++;
				else if (pos[r]>target[r]) pos[r]--;
				else
				{
					if (tidx[r]!=-1 && tidx[r]==idx)
					{
						bMove = true;
						tidx[r] = -1;
						for (int j=idx+1;j<N;j++)
							if (robot[j]==RB[r])
							{
								tidx[r] = j; 
								target[r] = button[j];
								break;
							}
					}
				}
			}
			if (bMove) idx++;
			steps++;
			if (tidx[0]==-1 && tidx[1]==-1) break;
			if (idx>=N) break;
		}
		fo << "Case #" << (i+1) << ": " << steps << endl;
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

