#include<cstdio>
#include<cstring>

bool vis[105],g[105][105];
int n,m,test,opp[105],a[105][30];

inline void Format()
{
	memset(g,false,sizeof(g));
	memset(opp,0,sizeof(opp));
}
inline bool find(int u)
{
	for (int i=1;i<=n;++i) if (!vis[i]&& g[u][i])
	{
	 	vis[i]=true;
		if (!opp[i] || find(opp[i])) 
		{
			opp[i]=u;
			return true;	
		}
	}
	return false;
}
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&test);
	int cnt=1;
	for (;test;--test,++cnt)
	{	
		Format();
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;++i)	
		for (int j=1;j<=m;++j) scanf("%d",&a[i][j]);
		for (int i=1;i<=n;++i)
		for (int j=i+1;j<=n;++j)
		{
			int flag;
			if (a[i][1]>a[j][1]) flag=1;
			else if (a[i][1]<a[j][1]) flag=0;
			else flag=-1;
			for (int k=2;k<=m;++k) 
			{
				if (a[i][k]>a[j][k]&& flag==0) flag=-1;
				if (a[i][k]<a[j][k]&& flag==1) flag=-1;
				if (a[i][k]==a[j][k]) flag=-1;
			}
			if (flag==1) g[i][j]=true;
			else if (flag==0) g[j][i]=true;
		}
	//	for (int i=1;i<=n;++i)
		//for (int j=1;j<=n;++j) if (cnt==3 && g[i][j]) printf("%d %d\n",i,j);
		int ans=n;
		for (int i=1;i<=n;++i)
		{
			memset(vis,false,sizeof(vis));
			if (find(i)) --ans;
		}
	//	for (int i=1;i<=n;++i) if (opp[i] && cnt==3) printf("%d %d\n",opp[i],i);
		printf("Case #%d: %d\n",cnt,ans);
	}	
	return 0;
}
