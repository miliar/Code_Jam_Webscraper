// Watersheds.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
const int max_height=10005;
int map[105][105];
char label[105][105];
int T,H,W;
int translate[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
char letter,sink;
void DFS_Find(int x,int y)
{
	if(label[x][y]!=0)
	{
		sink=label[x][y];
		return;
	}
	int min_height=map[x][y];
	int next=4;
	int next_x,next_y;
	for(int i=0;i<4;i++)
	{
		next_x=x+translate[i][0];
		next_y=y+translate[i][1];
		if(map[next_x][next_y]<min_height) 
			min_height=map[x+translate[i][0]][y+translate[i][1]],next=i;
	}
	if(next==4)
	{
		label[x][y]=sink=letter++;
		return;
	}
	DFS_Find(x+translate[next][0],y+translate[next][1]);
	label[x][y]=sink;
}
int main()
{
	//freopen("d:\\1.txt","r",stdin);
	freopen("d:\\B-large.in","r",stdin);
	freopen("d:\\B-large.out","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d%d",&H,&W);
		for(int j=1;j<=H;j++)
		{
			for(int k=1;k<=W;k++)
			{
				scanf("%d",&map[j][k]);
			}
		}
		for(int j=1;j<=W;j++)
		{
			map[0][j]=map[H+1][j]=max_height;
		}
		for(int j=1;j<=H;j++)
		{
			map[j][0]=map[j][W+1]=max_height;
		}
		memset(label,0,sizeof(label));
		letter='a';
		for(int j=1;j<=H;j++)
		{
			for(int k=1;k<=W;k++)
			{
				if(label[j][k]==0) DFS_Find(j,k);
			}
		}
		printf("Case #%d:\n",i);
		for(int j=1;j<=H;j++)
		{
			for(int k=1;k<W;k++)
			{
				printf("%c ",label[j][k]);
			}
			printf("%c\n",label[j][W]);
		}
	}
	return 0;
}

