// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <stack>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;
#define pb(x) push_back(x)

//string split given string a and delimiters

int main()
{
	int T;
	cin >> T;
	int grid[102][102];
	for(int tcase = 1; tcase <= T; tcase++)
	{
		set<pair<int,int> > bact;
		int R = 0;
		cin >> R;
		memset(grid,0,sizeof(grid));
		for(int i = 0; i < R; i++)
		{
			int xa,xb,ya,yb;
			cin >> xa >> ya >> xb >> yb;
			for(int xc = xa; xc <= xb; xc++)
				for(int yc = ya; yc <= yb; yc++)
				{
					/*
					if(bact.count(make_pair(yc,xc)) == 0)
						bact.insert(make_pair(yc,xc));
					*/
					grid[yc][xc] = 1;
				}
		}
		int ret = 0;
		int grid2[102][102];
		while(true)
		{
			int ok = 0;
			memset(grid2,0,sizeof(grid2));
			for(int cy = 1; cy <= 100; cy++)
			{
				for(int cx = 1; cx <= 100; cx++)
				{
					if(grid[cy][cx])
					{
					 	ok++;
						if(grid[cy+1][cx-1])
						{
							grid2[cy+1][cx] = 1;
						}
						if(grid[cy-1][cx] || grid[cy][cx-1]) grid2[cy][cx] = 1;
					}
				}
			}
			if(!ok) break;
			ret++;
			memcpy(grid,grid2,sizeof(grid2));
		}
			
		
		
		printf("Case #%d: %d\n",tcase,ret);
	}
	return 0;
}
