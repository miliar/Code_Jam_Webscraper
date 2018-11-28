#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(i,a)for(int i=0;i<(a);i++)
#define OR(i)(t[i]==0?0:c[i]==1?1:-20000)
#define AND(i)(t[i]==1?0:c[i]==1?1:-20000)

int N,M,V,t[10000],c[10000],d[10000][2];

inline void update(int &a, int b){if((a==-1||a>b)&&b>=0)a=b;}

int main()
{
	freopen("A.in","r",stdin);freopen("A.out","w",stdout);
	scanf("%d",&N);
	REP(C,N)
	{
		scanf("%d%d",&M,&V);
		memset(d,-1,sizeof(d));
		REP(i,M)
		{
			scanf("%d",t+i);
			if(i<(M-1>>1))scanf("%d",c+i);
		}
		for(int i=M-1>>1;i<M;i++)d[i][t[i]]=0;
		for(int i=(M-1>>1)-1;i>=0;i--)
		{
			int u=(i<<1)+1,v=(i<<1)+2;
			REP(j,2)if(d[u][j]!=-1)REP(k,2)if(d[v][k]!=-1)
			{
				update(d[i][j&k],d[u][j]+d[v][k]+AND(i));
				update(d[i][j|k],d[u][j]+d[v][k]+OR(i));
			}
		}
		printf("Case #%d: ",C+1);
		if(d[0][V]==-1)puts("IMPOSSIBLE");
		else printf("%d\n",d[0][V]);
	}
	return 0;
}
