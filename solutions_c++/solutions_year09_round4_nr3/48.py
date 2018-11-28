#include <cstdio>
#include <cstring>

#define maxn 105
#define maxm 30

bool adj[maxn][maxn],vis[maxn];
int n,m,a[maxn][maxm],Link[maxn];

inline bool Find(int x)
{
	for (int y=0;y<n;++y)
	if (adj[x][y] && !vis[y])
	{
		vis[y]=true;
		if (Link[y]==-1 || Find(Link[y]))
		{
			Link[y]=x;
			return true;
		}
	}
	return false;
}

int main()
{
	freopen("C_large.in","r",stdin);
	freopen("C_large.out","w",stdout);
	
	int test=1,T;
	for (scanf("%d",&T);test<=T;++test)
	{
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
				scanf("%d",&a[i][j]);
		for (int i=0;i<n;++i)
			for (int j=0;j<n;++j)
			{
				bool fl=true;
				for (int k=0;k<m;++k)
				if (a[i][k]<=a[j][k])
				{
					fl=false;
					break;
				}
				adj[i][j]=fl;
			}
		int ans=0;
		memset(Link,-1,sizeof(Link));
		for (int i=0;i<n;++i)
		{
			memset(vis,false,sizeof(vis));
			if (Find(i)) ++ans;
		}
		printf("Case #%d: %d\n",test,n-ans);
	}
	return 0;
}
