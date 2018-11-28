#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

bool vst[105][105];
char G[105][105];
int mp[105][105],T,cas=1;
int H,W,move[4][2]={-1,0,0,-1,0,1,1,0};
int stx,sty;

bool in(int x,int y)
{
	if(x<0||y<0||x>=H||y>=W)
		return false;
	return true;
}

void search(int x,int y)
{
	int minval=100000,d=-1;
	for(int i=0;i<4;i++)
	{
		int nx=x+move[i][0],ny=y+move[i][1];
		if(!in(nx,ny)) continue;
		if(mp[nx][ny]<mp[x][y]&&mp[nx][ny]<minval&&!vst[nx][ny])
			minval=mp[nx][ny],d=i;
	}
	if(d==-1)
	{
		stx=x,sty=y;
		return ;
	}
	search(x+move[d][0],y+move[d][1]);
}

void dfs(int x,int y,char ch)
{
	vst[x][y]=true;G[x][y]=ch;
	for(int i=0;i<4;i++)
	{
		int nx=x+move[i][0],ny=y+move[i][1];
		if(!in(nx,ny)||vst[nx][ny]) continue;
		if(mp[nx][ny]>mp[x][y])
		{
			int minval=100000,d=-1;
			for(int j=0;j<4;j++)
			{
				int mx=nx+move[j][0],my=ny+move[j][1];
				if(in(mx,my)&&mp[mx][my]<mp[nx][ny]&&mp[mx][my]<minval)
					minval=mp[mx][my],d=j;
			}
			if(x==nx+move[d][0]&&y==ny+move[d][1])
				dfs(nx,ny,ch);
		}
	}
}

int main()
{
	freopen("d://B-large.in","r",stdin);
	freopen("d://2.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&H,&W);
		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)
				scanf("%d",&mp[i][j]);
		memset(vst,false,sizeof(vst));
		char ch='a';
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				if(vst[i][j]) continue;
				search(i,j);
				dfs(stx,sty,ch);
				ch++;
			}
		}
		printf("Case #%d:\n",cas++);
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W-1;j++)
				printf("%c ",G[i][j]);
			printf("%c\n",G[i][W-1]);
		}
	}
	return 0;
}