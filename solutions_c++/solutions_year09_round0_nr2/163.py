
#include <iostream>

using namespace std;

int h,w;
int board[110][110];
int dir[][2]={-1,0,0,-1,0,1,1,0};
int usd[20000];
int ff[110][110];
int fun(int x,int y)
{
	int d=-1,xx,yy;
	int i;
	if(ff[x][y]!=-1) return ff[x][y];
	for(i=0;i<4;i++)
	{
		int x0=x+dir[i][0];
		int y0=y+dir[i][1];
		if(x0>=0&&x0<h&&y0>=0&&y0<w&&board[x0][y0]<board[x][y])
		{
			if(d==-1||board[x0][y0]<board[xx][yy])
			{
				xx=x0;yy=y0;
				d=i;
			}
		}
	}
	if(d==-1) return x*w+y;
	return ff[x][y]=fun(xx,yy);
}

int main()
{
	int t;
	scanf("%d",&t);
	int cse;
	for(cse=1;cse<=t;cse++)
	{
		scanf("%d%d",&h,&w);
		int i,j;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				scanf("%d",&board[i][j]);
			}
		}
		memset(ff,0xff,sizeof(ff));
		memset(usd,0xff,sizeof(usd));
		printf("Case #%d:\n",cse);
		int cnt=0;
		for(i=0;i<h;i++)
		{
			bool first=true;
			for(j=0;j<w;j++)
			{
				if(!first) putchar(' ');
				first=false;
				int r=fun(i,j);
				if(usd[r]!=-1)
				{
					putchar(usd[r]+'a');
				}
				else
				{
					usd[r]=cnt++;
					putchar(usd[r]+'a');
				}
			}
			printf("\n");
		}
	}
	return 0;
}
