// VS2008.cpp : 定义控制台应用程序的入口点。
//

//written on Sep 3,2009
#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <float.h>
#include <math.h>
#include <time.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <cassert>
#include <queue>
#include <bitset>
#include <iomanip>
#include <iostream>
#include <algorithm>

using namespace std;

const int M = 110;

int offset[4][2] = {-1,0,0,-1,0,1,1,0};

int c[M][M],d[M][M];
char out[M][M];
int h,w;

void dfs(int x,int y)
{
	int MinZ = INT_MAX;
	int dx,dy;
	for(int i=0;i<4;i++)
	{
		int cx,cy;
		cx = x+offset[i][0];
		cy = y+offset[i][1];
		if(cx >= 0 && cx < h && cy >= 0 && cy < w)
		{
			if(c[cx][cy] < c[x][y] && MinZ > c[cx][cy])
			{
				MinZ = c[cx][cy];
				dx = cx;
				dy = cy;
			}
		}
	}
	if(MinZ != INT_MAX)
	{
		d[x][y] = dx*w+dy;
	}
	else
		d[x][y] = -1;
}

char findson(int x,int y,char & c)
{
	if(d[x][y] == -1)
	{
		if(out[x][y] == '.')
			out[x][y] = c++;
		return out[x][y];
	}

	out[x][y] = findson(d[x][y]/w,d[x][y]%w,c);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    int i,j,k,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d %d",&h,&w);
		for(j=0;j<h;j++)
			for(k=0;k<w;k++)
				scanf("%d",&c[j][k]);

		for(j=0;j<h;j++)
			for(k=0;k<w;k++)
			{
				dfs(j,k);
				out[j][k] = '.';												//undo
			}

		char c = 'a';
		for(j=0;j<h;j++)
			for(k=0;k<w;k++)
				if(out[j][k] == '.')
					findson(j,k,c);		

		printf("Case #%d:\n",i);
		for(j=0;j<h;j++)
		{
			printf("%c",out[j][0]);
			for(k=1;k<w;k++)
				printf(" %c",out[j][k]);
			printf("\n");
		}
	}

	return 0;
}



