#include<stdio.h>
#include<string.h>
#define maxn 110
bool G[maxn][maxn]={0};
int data[maxn][maxn];
bool vis[maxn];
int po[maxn];

bool test(int n1,int n2,int m)
{
	for(int i=0;i<m;++i)
	{
		if(data[n1][i]>=data[n2][i])
			return 0;
	}
	return 1;
}

bool find(int p,int n)
{
	for(int i=0;i<n;++i)
		if(G[p][i]&&!vis[i])
		{
			vis[i]=1;
			if(po[i]==-1||find(po[i],n))
			{
				po[i]=p;
				return 1;
			}
		}
	return 0;
}

int solve()
{
	int n,m;
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;++i)
		for(int j=0;j<m;++j)
			scanf("%d",&data[i][j]);
	for(int i=0;i<n;++i)
		for(int j=0;j<n;++j)
			G[i][j]=test(i,j,m);
	int re=0;
	memset(po,0xff,sizeof(po));
	for(int i=0;i<n;++i)
	{
		memset(vis,0,sizeof(vis));
		if(find(i,n))
			++re;
	}
	return n-re;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
		printf("Case #%d: %d\n",i+1,solve());
	return 0;
}

