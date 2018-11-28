#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
typedef pair<int, int> ii;

int dp[505][20];
string s = "welcome to code jam";
string text;
int solve(int id, int let)
{
	if (id >= text.length()) return 0;
	if (let == 18) return text[id] == s[let];
	if (dp[id][let] != -1) return dp[id][let];
	if (text[id] != s[let]) return dp[id][let] = 0;
	dp[id][let] = 0;
	for (int i = id+1; i < text.length(); ++i)
		dp[id][let] += solve(i, let+1), dp[id][let] %= 10000;
	return dp[id][let];
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int n;
	cin >> n;
	char tt[505];
	cin.getline(tt, 505);
	for (int t = 0; t < n; ++t)
	{
		memset(dp, -1, sizeof(dp));
		cin.getline(tt, 505);
		text = tt;
		int ans = 0;
		for (int i = 0; i < text.length(); ++i)
			ans += solve(i, 0), ans %= 10000;
		cout << "Case #" << t+1 << ": " 
			<< ans/1000 << (ans/100)%10 << (ans/10)%10 << ans%10 << endl;
		cerr << t+1 << endl;
		
	}
}