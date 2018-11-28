#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn=410;
bool g[maxn][maxn];
bool f[maxn][maxn];
int s[maxn][maxn];
int n,m;
void init()
{
	scanf("%d%d",&n,&m);
	memset(g,0,sizeof(g));
	for(int i=0;i<m;i++)
	{
		int a,b;
		scanf("%d,%d",&a,&b);
		g[a][b]=g[b][a]=true;
//		printf("a=%d b=%d\n",a,b);
	}
}
pair<int,int> solve()
{
	int d[maxn];
	memset(d,255,sizeof(d));
	int q[maxn],h=0,e=1;
	q[0]=0;
	d[0]=0;
	while(h<e)
	{
		for(int i=0;i<n;i++)
		{
			if(!g[q[h]][i]) continue;
			if(d[i]>=0) continue;
			d[i]=d[q[h]]+1;
			q[e++]=i;
		}
		h++;
	}
	pair<int,int> ans(d[1]-1,0);
	if(ans.first==0)
	{
		for(int i=1;i<n;i++)
			if(g[0][i]) ans.second++;
		return ans;
	}
	memset(f,0,sizeof(f));
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
		{
			if(d[i]>=0&&d[j]>=0&&d[i]+1==d[j]&&g[i][j]) f[i][j]=true;
		}
	memset(s,0,sizeof(s));
	for(int i=0;i<n;i++)
	{
		if(!f[0][i]) continue;
		for(int j=1;j<n;j++)
			if(j!=i&&(g[0][j]||g[i][j])) s[0][i]++;
	}
	for(int i=1;i<h;i++)
	{
		int u=q[i];
		for(int v=0;v<n;v++)
		{
			if(!f[u][v]) continue;
			for(int j=0;j<n;j++)
			{
				if(!f[j][u]) continue;
				int t=s[j][u];
				for(int k=0;k<n;k++)
				{
					if(!g[v][k]) continue;
					if(g[u][k]) continue;
					if(g[j][k]) continue;
					if(!g[v][k]) continue;
					t++;
				}
				s[u][v]=max(s[u][v],t-1);
			}
		}
	}
	//for(int i=0;i<n;i++) printf("%d: %d\n",i,d[i]);
	for(int i=0;i<n;i++)
	{
		if(d[i]!=ans.first) continue;
		if(!f[i][1]) continue;
		for(int j=0;j<n;j++)
		{
			if(!f[j][i]) continue;
			//printf("check %d,%d\n",j,i);
			ans.second=max(ans.second,s[j][i]);
		}
	}
	/*for(int i=0;i<n;i++)
	{
		printf("%2d:",i);
		for(int j=0;j<n;j++) printf("%2d",s[i][j]);
		putchar('\n');
	}*/
	return ans;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		init();
		pair<int,int> ans=solve();
		printf("Case #%d: %d %d\n",cs,ans.first,ans.second);
	}
	return 0;
}
