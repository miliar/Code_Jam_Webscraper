#include <iostream>
#include <string>
using namespace std;
string text="welcome to code jam";
int main()
{
	int N,i,j,k;
	int dp[25][600];
	string s;
	cin >> N;
	cin.ignore();
	for (i=1; i<=N; i++)
	{
		getline(cin,s);
		for (j=0; j<s.length(); j++)
			if (s[j]=='w') dp[0][j]=1; else dp[0][j]=0;
		for (j=1; j<text.length(); j++)
		{
			int sum=0;
			dp[j][0]=0;
			for (k=1; k<s.length(); k++)
			{
				sum+=dp[j-1][k-1];
				sum%=10000;
				if (s[k]==text[j])
					dp[j][k]=sum;
				else
					dp[j][k]=0;
			}
		}
		int res=0;
		for (j=0; j<s.length(); j++)
			res=(res+dp[text.length()-1][j])%10000;
		printf("Case #%d: %04d\n",i,res);
	}
	return 0;
}