#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

char b[110];
vector<int> bot[2];

int sign(int n)
{
	if(n < 0) return -1;
	if(n > 0) return 1;
	return 0;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int ca = 1; ca <= T; ca++)
	{
		int n, sol = 0;
		scanf("%d", &n);
		bot[0].clear(); bot[1].clear();
		for(int i = 0; i < n; i++)
		{
			int p;
			scanf(" %c %d", &b[i], &p);
			if(b[i] == 'O')
				bot[0].push_back(p);
			else bot[1].push_back(p);
		}
		bot[0].push_back(99); bot[1].push_back(99);
		int p1 = 1, p2 = 1;
		int pl1 = 0, pl2 = 0;
		for(int i = 0; i < n; i++)
		{
			if(b[i] == 'O')
			{
				int delta = abs(p1-bot[0][pl1])+1;
				sol += delta;
				p1 = bot[0][pl1];
				if(abs(bot[1][pl2] - p2) < delta)
					p2 = bot[1][pl2];
				else p2 -= delta*sign(p2-bot[1][pl2]);
				pl1++;
			}
			else 
			{
				int delta = abs(p2-bot[1][pl2])+1;
				sol += delta;
				p2 = bot[1][pl2];
				if(abs(bot[0][pl1] - p1) < delta)
					p1 = bot[0][pl1];
				else p1 -= delta*sign(p1-bot[0][pl1]);
				pl2++;
			}
		}
		printf("Case #%d: %d\n", ca, sol);
	}
	return 0;
}
