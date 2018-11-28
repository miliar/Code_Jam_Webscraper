#include <iostream>
#include <cstdio>

#include <cstring>
#include <string>

#include <vector>
#include <map>
#include <set>

#include <algorithm>
#include <cmath>

using namespace std;

vector<int> robot[2];
char color[5];
vector<int> colors;


int sgn(int x)
{
	if(x == 0)
	{
		return 0;
	}
	if(x < 0)
	{
		return -1;
	}
	return 1;
}


int getDir(int x1, int x2)
{
	return sgn(x2 - x1);
}


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCount;
	scanf("%d", &testCount);
	for(int testNumber = 1; testNumber <= testCount; testNumber++)
	{
		int n;
		scanf("%d", &n);
		robot[0].clear();
		robot[1].clear();
		colors.clear();
		for(int i = 0; i < n; i++)
		{
			int num;
			scanf("%s%d", color, &num);
			int bit = 1;
			if(color[0] == 'O')
			{
				bit = 0;
			}
			robot[bit].push_back(num);
			colors.push_back(bit);
		}
		int oL = robot[0].size();
		int bL = robot[1].size();
		int It[2];
		It[0] = It[1] = 0;
		int x[2];
		x[0] = x[1] = 1;
		robot[0].push_back(1e6);
		robot[1].push_back(1e6);
		int res = 0;
		int cur = 0;
		int L = colors.size();
		while(cur != L)
		{
			int first = colors[cur];
			for(int i = 0; i < 2; i++)
			{
				int dir = getDir(x[first], robot[first][ It[first] ]);
				if(dir == 0)
				{
					if(i == 0)
					{
						cur++;
						It[first]++;
					}
				}
				else
				{
					x[first] += dir;
				}
				first ^= 1;
			}
			res++;			
		}
		printf("Case #%d: %d\n", testNumber, res);
	}
	return 0;
}