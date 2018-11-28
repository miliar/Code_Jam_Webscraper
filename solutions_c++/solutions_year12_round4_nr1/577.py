#include <cstdio>
#include <queue>
#include <cstring>
const int N=10010;
int d[N],l[N];
int DP[N];
bool flag[N];
std::queue<int>Q;
inline int min(int a,int b){return a<b?a:b;}
inline int max(int a,int b){return a>b?a:b;}
int main()
{
	int T,n,w=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
			scanf("%d%d",&d[i],&l[i]);
		int D;
		scanf("%d",&D);
		for(int i=1;i<=n;i++)
			DP[i]=-(1<<30);
		DP[1]=min(d[1],l[1]);
		Q.push(1);
		bool ok=false;
		memset(flag,0,sizeof(flag));
		while(!Q.empty())
		{
			int x=Q.front();
			Q.pop();
			for(int i=x+1;i<=n;i++)
			{
				if(DP[x]>=d[i]-d[x])
				{
					if(min(l[i],d[i]-d[x]) > DP[i])
					{
						DP[i]=min(l[i],d[i]-d[x]);
						if(!flag[i])
							Q.push(i);
						flag[i]=true;
					}
				}
				else break;
			}
			for(int i=x-1;i>=1;i--)
			{
				if(DP[x]>=d[x]-d[i])
				{
					if(min(l[i],d[x]-d[i]) > DP[i])
					{
						DP[i]=min(l[i],d[x]-d[i]);
						if(!flag[i])
							Q.push(i);
						flag[i]=true;
					}
				}
				else break;
			}
		}
		for(int i=1;i<=n;i++)
			if(DP[i]+d[i]>=D)ok=true;
		printf("Case #%d: ",w++);
		puts(ok?"YES":"NO");
	}
}
