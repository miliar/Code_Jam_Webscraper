#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;

int a[110];
int vis[110];
int dp[35][2];
//dp[i][0] not surprise
//dp[i][1] surprise
void solve()
{
	dp[0][0]=0;
	dp[0][1]=-1;
	dp[1][0]=1;
	dp[1][1]=-1;
	for(int i=2;i<=30;i++)
	{
        if(i%3==0)
		{
			dp[i][0]=i/3;
			dp[i][1]=i/3+1;
		}
		if(i%3==1)
		{
           dp[i][0]=i/3+1;
		   dp[i][1]=i/3+1;
		}
		if(i%3==2)
		{
		   dp[i][0]=i/3+1;
           dp[i][1]=i/3+2;
		}
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    int t,n,s,p;
	int tca=1;
	solve();
	scanf("%d",&t);
	while(t--)
	{
         scanf("%d %d %d",&n,&s,&p);
         for(int i=0;i<n;i++)
			 scanf("%d",&a[i]);
		 memset(vis,0,sizeof(vis));
		 sort(a,a+n);

		 int sum=0;
		 for(int i=0;i<=n-1;i++)
		 {
			 if(sum==s)
                break;
			 if(dp[a[i]][1]>=p)
			 {
				 vis[i]=1;
				 sum+=1;
			 }
		 }

		 int ans=0;
		 for(int i=0;i<=n-1;i++)
		 {
			 if(vis[i]==1)
				 ans+=1;
			 else if(dp[a[i]][0]>=p)
				 ans+=1;
		 }
		 printf("Case #%d: %d\n",tca++,ans);

	}
	return 0;
}