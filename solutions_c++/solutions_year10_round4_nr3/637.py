#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

int max(int a, int b)
{
	if(a > b)
		return a;
	return b;
}

int min(int a, int b)
{
	if(a < b)
		return a;
	return b;
}

int maze[105][105];
int temp[105][105];


int main()
{
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);

	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);

	int inp, kase, i, j, k, r;
	int a1, a2, b1, b2, cnt;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d", &r);
		memset(maze, 0, sizeof(maze));
		for(i = 0; i < r; i++)
		{
			scanf("%d %d %d %d", &a1, &b1, &a2, &b2);
			for(j = a1; j <= a2; j++)
			{
				for(k = b1; k <= b2; k++)
				{
					maze[j][k] = 1;
				}
			}
			cnt++;
		}
		int ret = 0;
		while(cnt)
		{
			cnt = 0;
			ret++;
			for(i = 1; i < 105; i++)
			{
				for(j = 1; j < 105; j++)
				{
					if(maze[i][j] == 1)
					{
						if(maze[i - 1][j] != 1 && maze[i][j - 1] != 1)
							temp[i][j] = 0;
						else
							temp[i][j] = 1;
					}
					else
					{
						if(maze[i - 1][j] == 1 && maze[i][j - 1] == 1)
							temp[i][j] = 1;
						else
							temp[i][j] = 0;
					}
				}
			}
			for(i = 0; i < 105; i++)
			{
				for(j = 0; j < 105; j++)
				{
					if(temp[i][j] == 1)
						cnt++;
					maze[i][j] = temp[i][j];
				}
			}
		}
		printf("Case #%d: %d\n", kase, ret);
	}
	
	return 0;

}
