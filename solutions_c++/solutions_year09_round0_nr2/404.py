#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

int h,w;
int mat[110][110];
int out[110][110];
int xshift[]={0,-1,1,0};
int yshift[]={-1,0,0,1};

int num[30];
void dfs(int i,int j)
{
	if(out[i][j])
		return;
	int x,y;
	int hh=mat[i][j];
	int ty,tx;
	for(int t=0;t<4;t++)
	{
		y=i+yshift[t];
		x=j+xshift[t];
		if(y>=0&&y<h&&x>=0&&x<w)
		{
			if(mat[y][x]<hh)
			{
				hh=mat[y][x];
				ty=y;
				tx=x;
			}
		}
	}
	dfs(ty,tx);
	out[i][j]=out[ty][tx];
}
int main(void)
{
	freopen("B-large.in","r",stdin);
	freopen("BSL.out","w",stdout);
	int tn;
	int nn=0;
	scanf("%d",&tn);
	while(tn--)
	{
	scanf("%d%d",&h,&w);
	
	for(int i=0;i<h;i++)
		for(int j=0;j<w;j++)
			scanf("%d",&mat[i][j]);
	int k=0;
	memset(out,0,sizeof(out));
	int x,y;
	for(int i=0;i<h;i++)
		for(int j=0;j<w;j++)
		{
			bool flag=false;
			for(int t=0;t<4;t++)
			{
				y=i+yshift[t];
				x=j+xshift[t];
				if(y>=0&&y<h&&x>=0&&x<w)
				{
					if(mat[y][x]<mat[i][j])
						flag=true;
				}
			}
			if(!flag)
				out[i][j]=++k;
		}
/*	for(int i=0;i<h;i++)
	{
		for(int j=0;j<w;j++)
		{
		   if(j)
		   	printf(" ");
			 printf("%d",out[i][j]);
		}
		printf("\n");
	}*/
	for(int i=0;i<h;i++)
		for(int j=0;j<w;j++)
				dfs(i,j);
	memset(num,0,sizeof(num));
	int st=0;
	for(int i=0;i<h;i++)
		for(int j=0;j<w;j++)
			if(!num[out[i][j]])
				num[out[i][j]]=++st;
	printf("Case #%d:\n",++nn);

	for(int i=0;i<h;i++)
	{
		for(int j=0;j<w;j++)		
		{
			if(j)
				printf(" ");
			printf("%c",'a'+num[out[i][j]]-1);
		}
		printf("\n");
	}
	}
	return 0;
}
