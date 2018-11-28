#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <vector>
#include <memory.h>

using namespace std;

const int MAXN=1<<20;

int dp[2][MAXN];
int q[MAXN];

int main()
{
	int T;
	cin >> T;
	for(int tNum=0; tNum<T; ++tNum)
	{
		for(int i=0; i<MAXN; ++i)	
			dp[1][i]=dp[0][i]=-1;
		dp[0][0]=0;
		int r=0;
		q[r++]=0;
		int N;
		cin >> N;
		int *a=new int[N];
		int totSum=0;
		int summ=0;
		for(int i=0; i<N; ++i)
		{
			cin >> a[i];
			totSum^=a[i];
			summ+=a[i];
			int rOld=r;
			int on=i%2, nn=1-on;
			for(int j=0; j<rOld; ++j){
				int newSum=q[j]^a[i];
				int val=dp[on][q[j]]+a[i];
				if(dp[on][newSum]==-1)
					q[r++]=newSum;
				dp[nn][newSum]=max(dp[on][newSum],val);
			}
			for(int j=0; j<r; ++j)
				dp[nn][q[j]]=max(dp[nn][q[j]],dp[on][q[j]]);
		}
		int ans=-1;
		int nn=N%2;
		for(int i=0; i<MAXN; ++i)
		{
			if(dp[nn][i]==-1 || dp[nn][i]==0 || dp[nn][i]==summ) continue;
			if(i==(totSum^i)){
				ans=max(ans,dp[nn][i]);
			}
		}
		printf("Case #%d: ",tNum+1);
		if(ans==-1)
			printf("NO\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}
