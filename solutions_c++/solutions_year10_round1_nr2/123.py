#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define abs(x) ((x)<0?(-(x)):(x))
#define maxn (105)
using namespace std;

int test,D,I,M,N,a[maxn],F[maxn][256];
bool vis[256];
queue<int> Q;

inline void Update(int &x,int y)
{
	if (x==-1 || y<x) x=y; 
}
inline void SPFA(int d[])
{
	for (;!Q.empty();Q.pop());
	memset(vis,0,sizeof(vis));
	for (int i=0;i<=255;++i)
	{
		Q.push(i);
		vis[i]=true;
	}
	for (;!Q.empty();)
	{
		int u=Q.front();
		Q.pop();
		vis[u]=false;
		if (d[u]!=-1)
		{
			for (int v=0;v<=255;++v) if (abs(u-v)<=M)
			{
				int cost=I;
				if (d[v]==-1 || d[u]+cost<d[v])
				{
					d[v]=d[u]+cost;
					if (!vis[v])
					{
						Q.push(v);
						vis[v]=true;
					}
				}
			}
			for (int v=0;v<=255;++v)
			{
				int cost=abs(u-v);
				if (d[v]==-1 || d[u]+cost<d[v])
				{
					d[v]=d[u]+cost;
					if (!vis[v])
					{
						Q.push(v);
						vis[v]=true;
					}
				}
			}
		}
	}
}
int main()
{
	freopen("B_s.in","r",stdin);
	int cnt=1;
	for (scanf("%d",&test);test--;cnt++)
	{
		scanf("%d%d%d%d",&D,&I,&M,&N);
		for (int i=1;i<=N;++i) scanf("%d",&a[i]);
		printf("Case #%d: ",cnt);
		memset(F,-1,sizeof(F));
		F[1][a[1]]=0;
		for (int i=1;i<=N;++i) F[i][a[i]]=D*(i-1);
		for (int i=1;i<=N;++i)
		{
			SPFA(F[i]);
			if (i+1<=N)
			{
				for (int j=0;j<=255;++j) if (F[i][j]!=-1)
				{
					if (abs(a[i+1]-j)<=M) Update(F[i+1][a[i+1]],F[i][j]);
						else 
						{
							if (a[i+1]>j) Update(F[i+1][j+M],F[i][j]+abs(j+M-a[i+1]));
								else Update(F[i+1][j-M],F[i][j]+abs(j-M-a[i+1]));
						}
					Update(F[i+1][j],F[i][j]+D);
				}
			}
		}
		int ans=-1;
		for (int i=0;i<=255;++i) if (F[N][i]!=-1)
			if (ans==-1 || ans>F[N][i]) ans=F[N][i];
		printf("%d\n",ans);
	}
	return 0;
}
