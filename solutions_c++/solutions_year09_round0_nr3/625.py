#include<iostream>
using namespace std;
int main()
{
	int cs,kk,l,i,k,j,ans;
	//freopen("welcome.in","r",stdin);
	//freopen("welcome.out","w",stdout);
	char str[510];
	int dp[510][20];
	char w[]="welcome to code jam";
	scanf("%d",&cs);
	getchar();
	for (kk=1;kk<=cs;kk++)
	{
		gets(str);
		l=strlen(str);
		memset(dp,0,sizeof(dp));
		for (i=0;i<l;i++)
			if (str[i]==w[18]) dp[i][18]=1;
		for (i=l-1;i>=0;i--)
			for (k=0;k<18;k++)
				if (str[i]==w[k])
					for (j=i+1;j<l;j++)
						if (str[j]==w[k+1])
							dp[i][k]=(dp[i][k]+dp[j][k+1])%10000;
		ans=0;
		for (i=0;i<l;i++)
			ans=(ans+dp[i][0])%10000;
		if (ans<10)	printf("Case #%d: 000%d\n",kk,ans);
		else if (ans<100) printf("Case #%d: 00%d\n",kk,ans);
		else if (ans<1000) printf("Case #%d: 0%d\n",kk,ans);
		else printf("Case #%d: %d\n",kk,ans);
	}
	return 0;
}
