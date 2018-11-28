#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	cin >> nt;
	for (int t = 1; t <= nt; t++)
	{
		int n;
		cin >> n;
		vector<int> pos[2];
		vector<int> color;
		for (int i = 0; i < n; i++)
		{
			char c;
			int p;
			cin >> c>> p;
			if (c == 'O')
			{
				pos[0].push_back(p);
				color.push_back(0);
			}
			else
			{
				pos[1].push_back(p);
				color.push_back(1);
			}			
		}		
		int curpos[2] = {1, 1};		
		int ind[2] = {0, 0};
		bool pushed[2] = {false, false};	
		int ans = 0;		
		for (int i = 0; i < n; i++)
		{	
			int x = color[i];			
			int y = x^1;
			int d = abs(curpos[x] - pos[x][ind[x]]) + 1;
			curpos[x] = pos[x][ind[x]++];
			ans += d;
			if (ind[y] == pos[y].size())
			{
				continue;
			}
			if (curpos[y] < pos[y][ind[y]])
			{				
				if (d > pos[y][ind[y]] - curpos[y])
				{
					curpos[y] = pos[y][ind[y]];
					pushed[y] = true;
				}				
				else
				{
					curpos[y] += d;
				}
			}
			else
			{
				if (d > curpos[y] - pos[y][ind[y]])
				{
					curpos[y] = pos[y][ind[y]];
					pushed[y] = true;
				}
				else
				{
					curpos[y] -= d;
				}				
			}							
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}