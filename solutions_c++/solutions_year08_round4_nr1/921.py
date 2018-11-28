#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<memory>
#include<math.h>
#include<time.h>
#include<string.h>
#include<algorithm>

using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs; 

#define min(i,j) ((i)<(j)?(i):(j))
#define max(i,j) ((i)>(j)?(i):(j))
#define abx(i) ((i)>0?(i):(-(i)))
#define eps 1e-9

int a[10001][2];
int dp[10001][2][2];
int n,m,x,v;

void dfs(int now)
{
	if(now+now>m)
	{
		dp[now][a[now][0]][0]=0;
		return ;
	}
	int l=now+now;
	int r=l+1;
	dfs(l);
	dfs(r);
	if(a[now][0])
	{
		dp[now][1][0]=min(dp[l][1][0],dp[l][1][1])+min(dp[r][1][0],dp[r][1][1]);
		dp[now][0][0]=min(dp[l][0][0],dp[l][0][1])+min(dp[r][0][0],dp[r][0][1]);
		dp[now][0][0]=min(dp[now][0][0],min(dp[l][0][0],dp[l][0][1])+min(dp[r][1][0],dp[r][1][1]));
		dp[now][0][0]=min(dp[now][0][0],min(dp[l][1][0],dp[l][1][1])+min(dp[r][0][0],dp[r][0][1]));
		if(a[now][1])
		{
			dp[now][1][1]=min(dp[l][0][0],dp[l][0][1])+min(dp[r][1][0],dp[r][1][1])+1;
			dp[now][1][1]=min(dp[now][1][1],min(dp[l][1][0],dp[l][1][1])+min(dp[r][1][0],dp[r][1][1])+1);
			dp[now][1][1]=min(dp[now][1][1],min(dp[l][1][0],dp[l][1][1])+min(dp[r][0][0],dp[r][0][1])+1);
			dp[now][0][1]=min(dp[l][0][0],dp[l][0][1])+min(dp[r][0][0],dp[r][0][1])+1;
		}
	}
	else
	{
		dp[now][1][0]=min(dp[l][0][0],dp[l][0][1])+min(dp[r][1][0],dp[r][1][1]);
		dp[now][1][0]=min(dp[now][1][0],min(dp[l][1][0],dp[l][1][1])+min(dp[r][1][0],dp[r][1][1]));
		dp[now][1][0]=min(dp[now][1][0],min(dp[l][1][0],dp[l][1][1])+min(dp[r][0][0],dp[r][0][1]));
		dp[now][0][0]=min(dp[l][0][0],dp[l][0][1])+min(dp[r][0][0],dp[r][0][1]);
		if(a[now][1])
		{
			dp[now][1][1]=min(dp[l][1][0],dp[l][1][1])+min(dp[r][1][0],dp[r][1][1])+1;
			dp[now][0][1]=min(dp[l][0][0],dp[l][0][1])+min(dp[r][0][0],dp[r][0][1])+1;
			dp[now][0][1]=min(dp[now][0][1],min(dp[l][0][0],dp[l][0][1])+min(dp[r][1][0],dp[r][1][1])+1);
			dp[now][0][1]=min(dp[now][0][1],min(dp[l][1][0],dp[l][1][1])+min(dp[r][0][0],dp[r][0][1])+1);
		}
	}
}

int main()
{
	int ncase,icase=1;
	int i,j,k,t;
	freopen("1.in","r",stdin);
	freopen("wqb.out","w",stdout);
	for(scanf("%d",&ncase);ncase--;)
	{
		scanf("%d%d",&m,&v);
		for(i=1;i<=(m-1)/2;i++)
			scanf("%d%d",&a[i][0],&a[i][1]);
		for(;i<=m;i++)
			scanf("%d",&a[i][0]);
		memset(dp,1,sizeof(dp));
		dfs(1);
		printf("Case #%d: ",icase++);
		if(dp[1][v][0]>m&&dp[1][v][1]>m)
			printf("IMPOSSIBLE\n");
		else printf("%d\n",min(dp[1][v][0],dp[1][v][1]));
	}
	return 0;
}

