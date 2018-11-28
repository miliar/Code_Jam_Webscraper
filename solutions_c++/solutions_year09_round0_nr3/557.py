#include<iostream>
#include<string>
using namespace std;

int dp[510][20];

char s[510];
char mp[20]="welcome to code jam";

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,i,j,k,cas=1,len,sum;
	scanf("%d",&t);
	gets(s);
	while(t--)
	{
		printf("Case #%d: ",cas);
		cas++;
		gets(s);
		len=strlen(s);
		memset(dp,0,sizeof(dp));
		for(i=0;i<len;i++)
		{
			for(j=0;j<19;j++)
			{
				if(s[i]==mp[j])
				{
					sum=0;
					if(j>0)
					{
						for(k=0;k<i;k++)
							sum+=dp[k][j-1];
						dp[i][j]=sum%10000;
					}
					else
					{
						dp[i][j]=1;
					}
				}
			}
		}
		sum=0;
		for(i=0;i<len;i++)
			sum+=dp[i][18];
		printf("%04d\n",sum%10000);
	}
	return 0;
}

