#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>

#include <set>
#include <map>
#include <vector>
#include <string>

#include <algorithm>

using namespace std;

char res[200][200];
int a[200][200];
int sx[4]={-1, 0, 0, 1};
int sy[4]={ 0,-1, 1, 0};
int n,m;
char p[1000];


bool goodPoint(int x, int y)
{
	return x>=0 && x<n && y>=0 && y<m;
}


bool fToS(int x1, int y1, int x2, int y2)
{
	int mi = -1;
	int x,y;
	for(int t=0; t<4; t++)
	{		
		int newX = x1+sx[t];
		int newY = y1+sy[t];
		if(goodPoint(newX,newY) && a[newX][newY]<a[x1][y1])
		{
			if(mi==-1)
			{
				mi = a[newX][newY];
			}
			else
			{
				mi = min(a[newX][newY],mi);
			}
		}
	}
	if(mi==-1)
	{
		return false;
	}
	for(int t=0; t<4; t++)
	{		
		int newX = x1+sx[t];
		int newY = y1+sy[t];
		if(goodPoint(newX,newY) && a[newX][newY]<a[x1][y1])
		{
			if(a[newX][newY]==mi)
			{
				x=newX;
				y=newY;
				break;
			}
		}
	}
	return x==x2 && y==y2;

}

void dfs(int x, int y, int c)
{
	res[x][y]=c;
	for(int t=0; t<4; t++)
	{
		int newX = x+sx[t];
		int newY = y+sy[t];
		if(goodPoint(newX,newY))
		{
			if(fToS(newX,newY,x,y))
			{
				dfs(newX,newY,c);
			}
		}
	}

}

void run()
{
	memset(res,0,sizeof(res));
	scanf("%d%d",&n,&m);
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	for(char c='a'; c<='z'; c++)
	{
		p[c]=0;
	}
	char c='a';
	
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
		{
			if(res[i][j]==0)
			{
				bool good = true;
				for(int t=0; t<4; t++)
				{
					int newX = i+sx[t];
					int newY = j+sy[t];
					if(goodPoint(newX,newY))
					{
						if(fToS(i,j,newX,newY))
						{
							good = false;
							break;
						}
					}
				}
				if(good)
				{
					dfs(i,j,c);
					c++;
				}
			}
		}
	}
	c ='a';
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
		{
			if(p[res[i][j]]==0)
			{
				p[res[i][j]]=c++;
			}
		}
	}
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
		{
			printf("%c ",p[res[i][j]]);
		}
		printf("\n");
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int testCount;
	scanf("%d\n",&testCount);
	for(int testNumber=1; testNumber<=testCount; testNumber++)
	{
		printf("Case #%d:\n",testNumber);
		run();
		printf("\n");
	}
	return 0;
}