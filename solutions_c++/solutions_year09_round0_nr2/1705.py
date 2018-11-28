#include <iostream>
using namespace std;
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int a[110][110];
char b[110][110];
int n,m;
char lastchar;

char findroot(int x,int y)
{
	int minn=a[x][y];
	int minx,miny;
	for(int i=0;i<4;i++)
	{
		int tx=x+dir[i][0];
		int ty=y+dir[i][1];
		if(tx<0 || ty<0 || tx>=n || ty>=m) continue;
		
		if(a[tx][ty]<minn)
		{
			minn=a[tx][ty];
			minx=tx;
			miny=ty;
		}
	}
	if(minn<a[x][y])
	{
		if(b[minx][miny])
		{
			b[x][y]=b[minx][miny];
			return b[minx][miny];
		}
		else
		{
			b[minx][miny]=findroot(minx,miny);
			b[x][y]=b[minx][miny];
			return b[minx][miny];
		}
	}
	else
	{
		if(!b[x][y])
		{
			b[x][y]=lastchar;
			lastchar ++;
		}
		return b[x][y];
	}
	
}


int main()
{
	
	int T;
	scanf("%d",&T);
	for(int Ti=1;Ti<=T;Ti++)
	{
		
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}				
		
		memset(b,0,sizeof(b));
		lastchar = 'a';
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				b[i][j]=findroot(i,j);
			}
		}
		printf("Case #%d:\n",Ti);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				printf("%c ",b[i][j]);
			}
			puts("");
		}				

	}
}
