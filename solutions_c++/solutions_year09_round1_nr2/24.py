#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<map>
#include<set>
#include<algorithm>

using namespace std;

const int inf = 2147483647;
const double pi = acos(-1.0);
const double eps = 1e-7;
const int maxn = 22;
const int maxq = maxn*maxn*20;

int n,m,ntest;
int s[maxn][maxn],w[maxn][maxn],t[maxn][maxn];
int dist[maxn][maxn][4];
int queue[maxq],begin,end;
int inq[maxn][maxn][4];

void relax(int x,int y,int u,int d)
{
	if(x<0 || x>=n || y<0 || y>=m) return;
	if(dist[x][y][u]==-1 || dist[x][y][u]>d)
	{
		dist[x][y][u] = d;
		if(inq[x][y][u]==0)
		{
			inq[x][y][u] = 1;
			queue[end++] = x; if(end==maxq)end=0;
			queue[end++] = y; if(end==maxq)end=0;
			queue[end++] = u; if(end==maxq)end=0;
		}
	}
}

int spfa()
{
	begin = end = 0;
	queue[end++] = n-1; queue[end++] = 0; queue[end++] = 1;
	memset(dist,-1,sizeof(dist));
	dist[n-1][0][1] = 0; inq[n-1][0][1] = 1;
	while(begin!=end)
	{
		int x = queue[begin++]; if(begin==maxq) begin=0;
		int y = queue[begin++]; if(begin==maxq) begin=0;
		int u = queue[begin++]; if(begin==maxq) begin=0;
		inq[x][y][u] = 0;
		int d = dist[x][y][u];
		
		int xx,yy,uu,dd;
		if((u&1)==0) xx=x-1; else xx=x+1; yy=y; uu=u^1; dd=d+2;
		relax(xx,yy,uu,dd);
		if((u&2)==0) yy=y-1; else yy=y+1; xx=x; uu=u^2; dd=d+2;
		relax(xx,yy,uu,dd);
		
		int tmp = ((d-t[x][y])%w[x][y]+w[x][y])%w[x][y];
		if(tmp<s[x][y]) relax(x,y,u^1,d+1); else relax(x,y,u^1,d+w[x][y]-tmp+1);
		if(tmp<s[x][y]) relax(x,y,u^2,d+s[x][y]-tmp+1); else relax(x,y,u^2,d+1);
	}
	return dist[0][m-1][2];
}

int main()
{
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
			{
				scanf("%d%d%d",&s[i][j],&w[i][j],&t[i][j]);
				w[i][j] += s[i][j];
				t[i][j] %= w[i][j];
			}
		int ans = spfa();
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}


