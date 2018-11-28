#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include<iostream>
using namespace std;
int T;
int R;
int allCell[110][110];
int nowCell[110][110];
void copyT()
{
	for(int i = 1;i <= 100;i++)
		for(int j = 1;j <= 100;j++)
			allCell[i][j] = nowCell[i][j];
}
void copyF()
{
	for(int i = 1;i <= 100;i++)
		for(int j = 1;j <= 100;j++)
			nowCell[i][j] = allCell[i][j];
}
bool solve()
{
	copyF();
	for(int i = 1;i <= 100;i++)
	{
		for(int j = 1;j <= 100;j++)
		{
			if(allCell[i][j] == 0)
			{
				if((j - 1) >= 1 && (i - 1) >= 1 && allCell[i - 1][j] == 1 && allCell[i][j - 1] == 1)
					nowCell[i][j] = 1;
			}
			if(allCell[i][j] == 1)
			{
				if(!(((i - 1) >= 1 && allCell[i - 1][j] == 1) || ((j - 1) >= 1 && allCell[i][j - 1] == 1)))
					nowCell[i][j] = 0;
			}
		}
	}
	copyT();
	for(int i = 1;i <= 100;i++)
		for(int j = 1;j <= 100;j++)
			if(allCell[i][j] == 1)
				return false;
	return true;
}
int main()
{
	freopen("..\\C-small-attempt0_round2.in","r",stdin);
	freopen("..\\C-small-attempt0_round2.out","w",stdout);
	scanf("%d",&T);
	for(int t = 1;t <= T;t++)
	{
		scanf("%d", &R);
		memset(allCell, 0, sizeof(allCell));
		int x1,x2,y1,y2;
		for(int i = 0;i < R;i++)
		{
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(int j = y1;j <= y2;j++)
				for(int k = x1;k <= x2;k++)
					allCell[j][k] = 1;
		}
		int res = 0;
		while(!solve())
		{
			res++;
		}
		printf("Case #%d: %d\n",t, res + 1);
	}
	return 0;
}