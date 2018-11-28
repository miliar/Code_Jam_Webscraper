// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <set>
#include <map>

/////////////////////////
///@author: sakar2003 ///
///@lang: C++         ///
/////////////////////////

using namespace std;

const int MAXN = 100010;

int T;

const string welcome = "welcome to code jam";
string s;
int dp[512][32];
int data[4];

void solve(){
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	for(size_t i = 0; i < s.size(); ++i){
		for(int j = 0; j < welcome.size(); ++j){
			dp[i + 1][j] += dp[i][j];
			dp[i + 1][j] %= 10000;
			if(s[i] == welcome[j]){
				dp[i + 1][j + 1] += dp[i][j];
			}
			dp[i + 1][j + 1] %= 10000;
		}
	}
	int ans = 0;
	for(int i = 0; i < 512; ++i){
		ans += dp[i][welcome.size()];
		ans %= 10000;
	}

	memset(data, 0, sizeof(data));
	int idx = 0;
	while(ans && idx < 4){
		data[idx++] = ans % 10;
		ans /= 10;
	}
	std::reverse(data, data+4);
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("Clarge.txt", "w", stdout);
	scanf("%d", &T);
	getline(cin, s);
	for(int tt = 1; tt <= T; ++tt)
	{
		getline(cin, s);
		solve();
		printf("Case #%d: ", tt);
		for(int i = 0; i < 4; ++i){
			printf("%d", data[i]);
		}
		printf("\n");
	}

	return 0;
}

