// C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define ull unsigned long long

void solve()
{
	int T;
	cin >> T;
	for (int t=0;t<T;t++)
	{
		map<ull, char> dt[2];
		int R;
		cin >> R;
		for (int r=0;r<R;r++)
		{
			int x1,y1,x2,y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int x=x1;x<=x2;x++)
				for (int y=y1;y<=y2;y++)
				{
					ull vx = x;
					ull vy = y;
					vy = vy << 32;
					vx += vy;
					dt[0][vx] = 1;
				}
		}
		int tm = 0;
		int idx = 0;
		while (dt[idx].size())
		{
			int nidx = 1-idx;
			dt[nidx].clear();
			for (map<ull, char>::iterator itr=dt[idx].begin();itr!=dt[idx].end();++itr)
			{
				ull cur = itr->first;
				ull cy = cur >> 32;
				ull cx = (unsigned int)cur;
				ull cxn = cx;
				ull cyn = cy - (ull)1;
				ull cxw = cx - (ull)1;
				ull cyw = cy;
				cyn = cyn << 32;
				cyw = cyw << 32;
				cxn += cyn;
				cxw += cyw;
				if (dt[idx].count(cxn)==0 && dt[idx].count(cxw)==0)
				{
					// die
				}
				else
				{
					dt[nidx][cur] = 1;
				}
				ull cxe = cx + (ull)1;
				ull cye = cy;
				ull cxne = cx + (ull)1;
				ull cyne = cy - (ull)1;
				cye = cye << 32;
				cyne = cyne << 32;
				cxe += cye;
				cxne += cyne;
				if (dt[idx].count(cxe)==0 && dt[idx].count(cxne)!=0)
				{
					dt[nidx][cxe] = 1;
				}
			}
			idx = nidx;
			tm++;
		}

		cout << "Case #" << (t+1) << ": " << tm << endl;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	solve();
	return 0;
}

