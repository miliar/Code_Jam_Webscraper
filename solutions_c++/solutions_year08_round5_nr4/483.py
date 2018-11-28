#include <cstdio>
#include <cstring>

int w,h,r;
int x[10],y[10];
int d[110][110];
bool vis[110][110];
int que[20000];
bool isevil[110][110];

int bfs()
{
	memset(vis,0,sizeof(vis));
	memset(d,0,sizeof(d));
	int ans = 0;
	d[1][1] = 1;
	int st = 0,en = 0,temp;
	que[en++] = 1001;
	int xx,yy;
	vis[1][1] = 1;
	while(st != en)
	{
		temp = en;
		for(int i = st;i < en;++i)
		{
			xx = que[i]/1000;
			yy = que[i]%1000;
			if(xx+1 <= h && yy+2 <= w)
			{
				if(((!isevil[xx][yy+1]) && (!isevil[xx][yy+2]) && (!isevil[xx+1][yy+2])) || ((!isevil[xx+1][yy]) && (!isevil[xx+1][yy+1]) && (!isevil[xx+1][yy+2])))
					d[xx+1][yy+2] += d[xx][yy];
				d[xx+1][yy+2] %= 10007;
				if(!vis[xx+1][yy+2])
				{
					vis[xx+1][yy+2] = 1;
					que[temp++] = (xx+1)*1000+yy+2;
				}
			}
			if(xx+2 <= h && yy+1 <= w)
			{
				if(((!isevil[xx+1][yy+1]) && (!isevil[xx][yy+1]) && (!isevil[xx+2][yy+1])) || ((!isevil[xx+1][yy]) && (!isevil[xx+2][yy]) && (!isevil[xx+2][yy+1])))
					d[xx+2][yy+1] += d[xx][yy];
				d[xx+2][yy+1] %= 10007;
				if(!vis[xx+2][yy+1])
				{
					vis[xx+2][yy+1] = 1;
					que[temp++] = (xx+2)*1000+yy+1;
				}
			}	
		}
		st = en;
		en = temp;
	}
	return d[h][w];
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t = 1;t <= T;++t)
	{
		scanf("%d%d%d",&h,&w,&r);
		memset(isevil,0,sizeof(isevil));
		for(int i = 0;i < r;++i)
		{
			scanf("%d%d",&x[i],&y[i]);
			isevil[x[i]][y[i]] = 1;
		}
		int ans = bfs();
		ans %= 10007;
		printf("Case #%d: %d\n",t,d[h][w]);
	}
}