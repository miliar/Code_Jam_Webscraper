#include<iostream>
#include<string>
using namespace std;
int main()
{
	int dp[30];
	int t;
	freopen("G:\\C-large.in","r",stdin);
	freopen("G:\\C-large.out","w",stdout);

	while(scanf("%d",&t)!=EOF)
	{
		getchar();	
		for(int cas=1;cas<=t;++cas)
		{
			string s;
			getline(cin,s);
			memset(dp,0,sizeof(dp));
			for(int i=0;i<s.size();++i)
			{
				if(s[i]=='w')
					dp[1]=(dp[1]+1)%10000;
				if(s[i]=='e')
					dp[2]=(dp[1]+dp[2])%10000;
				if(s[i]=='l')
					dp[3]=(dp[2]+dp[3])%10000;
				if(s[i]=='c')
					dp[4]=(dp[3]+dp[4])%10000;
				if(s[i]=='o')
					dp[5]=(dp[4]+dp[5])%10000;
				if(s[i]=='m')
					dp[6]=(dp[5]+dp[6])%10000; 
				if(s[i]=='e')
					dp[7]=(dp[6]+dp[7])%10000;
				if(s[i]==32)
					dp[8]=(dp[7]+dp[8])%10000;
				if(s[i]=='t')
					dp[9]=(dp[8]+dp[9])%10000;
				if(s[i]=='o')
					dp[10]=(dp[9]+dp[10])%10000;
				if(s[i]==32)
					dp[11]=(dp[10]+dp[11])%10000;
				if(s[i]=='c')
					dp[12]=(dp[11]+dp[12])%10000;
				if(s[i]=='o')
					dp[13]=(dp[12]+dp[13])%10000;
				if(s[i]=='d')
					dp[14]=(dp[13]+dp[14])%10000;
				if(s[i]=='e')
					dp[15]=(dp[14]+dp[15])%10000;
				if(s[i]==32)
					dp[16]=(dp[15]+dp[16])%10000;
				if(s[i]=='j')
					dp[17]=(dp[16]+dp[17])%10000;
				if(s[i]=='a')
					dp[18]=(dp[17]+dp[18])%10000;
				if(s[i]=='m')
					dp[19]=(dp[18]+dp[19])%10000;
			}
			string ans="0000";
			ans[3]=dp[19]%10+'0';
			ans[2]=(dp[19]/10)%10+'0';
			ans[1]=(dp[19]/100)%10+'0';
			ans[0]=(dp[19]/1000)%10+'0';
			printf("Case #%d: ",cas);
			cout<<ans<<endl;
		}

	}
	return 0;
}