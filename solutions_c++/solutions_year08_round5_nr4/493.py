#include<stdio.h>
#include<memory>
#include<stdlib.h>
#include<algorithm>
#include<string>
using namespace std;
#define  oo 2100000000
#define  l(A) (A<<1)
#define  r(A) ((A<<1)+1)
int w,h,r;
int x[10],y[10];
int d[110][110];
bool vis[110][110];
int que[20000];
bool evil[110][110];
int bfs();
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t = 1;t <= T;++t)
	{
		scanf("%d%d%d",&h,&w,&r);
		memset(evil,0,sizeof(evil));
		for(int i = 0;i < r;++i)
		{
			scanf("%d%d",&x[i],&y[i]);
			evil[x[i]][y[i]] = 1;
		}
		int ans = bfs();
		ans %= 10007;
		printf("Case #%d: %d\n",t,d[h][w]);
	}
}
int bfs()
{
	memset(vis,0,sizeof(vis));
	memset(d,0,sizeof(d));
	int ans = 0;
	d[1][1] = 1;
	int st = 0,en = 0,temp;
	que[en++] = 1001;
	int nx,ny;
	vis[1][1] = 1;
	while(st != en){
		temp = en;
		for(int i = st;i < en;++i){
			nx = que[i]/1000,ny = que[i]%1000;
			if(nx+1 <= h && ny+2 <= w){
				if(((!evil[nx][ny+1])&&(!evil[nx][ny+2])&&(!evil[nx+1][ny+2]))||((!evil[nx+1][ny])&&(!evil[nx+1][ny+1])&&(!evil[nx+1][ny+2])))
					d[nx+1][ny+2] += d[nx][ny];
				d[nx+1][ny+2] %= 10007;
				if(!vis[nx+1][ny+2]){
					vis[nx+1][ny+2] = 1;
					que[temp++] = (nx+1)*1000+ny+2;
				}
			}
			if(nx+2 <= h && ny+1 <= w){
				if(((!evil[nx+1][ny+1])&&(!evil[nx][ny+1])&&(!evil[nx+2][ny+1]))||((!evil[nx+1][ny])&&(!evil[nx+2][ny])&&(!evil[nx+2][ny+1])))
					d[nx+2][ny+1] += d[nx][ny];
				d[nx+2][ny+1] %= 10007;
				if(!vis[nx+2][ny+1]){
					vis[nx+2][ny+1] = 1;
					que[temp++] = (nx+2)*1000+ny+1;
				}
			}	
		}
		st=en;
		en=temp;
	}
	return d[h][w];
}
