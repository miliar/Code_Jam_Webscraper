#include <cstdio>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

long long dp[10001];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	
	long long l;
	int t,T,n,i,j;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>l>>n;
		int num[100];
		for(i=0;i<n;i++) cin>>num[i];
		for(i=0;i<10001;i++) dp[i]=-1;
		dp[0]=0;

		for(i=0;i<10001;i++)
		{
			if (dp[i]==-1) continue;
			for(j=0;j<n;j++)
			{
				if (i+num[j]>10000) continue;
				if (dp[i+num[j]]==-1 || dp[i+num[j]]>dp[i]+1) dp[i+num[j]]=dp[i]+1;
			}
		}

		long long ans=-1;
		for(i=0;i<n;i++)
		{
			long long take=l/num[i];
			for(j=0;j<=100 && take>=0;j++,take--)
			{
				int left=l-take*num[i];
				if (left<0 || left>10000) continue;
				if (dp[left]==-1) continue;
				if (ans==-1 || ans>take+dp[left])
					ans=take+dp[left];
			}
		}
		
		if (ans!=-1)
			printf("Case #%d: %lld\n",t,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n",t);
	}

	return 0;
}
