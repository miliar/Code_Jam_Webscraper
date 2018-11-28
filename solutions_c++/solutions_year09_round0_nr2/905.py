// watersheds.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

static const int dx[] = {0,-1,1,0};
static const int dy[] = {-1,0,0,1};

int _tmain(int argc, _TCHAR* argv[])
{
	int T,W,H;
	int dt[128][128];
	int h[128][128];
	map<int, int> mm;
	cin >> T;
	for (int t=0;t<T;t++)
	{
		mm.clear();
		cin >> H >> W;
		memset(dt, 0, sizeof(dt));
		for (int y=0;y<H;y++)
			for (int x=0;x<W;x++)
				cin >> h[x][y];
		int idx = 0;
		int grp = 0;
		for (int y=0;y<H;y++)
			for (int x=0;x<W;x++)
				if (dt[x][y]==0)
				{
					idx++;
					mm[idx] = grp;
					int ox = x;
					int oy = y;

					for (;;)
					{
						dt[ox][oy] = idx;
						int myh = h[ox][oy];
						int bx,by;
						for (int j=0;j<4;j++)
						{
							int nx = ox + dx[j];
							int ny = oy + dy[j];
							if (nx>=0 && nx<W && ny>=0 && ny<H)
							{
								if (h[nx][ny]<myh)
								{
									bx = nx;
									by = ny;
									myh = h[nx][ny];
								}
							}
						}
						if (myh<h[ox][oy])
						{
							ox = bx;
							oy = by;
							if (dt[ox][oy]!=0)
							{
								mm[idx] = mm[ dt[ox][oy] ];
								break;
							}
						} else break;
					}
					if (mm[idx] == grp) grp++;
				}
				cout << "Case #" << (t+1) << ":" << endl;
		for (int y=0;y<H;y++)
		{
			for (int x=0;x<W;x++)
			{
				cout << (char)('a'+mm[dt[x][y]]); 
				if (x<W-1) cout << " ";
			}
			cout << endl;
		}

	}

	return 0;
}

