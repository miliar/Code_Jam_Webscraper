#include <iostream>
#include <string>
using namespace std;

long long dp[20][510];

string s = "welcome to code jam";

int solve(string str)
{
	memset(dp,0,sizeof(dp));
	int L = str.length();
	int a = 1;
	for(int i = 0; i< L; ++i)
	{
		if(str[i] == 'w')
		{
			dp[0][i] = (dp[0][i-1]+1)%10000;
		}
		else dp[0][i] = (dp[0][i-1])%10000;
	}
	for(int i = 1; i< 19; ++i)
	{
		for(int j = 0; j< L; ++j)
		{
			if(str[j] == s[i])
			{
				dp[i][j] = dp[i-1][j-1]%10000;
				for(int k = 0; k< j; ++k)
				{
					if(str[k] == s[i])
					{
						dp[i][j] += (dp[i-1][k-1]%10000);
						dp[i][j] = dp[i][j]%10000;
					}
				}
			}
			else 
			{
				dp[i][j] = dp[i][j-1]%10000;
			}
		}
	}
	return dp[18][L-1]%10000;
}

int main()
{
	int T;
	cin >> T;
	char p[510];
	getchar();
	for(int t = 1; t<= T; ++t)
	{
		gets(p);
		string str = p;
		//cout << str << endl;
		printf("Case #%d: %.4d\n",t,solve(str));
	}
	return 0;
}