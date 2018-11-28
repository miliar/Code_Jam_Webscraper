/*
problem: saving the univers
goolge code jam 2008
*/
using namespace std;
#include <cstdio>
#include <algorithm>
#include <string>

char a[128][128];

int T, n, m;

int q[1024];

int dp[1001][101];

void read()
{
	int i,j;
	scanf("%d\n", &n);
	
	for(i=1;i<=n;++i) gets(a[i]);
	
	scanf("%d\n", &m);

//	for(i=1;i<=n;++i) printf("%s\n",a[i]);
	
	char ax[128];
	
	for(i=1;i<=m;++i)
	{
		gets(ax);
		for(j=1;j<=n;++j)
			if(strcmp(ax, a[j])==0) { q[i]=j;break;}
	}
	
	
}

void solve()
{
	
	int i, j, k;
	memset(dp,0,sizeof(dp));
	
	for(i=1;i<=n;++i) if(i==q[1])dp[1][i]=0x3f3f3f3f;
	
	for(i=2;i<=m;++i)
		for(j=1;j<=n;++j)
			if(q[i]  != j)
			{
				dp[i][j]=0x3f3f3f3f;
				
				if(q[i-1] != j)
					dp[i][j]=min(dp[i][j], dp[i-1][j]);
				
				for(k=1;k<=n;++k)
					if(j!=k)
						if(q[i-1] != k)
							dp[i][j]=min(dp[i][j], dp[i-1][k]+1);
			}
			else dp[i][j]=0x3f3f3f3f;
			
	int sol=0x3f3f3f3f;
	for(i=1;i<=n;++i) sol=min(sol, dp[m][i]);
	
	
	printf("%d\n", sol);
	
			
	
}

int main()
{
	freopen("univers.in","r",stdin);
	freopen("univers.out","w",stdout);
	scanf("%d\n", &T);
	
	
	for(int i=1;i<=T;++i)
	{
		printf("Case #%d: ",i);
		read();
		solve();
	}
	return 0;
}


