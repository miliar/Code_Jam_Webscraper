#include<stdio.h>
#define N 110
const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};
const short inf=32000;
int T,h,w;
char c;
short a[N][N];
char cod[N][N];
inline void citire()
{
	scanf("%d%d",&h,&w);
	for(int i=1; i<=h; ++i)
	{
		for(int j=1; j<=w; ++j)
			scanf("%hd",&a[i][j]);
		a[i][0]=inf;
		a[i][w+1]=inf;
	}
	int w1=w+1;
	int h1=h+1;
	for(int i=0; i<=w1; ++i)
	{
		a[0][i]=inf;
		a[h1][i]=inf;
	}
}
void dfs(int x,int y)
{
	if(cod[x][y])
		return;
	int x1,y1,x2,y2;
	x2=x;
	y2=y;
	for(int i=0; i<4; ++i)
	{
		x1=x+dx[i];
		y1=y+dy[i];
		if(a[x1][y1]<a[x2][y2])
		{
			x2=x1;
			y2=y1;
		}
	}
        if(x==x2 && y==y2)
	{
       		++c;
		cod[x][y]=c;
		return;
	}
	dfs(x2,y2);
	cod[x][y]=cod[x2][y2];
}				
inline void rezolva()
{
	citire();
	c='a'-1;
	for(int i=1; i<=h; ++i)
	{
		for(int j=1; j<=w; ++j)
		{
			if(cod[i][j]==0)
				dfs(i,j);
		}
	}

	for(int i=1; i<=h; ++i)
	{
		for(int j=1; j<w; ++j)
                {
			fputc(cod[i][j],stdout);
			fputc(' ',stdout);
			cod[i][j]=0;
		}
		fputc(cod[i][w],stdout);
		fputc('\n',stdout);
		cod[i][w]=0;
	}
}
int main()
{
	freopen("pb.in","r",stdin);
	freopen("pb.out","w",stdout);
        scanf("%d",&T);
        for(int i=1; i<=T; ++i)
	{
		printf("Case #%d:\n",i);
		rezolva();
	}
	return 0;
}

