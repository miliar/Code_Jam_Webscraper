#include <queue>
#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(i,a)for(int i=0;i<(a);i++)

bool col[2000],inQ[2000];
int C,N,M,gra[2000],des[3000],nex[3000],sp[2000],m,rem[2000];
deque<int> Q;

int main()
{
	freopen("B.in","r",stdin);freopen("B.out","w",stdout);
	scanf("%d",&C);
	REP(c,C)
	{
		bool ok=1;
		scanf("%d%d",&N,&M);
		memset(gra,-1,sizeof(gra));
		memset(sp,-1,sizeof(sp));
		memset(rem,0,sizeof(rem));
		memset(col,0,sizeof(col));
		memset(inQ,0,sizeof(inQ));
		m=0;
		Q.clear();
		REP(i,M)
		{
			int T,X,Y;
			scanf("%d",&T);
			while(T--)
			{
				scanf("%d%d",&X,&Y);
				X--;
				if(Y)sp[i]=X;
				else
				{
					rem[i]++;
					des[m]=i;
					nex[m]=gra[X];
					gra[X]=m++;
				}
			}
			if(!rem[i])
			{
				if(sp[i]==-1)
				{
					ok=0;
					goto next;
				}
				if(!inQ[sp[i]])
				{
					Q.push_back(sp[i]);
					inQ[sp[i]]=1;
				}
			}
		}
		while(!Q.empty())
		{
			int u=Q.front(),v;
			Q.pop_front();
			col[u]=1;
			for(int i=gra[u];i!=-1;i=nex[i])
			{
				rem[v=des[i]]--;
				if(!rem[v])
				{
					if(sp[v]==-1)
					{
						ok=0;
						goto next;
					}
					if(!inQ[sp[v]])
					{
						Q.push_back(sp[v]);
						inQ[sp[v]]=1;
					}
				}
			}
		}
next:	printf("Case #%d:",c+1);
		if(!ok)printf(" IMPOSSIBLE");
		else REP(i,N)printf(" %d",col[i]?1:0);
		printf("\n");
	}
	return 0;
}
