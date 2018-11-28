#include<iostream>
using namespace std;
const int N=600;
char a[N],b[30]="welcome to code jam";
int dp[30][N],len;
int main()
{
	int t,tt=0;scanf("%d",&t);
	len=strlen(b);
	while(t--)
	{
		tt++;
		int i,j,k,l;
		if(tt==1)getchar();
		gets(a);
		k=strlen(a);
		memset(dp,0,sizeof(dp));
		for(i=0;i<k;i++)
		{
			if(b[0]==a[i])
			{
				dp[0][i]=1;
			}
		}
		for(i=1;i<len;i++)
		{
			int cnt=0;
			for(j=0;j<k;j++)
			{
				if(a[j]==b[i-1])
				{
					cnt+=dp[i-1][j];
					cnt%=10000;
				}
				else if(a[j]==b[i])
				{
					dp[i][j]=cnt;
				}
			}
		}
		int ans=0;
		for(i=0;i<k;i++)
		{
			ans+=dp[len-1][i];
			ans%=10000;
		}
		printf("Case #%d: %04d\n",tt,ans);
	}
	return 0;
}