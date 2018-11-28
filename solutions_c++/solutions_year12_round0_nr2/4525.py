#include <iostream>
using namespace std;

const int MAXn=100+10;
int point[MAXn];
int dp[MAXn][MAXn];
int n, s, p;

int main()
{
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		cin >> n >> s >> p;
		for(int i = 0; i < n; i++)
			cin >> point[i];
		for(int i = 0; i <= s; i++)
			dp[0][i]=-100;
		dp[0][0]=0;
		for(int i = 1; i <= n; i++)
			for(int j = 0; j <= s; j++)
			{
				bool s1=false,s2=false;
				bool S1=false,S2=false;
				for(int k = 0; k <= 10; k++)
					for(int h = k; h <= 10 && h <= k+2; h++)
						for(int g = h; g <= 10 && g <= k+2; g++)
						{
							if(k+h+g==point[i-1])
							{
								if(g>=p)
								{
									if(g-k==2)
										s1=true;
									else
										s2=true;
								}
								else
								{
									if(g-k==2)
										S1=true;
									else
										S2=true;
								}
							}
						}
				dp[i][j]=-100;
				if(s1&&j-1>=0&&dp[i-1][j-1]>=0)
					dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1);
				if(s2&&dp[i-1][j]>=0)
					dp[i][j]=max(dp[i][j],dp[i-1][j]+1);
				if(S1&&j-1>=0&&dp[i-1][j-1]>=0)
					dp[i][j]=max(dp[i][j],dp[i-1][j-1]);
				if(S2)
					dp[i][j]=max(dp[i][j],dp[i-1][j]);
			}
		cout << "Case #" << t << ": " << dp[n][s] << endl;
	}
	return 0;
}
