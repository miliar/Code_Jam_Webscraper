#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

#ifndef ONLINE_JUDGE
#include<fstream>
  ifstream in("C-small-attempt0.in.txt");
  ofstream out("c.out");
#define cin in
#define cout out
#endif


int a[128];
int speed[500001];
int mod = 1000000007;
int dp[500001];

int main()
{
	int cs;
	cin>>cs;
	for(int ct = 1; ct <= cs; ct ++)
	{
		cout << "Case #"<<ct<<": ";

		int n,m;
		long long x,y,z;
		cin>>n>>m>>x>>y>>z;
		for(int i = 0; i < m; i++)
			cin >> a[i];

		for(int i = 0; i < n; i ++)
		{
			speed[i] = a[i % m];
			//cout << speed[i] <<' ' ;
			a[i % m] = (x * a[i % m] + y * (i + 1)) % z;
		}

		for(int i = 0; i < n; i++)
			dp[i] = 1;
		for(int i = n - 2; i >= 0; i --)
		{
			for(int j = i + 1; j < n; j ++)
				if(speed[j] > speed[i])
					dp[i] = (dp[i] + dp[j]) % mod;
		}
		int ans = 0;
		for(int i = 0; i < n;  i++)
			ans = (ans + dp[i]) % mod;
		cout << ans <<endl;

	}
}
