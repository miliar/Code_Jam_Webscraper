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

int N, K;
int G[20][20];
int C[20][30];

int dp[1 << 17];
int Rec(int x)
{
	if(dp[x])
		return dp[x];
	bool ok = true;
	for(int i = 0; ok && i < N; ++i)
		if(x & (1 << i))
			for(int j = i + 1; ok && j < N; ++j)
				if(x & (1 << j))
					if(G[i][j] == 0)
						ok = false;
	if(ok)
		return dp[x] = 1;
	dp[x] = N;
	for(int y = x; y; y = (y - 1) & x)
	{
		int z = x ^ y;
		if(y && z)
			dp[x] = min(dp[x], Rec(y) + Rec(z));
	}
	return dp[x];
}

bool Solve(int test)
{
	scanf("%d %d", &N, &K);
	for(int i = 0; i < N; ++i)
		for(int j = 0; j < N; ++j)
			G[i][j] = i == j ? 0 : 1;
	for(int i = 0; i < N; ++i)
		for(int j = 0; j < K; ++j)
			scanf("%d", &C[i][j]);
	for(int i = 0; i < N; ++i)
		for(int j = i + 1; j < N; ++j)
		{
			for(int k = 1; G[i][j] && k < K; ++k)
			{
				if(C[i][k] == C[j][k] || C[i][k - 1] == C[j][k - 1])
					G[i][j] = G[j][i] = 0;
				if(C[i][k] > C[j][k] && C[i][k - 1] < C[j][k - 1])
					G[i][j] = G[j][i] = 0;
				if(C[i][k] < C[j][k] && C[i][k - 1] > C[j][k - 1])
					G[i][j] = G[j][i] = 0;
			}
		}
	for(int i = 0; i < 1 << N; ++i)
		dp[i] = 0;
	printf("Case #%d: %d\n", test, Rec((1 << N) - 1));
	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t = 0;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	//*/while(Solve(++t));
	return 0;
}