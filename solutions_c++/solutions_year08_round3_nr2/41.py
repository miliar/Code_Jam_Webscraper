#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

#ifndef ONLINE_JUDGE
#include<fstream>
  ifstream in("B-large.in.txt");
  ofstream out("b.out");
#define cin in
#define cout out
#endif


const int mod = 2 * 3 * 5 * 7;
long long dp[64][mod];
int ys[64][64];
string s;

int getYS(int start, int end)
{
	int ret = 0;
	for(int i = start; i <= end; i++)
	{
		ret = ret * 10 + s[i] - '0';
		ret %= mod;
	}
	return ret;
}

int main()
{
	int cs;
	cin>>cs;
	for(int ct = 1; ct <= cs; ct ++)
	{
		cout << "Case #"<<ct<<": ";

		memset(dp, 0, sizeof(dp));
		memset(ys, 0, sizeof(ys));

		cin >> s;
		int n = s.size();

		for(int i = 0; i <= n - 1; i ++)
			for(int j = i; j <= n -1; j++)
			{
				ys[i][j] = getYS(i,j);			
			}
		
		dp[0][ys[0][0]] = 1;
		for(int i = 1; i <= n -1; i++)
		{
			dp[i][ys[0][i]] = 1;
			for(int j = 0; j < i; j++)
			{
				int cur = ys[j+1][i];
				for(int k = 0; k < mod; k ++)
				{
					// add
					int index = (k + cur) % mod;
					dp[i][index] += dp[j][k];

					//sub
					index = k - cur;
					if(index < 0)
						index += mod;
					dp[i][index] += dp[j][k];
				}

				
			}
		}
		long long ans = 0;
		for(int i = 0; i < mod; i ++)
		{
			if(i % 2 == 0 || i % 3 == 0 || i % 5 == 0 || i % 7 == 0)
				ans += dp[n-1][i];
		}
		cout << ans << endl;
	}
}
