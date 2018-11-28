#include <stdio.h>
#include <algorithm>

using namespace std;

bool u[1000];
int a[1000];
int dp[1000][1000];

int dfs(int i,int j)
{
	int k,z,mi;
	if(j-i==1)
		dp[i][j]=0;
	if(dp[i][j]!=-1)
		return dp[i][j];
	mi=999999999;
	for(k=i+1;k<j;k++)
	{
		z=a[j]-a[i]-2+dfs(i,k)+dfs(k,j);
		if(z<mi)
			mi=z;
	}
	dp[i][j]=mi;
	return mi;
}

int main()
{
	int T,t,i,n,m,mi,c,j;
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++)
		{
			scanf("%d",&a[i]);
			a[i]--;
		}
		a[m]=-1;
		a[m+1]=n;
		m+=2;
		sort(a,a+m);
		for(i=0;i<m;i++)
			for(j=0;j<m;j++)
				dp[i][j]=-1;
		printf("%d\n",dfs(0,m-1));
	}
	return 0;
}