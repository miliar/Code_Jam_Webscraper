#include <iostream>
#include <string>
using namespace std;
const string wcj="welcome to code jam";
int main()
{
	int dp[500][19];
	int i,j,k,rp,n,ri;
	string s;
	cin>>n;
	getline(cin,s);
	for (ri=0;ri<n;ri++)
	{
		memset(dp,0,sizeof(dp));
		getline(cin,s); k=s.length();
		if (s[0]=='w') dp[0][0]=1; else dp[0][0]=0;
		for (i=1;i<k;i++)
		{
			dp[i][0]=dp[i-1][0];
			if (s[i]=='w') dp[i][0]++;
			for (j=1;j<19;j++)
			{
				dp[i][j]=dp[i-1][j];
				if (s[i]==wcj[j]) dp[i][j]+=dp[i-1][j-1];
				if (dp[i][j]>10000) dp[i][j]%=10000;
			}
		}
		dp[k-1][18]%=10000;
		cout<<"Case #"<<ri+1<<": ";
		if (dp[k-1][18]<1000) cout<<0;
		if (dp[k-1][18]<100) cout<<0;
		if (dp[k-1][18]<10) cout<<0;
		cout<<dp[k-1][18]<<endl;
	}
	return 0;
}