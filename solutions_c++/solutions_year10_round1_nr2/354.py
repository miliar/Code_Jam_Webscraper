#include<iostream>
#include<algorithm>


using namespace std;

int dp[2][257];

int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("B-small-attempt2.out","w",stdout);

	int T;
	cin>>T;
	for(int tt=1;tt<=T;++tt)
	{
		int D,I,M,n,ans=0x7f7f7f7f;
		memset(dp,0,sizeof(dp));
		cin>>D>>I>>M>>n;

		for(int i=0;i<n;i++)
		{
			int a,curr = i&1,prev = !curr;
			scanf("%d",&a);

			for(int j=0;j<256;j++)
			{
				int modifycost = abs(a-j);
				int buildcost = D+I;
				int changecost = min(modifycost,buildcost);

				if (i==0)
				{
					dp[0][j] = changecost;
				}
				else
				{
					int mincost = 0x7f7f7f7f;
					for(int k=0;k<256;k++)
					{
						int tmp = 0x7f7f7f7f;
						if (j==k) tmp = D+dp[prev][k];
						int dist = abs(j-k);
						int insertcost = M==0?j==k?0:0x0f0f0f0f:(I*(dist>M?(dist)/M+!(dist%M==0)-1:0));
						tmp = min(tmp,changecost+insertcost+dp[prev][k]);
						mincost = min(mincost,tmp);
					}

					mincost = min(mincost,dp[prev][256]+changecost);

					dp[curr][j] = mincost;
					if (i==n-1) ans = min(ans,dp[curr][j]);
				}
				
			}

			if (i==0) dp[0][256] = D;
			else dp[curr][256] = dp[prev][256]+D;

			if (i==n-1) ans = min(ans,dp[curr][256]);
		}
			
		if (n==1) ans = 0;

		printf("Case #%d: %d\n",tt,ans);
	}

	return 0;
}
