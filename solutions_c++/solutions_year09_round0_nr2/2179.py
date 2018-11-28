#include <cstdio>
#include <cstring>

int T;
int h,w;
int alt[110][110];
char ans[110][110];
bool vis[110][110];
int to[110][110];

int dfs(int a,int b)
{
	if(vis[a][b])
		return to[a][b];
	vis[a][b] = 1;
	int min = alt[a][b];
	if(alt[a-1][b] < min)
		min = alt[a-1][b];
	if(alt[a+1][b] < min)
		min = alt[a+1][b];
	if(alt[a][b-1] < min)
		min = alt[a][b-1];
	if(alt[a][b+1] < min)
		min = alt[a][b+1];
	if(min == alt[a][b])
	{
		to[a][b] = a*1000+b;
		return to[a][b];
	}
	if(min == alt[a-1][b])
	{
		dfs(a-1,b);
		to[a][b] = to[a-1][b];
		return to[a][b];
	}
	if(min == alt[a][b-1])
	{
		dfs(a,b-1);
		to[a][b] = to[a][b-1];
		return to[a][b];
	}
	if(min == alt[a][b+1])
	{
		dfs(a,b+1);
		to[a][b] = to[a][b+1];
		return to[a][b];
	}
	dfs(a+1,b);
	to[a][b] = to[a+1][b];
	return to[a][b];
}

void init()
{
	for(int i = 0;i <= h+1;++i)
		alt[i][0] = alt[i][w+1] = 10001;
	for(int i = 0;i <= w+1;++i)
		alt[0][i] = alt[h+1][i] = 10001;
	memset(vis,0,sizeof(vis));
}

int main()
{
	freopen("2large.out","w",stdout);
	freopen("B-large.in","r",stdin);
	scanf("%d",&T);
	for(int t = 1;t <= T;++t)
	{
		scanf("%d%d",&h,&w);
		init();
		for(int i = 1;i <= h;++i)
			for(int j = 1;j <= w;++j)
				scanf("%d",&alt[i][j]);
		for(int i = 1;i <= h;++i)
			for(int j = 1;j <= w;++j)
				dfs(i,j);
		char now = 'a';
		memset(vis,0,sizeof(vis));
		for(int i = 1;i <= h;++i)
		{
			for(int j = 1;j <= w;++j)
			{
				int a = to[i][j]/1000;
				int b = to[i][j]%1000;
				if(!vis[a][b])
				{
					vis[a][b] = 1;
					ans[a][b] = now++;
				}
				ans[i][j] = ans[a][b];
			}
		}
		printf("Case #%d:\n",t);
		for(int i = 1;i <= h;++i)
		{
			printf("%c",ans[i][1]);
			for(int j = 2;j <= w;++j)
				printf(" %c",ans[i][j]);
			printf("\n");
		}
	}
	return 0;
}