#include <iostream>
using namespace std;
string s = "welcome to code jam";
char text[505];
int dp[20][505];
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int N;
	scanf("%d", &N);
	gets(text);
	int Case;
	for(Case = 1; Case <= N; Case++)
	{
		gets(text);
		int len = strlen(text);
		int i, j;
		memset(dp, 0, sizeof(dp));
		int ans = 0;
		dp[0][0] = 1;
		for(i = 0; i < len; i++)
		{
			dp[0][i+1] = 1;
			for(j = 0; j < s.length(); j++)
			{
				if(text[i] == s[j])
					dp[j+1][i+1] = (dp[j+1][i+1] + dp[j][i]) % 10000;
				dp[j+1][i+1] = (dp[j+1][i+1] + dp[j+1][i]) % 10000;
				//cout<<dp[j+1][i+1]<<" ";
			}
			//cout<<endl;
			//ans = (ans + dp[s.length()][i+1])  % 10000;
		}
		printf("Case #%d: %04d\n", Case, dp[s.length()][len]);
	}
}