#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define maxn 3000
#define inf 200000000LL

long long f[maxn][maxn];
int p,bit[100],Cnt[maxn],M[maxn],price[maxn];

inline void search(int dep,int u,int stat)
{
	if (dep==p)
	{
		if (p-Cnt[stat]>M[u-bit[p]]) f[u][stat]=inf;
		else f[u][stat]=0;
		return;
	}
	int left=u*2,right=u*2+1;
	
	if (f[left][stat]==-1) search(dep+1,left,stat);
	if (f[right][stat]==-1) search(dep+1,right,stat);
	int nst=stat+bit[dep];
	if (f[left][nst]==-1) search(dep+1,left,nst);
	if (f[right][nst]==-1) search(dep+1,right,nst);
	
	f[u][stat]=min(f[left][nst]+f[right][nst]+price[u],f[left][stat]+f[right][stat]);
}

int main()
{
	freopen("B_large.in","r",stdin);
	freopen("B_large.out","w",stdout);
	
	bit[0]=1;
	for (int i=1;i<=20;++i)
		bit[i]=bit[i-1]*2;
	for (int i=1;i<=2500;++i)
		Cnt[i]=Cnt[i/2]+(i&1);
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		scanf("%d",&p);
		for (int i=0;i<bit[p];++i)
			scanf("%d",&M[i]);
		for (int i=p-1;i>=0;--i)
			for (int j=bit[i];j<bit[i+1];++j)
				scanf("%d",&price[j]);
		
		memset(f,-1,sizeof(f));
		search(0,1,0);
		printf("Case #%d: %I64d\n",test,f[1][0]);
	}
	return 0;
}
