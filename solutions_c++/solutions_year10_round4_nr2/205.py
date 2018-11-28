#include<iostream>
using namespace std;
int a[1024];
int b[13][1024];
int dp[13][1024];
const int inf = 0x3f3f3f3f;
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	for(int CaSe = 1 ;CaSe<=zu;CaSe++)
	{
		printf("Case #%d: ",CaSe);

		memset(dp,0x3f,sizeof(dp));
		//cout<<dp[0][0]<<endl;
		int m;
		scanf("%d",&m);
		for(int i=0;i<(1<<m);i++)
		{
			scanf("%d",&a[i]);
			for(int j=0;j<=a[i];j++)
			{
				dp[j][i]=0;
			}
			dp[a[i]+1][i]=inf;
		}
		for(int i=m-1;i>=0;i--)
		{
			for(int j=0;j<(1<<i);j++)
			{
				int z ;
				scanf("%d",&z);
				int aa[14]={0};
				memset(aa,0x3f,sizeof(aa));
				//aa[0]  =  dp[0][j<<1] + dp[0][j<<1|1] + z;
				for(int k=0;k<12;k++)
				{

					for(int p =k;p<=12;p++)for(int q=k;q<=12;q++)
					{
						aa[k]=min(dp[p][j<<1]+dp[q][j<<1|1]+z,aa[k]);
					}

					for(int p =k+1;p<=12;p++)for(int q=k+1;q<=12;q++)
					{
						aa[k]=min(dp[p][j<<1]+dp[q][j<<1|1],aa[k]);
					}
					//aa[k]  =  min( dp[k][j<<1] + dp[k][j<<1|1] + z , dp [k+1][j<<1] + dp [k+1][j<<1|1]);
				}
				for(int k=0;k<13;k++)
					dp[k][j]=min(aa[k],inf);
			}
		}
		int rr=inf;
		for(int i=0;i<13;i++)
			rr=min(rr,dp[i][0]);
		cout<<rr<<endl;
	}
}