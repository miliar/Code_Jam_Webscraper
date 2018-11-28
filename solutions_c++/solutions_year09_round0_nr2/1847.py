#include "stdafx.h"
#include <set>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

const int NMAX=110;
int T,H,W;
int a[NMAX][NMAX],ans[NMAX][NMAX];
int K;

const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};

bool have(int x,int y)
{
	if ( (x<0) || (y<0) || (x>=H) || (y>=W) )
		return 0;
	return 1;
}

bool tink(int i,int j)
{
	for(int k=0;k<4;k++)
		if ( (have(i+dx[k],j+dy[k])) && (a[i][j]>a[i+dx[k]][j+dy[k]]))
			return 0;
	return 1;
}



int will(int x,int y)
{
	if (!have(x,y))
		return -1;
	int res=-1;
	int minh=1000000000;
	for(int k=0;k<4;k++)
		if ( have(x+dx[k],y+dy[k]) && (a[x][y]>a[x+dx[k]][y+dy[k]]) && (a[x+dx[k]][y+dy[k]]<minh) )
		{
			minh=a[x+dx[k]][y+dy[k]];
			res=k;
		}
	return res;
}

void dfs(int x,int y)
{
	ans[x][y]=K;
	for(int k=0;k<4;k++)
	{
		int r=will(x+dx[k],y+dy[k]);
		if (r==-1)
			continue;
		if ( (dx[r]+dx[k]==0) && (dy[k]+dy[r]==0) )
			dfs(x+dx[k],y+dy[k]);
	}
}

int main()
{

	freopen("A-small.in","rt",stdin);
	freopen("A-small.out","wt",stdout);

	scanf("%d\n",&T);
	for(int i=0;i<T;i++)
	{
		scanf("%d%d\n",&H,&W);
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
				scanf("%d",&a[i][j]);
			scanf("\n");
		}
		K=0;
		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)
				if (tink(i,j))
				{
					K++;
					dfs(i,j);
				}
		vector<char> xz(K+1,'X');
		char now='a';
		printf("Case #%d:\n",i+1);
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
				if (xz[ans[i][j]]!='X')
					printf("%c ",xz[ans[i][j]]);
				else
				{
					printf("%c ",now);
					xz[ans[i][j]]=now;
					now++;
				}
			printf("\n");
		}
	}
	
	
	return 0;
}