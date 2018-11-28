#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define N 110
int map[N][N], visit[N][N];
int h, w;
typedef struct 
{
	int x, y;
}Q;
char ans[N][N], t;
int dx[]={-1,0,0,1}, dy[]={0,-1,1,0};
int ok(int x, int y)
{
	if(x>=1&&x<=h&&y>=1&&y<=w) return 1;
	return 0;
}
void floodfill(int a, int b)
{
	int k, nextx, nexty, cntx, cnty, rear, i, mini, minj, min, ansx, ansy;
	Q q[N*N];
	rear=0;
	q[rear].x=a;
	q[rear++].y=b;
	min=map[a][b];
	mini=a;
	minj=b;
	for(i=0;i<rear;i++)
	{
		cntx=q[i].x;
		cnty=q[i].y;
		ansx=cntx;
		ansy=cnty;
		for(k=0;k<4;k++)
		{
			nextx=cntx+dx[k];
			nexty=cnty+dy[k];
			if(ok(nextx,nexty) && map[nextx][nexty]<map[ansx][ansy])
			{
				ansx=nextx;
				ansy=nexty;
			}
		}
		if(!(ansx==cntx && ansy==cnty))
			{
				q[rear].x=ansx;
				q[rear++].y=ansy;
				if(map[ansx][ansy]<min)
				{
					min=map[ansx][ansy];
					mini=ansx;
					minj=ansy;
				}
			}
	}
	if(ans[mini][minj]=='#')
	{
		for(i=0;i<rear;i++)
		{
			ans[q[i].x][q[i].y]=t;
		}
		t++;
	}
	else
		for(i=0;i<rear;i++)
			ans[q[i].x][q[i].y]=ans[mini][minj];
}
void solve()
{
	int i, j;
	scanf("%d%d",&h,&w);
	for(i=1;i<=h;i++)
		for(j=1;j<=w;j++)
			ans[i][j]='#';
	memset(visit,0,sizeof(visit));
	for(i=1;i<=h;i++)
		for(j=1;j<=w;j++)
			scanf("%d",&map[i][j]);
	t='a';
	for(i=1;i<=h;i++)
		for(j=1;j<=w;j++)
			if(ans[i][j]=='#')
			{
				floodfill(i, j);
			}
	for(i=1;i<=h;i++)
	{
		printf("%c",ans[i][1]);
		for(j=2;j<=w;j++)
			printf(" %c",ans[i][j]);
		printf("\n");	
	}
}
int main()
{
	int i,T;
	freopen("B-large.in","r",stdin);
    freopen("blarge.out","w",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		printf("Case #%d:\n",i);
		solve();
	}
	return 0;
}
