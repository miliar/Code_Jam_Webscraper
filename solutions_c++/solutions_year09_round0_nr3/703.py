#include <cstdio>
#include <algorithm>
#include <vector>
#include <cassert>
#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <iostream>
using namespace std;
#define sz(a) (int)((a).size())
#define pb push_back
#define mp make_pair
#define all(a) (a).begin(), (a).end()
typedef pair<int, int> pii;
typedef vector<int> vint;
typedef long long lint;

char Pat[] = "welcome to code jam";
char S[555];

int dp[501][20];

bool Solve(int test)
{
	int n = 0;
	while(Pat[n])
		n++;
	gets(S);
	for(int i = 0; i <= 500; ++i)
		for(int j = 0; j < 20; ++j)
			dp[i][j] = 0;
	for(int i = 0; S[i]; ++i)
		if(S[i] == 'w')
			dp[i][0] = 1;
	for(int k = 1; Pat[k]; ++k)
	{
		for(int i = 1; S[i]; ++i)
			if(S[i] == Pat[k])
				for(int j = 0; j < i; ++j)
					if(S[j] == Pat[k - 1])
					{
						dp[i][k] += dp[j][k - 1];
						dp[i][k] %= 10000;
					}
	}
	int ans = 0;
	for(int i = 0; S[i]; ++i)
		ans = (ans + dp[i][n - 1]) % 10000;
	printf("Case #%d: %04d\n", test, ans);
	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t = 0;
	scanf("%d", &t);
	gets(S);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	//*/while(Solve(++t));
	return 0;
}