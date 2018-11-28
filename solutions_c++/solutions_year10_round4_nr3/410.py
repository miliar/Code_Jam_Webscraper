#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <vector>
using namespace std;

const int MAXN = 120;
bool mmap[MAXN][MAXN], newmap[MAXN][MAXN];

int mymax(int a, int b)
{
	return a > b ? a : b;
}

int mymin(int a, int b)
{
	return a < b ? a : b;
}

bool endchk()
{
	for(int i = 0; i < MAXN; i++)
		for(int j = 0; j < MAXN; j++)
			if(mmap[i][j])
				return false;
	return true;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T, R;
	cin>>T;

	for(int t = 0; t < T; t++)
	{
		memset(mmap, false, sizeof(mmap));
		cin>>R;

		for(int i = 0; i < R; i++)
		{
			int x1, x2, y1, y2, sx, ex, sy, ey;
			cin>>x1>>y1>>x2>>y2;
			sx = mymin(x1, x2), ex = mymax(x1, x2);
			sy = mymin(y1, y2), ey = mymax(y1, y2);
			
			for(int nx = sx; nx <= ex; nx++)
				for(int ny = sy; ny <= ey; ny++)
					mmap[nx][ny] = true;
		}

		int ans = 0;
		
		while(!endchk())
		{
			memset(newmap, false, sizeof(newmap));

			for(int i = 1; i < MAXN; i++)
				for(int j = 1; j < MAXN; j++)
				{
					if(mmap[i][j])
					{
						if(mmap[i-1][j] || mmap[i][j-1]) newmap[i][j] = true;
					}
					else
					{
						if(mmap[i-1][j] && mmap[i][j-1])
							newmap[i][j] = true;
					}
				}
			
			memcpy(mmap, newmap, sizeof(mmap));
			ans++;
		}
		
		printf("Case #%d: %d\n", t+1, ans);
	}

	return 0;
}
