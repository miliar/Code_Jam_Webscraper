#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>
#include<math.h>
#include<queue>
#include<sstream>
#include<algorithm>
#include<set>
using namespace std;
const int INF=1<<30;
typedef __int64 ll;

struct node
{
	int x,y,h;
}p[10100];
class prio
{
	public:
	bool operator()(const node &x , const node &y)
	{
		return x.h > y.h;
	}  //>表示最小堆
};
int n,m;
int g[200][200];
int gg[200][200];
int flag;
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int isok(int x,int y) 
{
	if(x>=0&&x<n&&y>=0&&y<m) return 1;
	return 0;
}
void dfs(int x,int y)
{
	int i,j,k;
	gg[x][y]=flag;
	for(i=0;i<4;i++) 
	{
		int xx=x+dir[i][0],yy=y+dir[i][1];
		if(isok(xx,yy)==0) continue;
		if(gg[xx][yy]>0||g[xx][yy]<=g[x][y]) continue;
		int x2=-1,y2=-1,mi=g[xx][yy];
		for(j=0;j<4;j++) 
		{
			int tx=xx+dir[j][0],ty=yy+dir[j][1];
			if(isok(tx,ty)&&mi>g[tx][ty])
			{
				mi=g[tx][ty];x2=tx;y2=ty;
			}
		}
		if(x2==x&&y2==y) 
		{
			dfs(xx,yy);
		}
	}
}
char ch;
char des[200][200];
void dfs2(int x,int y) 
{
	des[x][y]=ch;
	for(int i=0;i<4;i++) 
	{
		int xx=x+dir[i][0],yy=y+dir[i][1];
		if(isok(xx,yy)&&gg[xx][yy]==gg[x][y]&&des[xx][yy]==0) 
		{
			dfs2(xx,yy);
		}
	}
}
void play()
{
	int i,j;
	priority_queue< node , vector<node> , prio > que;
	for(i=0;i<n;i++) for(j=0;j<m;j++) 
	{
		node temp;
		temp.x=i;temp.y=j;temp.h=g[i][j];
		que.push(temp);
	}
	flag=0;
	memset(gg,-1,sizeof(gg));
	while(!que.empty())
	{
		node temp=que.top();que.pop();
		if(gg[temp.x][temp.y]>=0) continue;
		flag++;
		dfs(temp.x,temp.y);
	}
	ch='a';
	memset(des,0,sizeof(des));
	for(i=0;i<n;i++) for(j=0;j<m;j++) 
	{
		if(des[i][j]==0)
		{
			dfs2(i,j);ch++;
		}
	}
}


int main()
{
	int i,j,k,ca,kk=1;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&ca);
	while(ca--) 
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++) for(j=0;j<m;j++) scanf("%d",&g[i][j]);
		play();
		printf("Case #%d:\n",kk++);
		for(i=0;i<n;i++) 
		{
			for(j=0;j<m;j++) printf("%c ",des[i][j]);
			printf("\n");
		}
	}
	return 0;
}