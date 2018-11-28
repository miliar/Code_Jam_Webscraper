#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int dp[110][110];
int que[110];
int n,p,q;

int find(int l,int r)
{
	if(dp[l][r]!=-1) return dp[l][r];
	if(r==l+1) return dp[l][r]=0;
	int tmp,i;
	dp[l][r]=0x7FFFFFFF;
	for(i=l+1;i<r;i++)
	dp[l][r]=min(dp[l][r],find(l,i)+find(i,r)+que[r]-que[l]-2);
	return dp[l][r];
}



int main()
{
	int i,j,k,t;
	freopen("C.small.out","w",stdout);
	scanf("%d",&n);
	for(t=1;t<=n;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d%d",&p,&q);
		for(i=1;i<=q;i++)
			scanf("%d",&que[i]);
		que[0]=0;
		que[q+1]=p+1;
		sort(&que[1],&que[q + 1]);
        memset(dp,-1,sizeof(dp));
		printf("%d\n",find(0,q+1));
	}
	return 0;
}


