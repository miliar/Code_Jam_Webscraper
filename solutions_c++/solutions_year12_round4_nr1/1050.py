#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <vector>

using namespace std;

typedef pair<int,int> pii;

int dp[10050];
int d[10050],l[10050];

int main()
{
	int t;
	int n,dd;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin >> t;
	for (int cnt=1;cnt<=t;cnt++)
	{
		cin >> n;
		for (int i=0;i<n;i++)
			scanf("%d%d",d+i,l+i);
		scanf("%d",&dd);
		memset(dp,0,sizeof(dp));
		dp[0]=d[0];
		d[n]=dd;
		for (int i=0;i<n;i++)
		{
			dp[i]=min(dp[i],l[i]);
			for (int j=i+1;j<=n && d[j]-d[i]<=dp[i];j++)
				dp[j]=max(dp[j],d[j]-d[i]);
		}
		printf("Case #%d: ",cnt);
		if (dp[n]) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}