
#include <iostream>
#include <cstdio>
#include <string>
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <cstring>
using namespace std;
const int INFI = 1000000000;


int T;
ifstream in("A-small.in");
ofstream out("A-small.out");
#define cout out
#define cin in

int n;

const int MOD = 100003;

long long ans;

long long c[550][550];

long long dp[550][550];


int main()
{
	memset(c,0,sizeof(c));
	c[0][0] = 1;
	for(int i = 1;i <= 501;i ++)
	{
		c[i][0] = 1;
		for(int j = 1;j <= i;j ++)
		{
			c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD;
		}
	}


	cin >> T;
	for(int cnt = 1;cnt <= T;cnt ++)
	{
		cout << "Case #"<<cnt<<": "; 
		cin >> n;

		memset(dp,0,sizeof(dp));

		for(int i = 1;i <= n;i ++)
			dp[i][1] = 1;

		for(int i = 3;i <= n;i ++)
		{
			for(int j = 2;j < i;j ++)
			{
				for(int k = 1;k < j;k ++)
				{
					if(j + (j - k) <= i)
					{
					  dp[i][j] += dp[j][k] * c[i - j - 1][j - k - 1];
					  dp[i][j] %= MOD;
					}
				}
			}
		}

	    long long ans = 0;
		for(int i = 1;i <= n - 1;i ++)
		{
			ans += dp[n][i];
			ans %= MOD;
		}
		cout << ans << endl;









	}

	return 0;
}
