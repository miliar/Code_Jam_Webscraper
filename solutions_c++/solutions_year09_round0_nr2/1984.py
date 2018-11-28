#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int t,h,w;
int a[110][110];
int basin[110][110];
int basins,i,j,test;
char name[10010];
char letter;
int mnx=0,mny=0;

int dfs(int x, int y)
{
	if (basin[x][y]!=0) return basin[x][y];

	mnx=mny=0;
	if (y<h) if (a[x][y+1]<a[x+mnx][y+mny] || (a[x][y+1]==a[x+mnx][y+mny] && mnx+mny!=0)) {mnx=+0; mny=+1;}
	if (x<w) if (a[x+1][y]<a[x+mnx][y+mny] || (a[x+1][y]==a[x+mnx][y+mny] && mnx+mny!=0)) {mnx=+1; mny=+0;}
	if (x>1) if (a[x-1][y]<a[x+mnx][y+mny] || (a[x-1][y]==a[x+mnx][y+mny] && mnx+mny!=0)) {mnx=-1; mny=+0;}
	if (y>1) if (a[x][y-1]<a[x+mnx][y+mny] || (a[x][y-1]==a[x+mnx][y+mny] && mnx+mny!=0)) {mnx=+0; mny=-1;}
	
	if (mnx+mny!=0)
	{
		basin[x][y]=dfs(x+mnx,y+mny);
		return basin[x][y];
	} else
	{
		basin[x][y]=++basins;
		return basin[x][y];
	}
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

	scanf("%d",&t);
	for (test=1; test<=t; test++)
	{
		printf("Case #%d:\n",test);
		scanf("%d %d",&h,&w);
		for (j=1; j<=h; j++)
		for (i=1; i<=w; i++)
		{
			scanf("%d",&a[i][j]);
		}
		memset(basin, 0, sizeof(basin));
		basins=0;
		for (i=1; i<=w; i++)
		for (j=1; j<=h; j++)
		{
			if (basin[i][j]==0) dfs(i,j);
		}

		memset(name,0,sizeof(name));
		letter='a';
		for (j=1; j<=h; j++)
		for (i=1; i<=w; i++)
			if (name[basin[i][j]]==0)
			{
				name[basin[i][j]]=letter;
				letter++;
			}
		
		for (j=1; j<=h; j++)
		{
			for (i=1; i<w; i++)
				printf("%c ", name[basin[i][j]]);
				printf("%c\n",name[basin[w][j]]);
		}
	}

    return 0;
}
