#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int n,m,a[102][102],l[102];
bool visit[102],dist[102][102];

inline bool Down(int i,int j)
{
	for (int k=0;k<m;k++)
	if (a[i][k]>=a[j][k]) return false;
	return true;
}

inline bool Extended_path(int u)
{
	for (int v=1;v<=n;v++)
	if (dist[u][v] && !visit[v]) {
		visit[v]=1;
		if (!l[v] || Extended_path(l[v]))
			return l[v]=u,true;
	}
	return false;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int Test,Case=0;
	for (scanf("%d",&Test);Test;--Test) {
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++)
		for (int j=0;j<m;j++)
			scanf("%d",&a[i][j]);
		memset(dist,0,sizeof(dist));
		for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
		if (Down(i,j)) dist[i][j]=1;
		int ret=n;
		memset(l,0,sizeof(l));
		for (int i=1;i<=n;i++) {
			memset(visit,0,sizeof(visit));
			if (Extended_path(i)) --ret;
		}
		printf("Case #%d: %d\n",++Case,ret);
	}
	return 0;
}
