#include <stdio.h>
#include <string.h>

int T,t,m[5000],a[2000],p,p2,i,j,dep[5000];
int dp[2000][20];

int rec(int root,int dec)
{
	if(dp[root][dec]!=-1)
		return dp[root][dec];
	if(m[root]<=dec)
		return dp[root][dec]=0;
	if(root>=p2/2)
		return dp[root][dec]=a[root];
	int z=a[root]+rec(2*root,dec+1)+rec(2*root+1,dec+1);
	int y=rec(2*root,dec)+rec(2*root+1,dec);
	if(m[root]-dec==dep[root])
		dp[root][dec]=z;
	else
		dp[root][dec]=z>y?y:z;
	return dp[root][dec];
}

int main()
{
	freopen("b.in","r",stdin);	freopen("b.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		memset(dp,-1,sizeof(dp));
		memset(dep,0,sizeof(dep));
		scanf("%d",&p);
		p2=1<<p;
		for(i=p2;i<2*p2;i++)
		{
			scanf("%d",&m[i]);
			m[i]=p-m[i];
		}
		for(i=p2-1;i;i--)
		{
			m[i]=m[2*i]>m[2*i+1]?m[2*i]:m[2*i+1];
			dep[i]=dep[2*i]+1;
		}
		for(i=p2/2;i;i/=2)
			for(j=i;j<i+i;j++)
				scanf("%d",&a[j]);
		printf("Case #%d: %d\n",t,rec(1,0));
	}
	return 0;
}