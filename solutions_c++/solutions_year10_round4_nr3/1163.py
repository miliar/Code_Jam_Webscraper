#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <sstream>
#define MAX 103
using namespace std;
#define min(a,b) (((a) < (b)) ? (a) : (b))
char map[MAX][MAX];
bool check(int y,int x)
{
	int i,j;
	for (i=1; i<=x; ++i)
	{
		for (j=1; j<=y; ++j)
		{
			if (map[j][i] == 1) return false;
		}
	}
	return true;
}

void dead(int y,int x)
{
	int i,j;
	for (j=y;j>0; --j)
	{
		for (i=x;i>0; --i)
		{
			if (map[j][i] == 0)
			{
				if (map[j][i-1] == 1 && map[j-1][i] == 1)
				{
					map[j][i] = 1;
					continue;
				}
			}
			if (map[j][i] == 1)
			{
				if (map[j][i-1] == 1 || map[j-1][i] == 1)
				{
					map[j][i] = 1;
					continue;
				}
			}

			map[j][i] = 0;
		}
	}
}
void print(int y,int x)
{
	int i,j;
	for (i=1; i<=y; ++i)
	{
		for (j=1; j<=x; ++j)
		{
			printf("%d ",map[i][j]);
		}
		printf("\n");
	}
	printf("----------\n");
}
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("large.txt", "w", stdout);
	int nt, it,k;
	int i,j;
	int x1,x2,y1,y2,x,y,sum,max_x,max_y;
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		sum = 0;
		max_x = 0;
		max_y = 0;
		memset(map,0,sizeof(map));
		scanf("%d",&k);
		for (i=0; i<k; ++i)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if (x2 > max_x) max_x = x2;
			if (y2 > max_y) max_y = y2;
 			for (x=x1; x<=x2; ++x)
			{
				for (y=y1; y<=y2; ++y)
				{
					map[y][x] = 1;
				}
			}
		}
		
		while (!check(max_y,max_x))
		{
			sum++;
			dead(max_y,max_x);
		//	print(max_y,max_x);
		}

		printf("Case #%d: %d\n",it,sum);
	
	}
	return 0;
}