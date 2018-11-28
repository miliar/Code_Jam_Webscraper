// ProbA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <string>
#include <iostream>

using namespace std;


void solve()
{
	char buf[1024];
	int T;
	cin >> T;
	cin.getline(buf, 1024);
	for (int t=0;t<T;t++)
	{
		vector<string> dt;
		vector<int> right;
		int N;
		cin >> N;
		cin.getline(buf, 1024);
		for (int i=0;i<N;i++)
		{
			cin.getline(buf, 1024);
			dt.push_back(buf);
			int v = -1;
			for (int j=N-1;j>=0;j--)
				if (buf[j]=='1')
				{
					v = j;
					break;
				}
			right.push_back(v);
		}
		int swaps = 0;
		int y = 0;
		for (;;)
		{
			if (y>=N) break;
			int ibig = -1;
			int big = -1;
			for (int i=y;i<N;i++)
			{
				if (right[i]<=y)
				{
					big = right[i];
					ibig = i;
					break;
				}
			}
			if (ibig==y)
			{
				y++;
				continue;
			}
			while (ibig!=y)
			{
				swap(right[ibig], right[ibig-1]);
				ibig--;
				swaps++;
			}
			y++;
		}
		cout << "Case #" << (t+1) << ": " << swaps << endl;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	solve();
	return 0;
}

