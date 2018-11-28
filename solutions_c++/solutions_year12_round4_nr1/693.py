#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<algorithm>
#include<sstream>
#include<ctime>
#include<cmath>
#include<set>
#include<queue>
#include<map>
#include<cstdio>
#include<map>
using namespace std;
typedef unsigned long long u64;
typedef long long i64;
typedef unsigned long long u32;
typedef long long i32;
const double EPS = 1e-9;
const double PI = 3.1415926535897932384626433832795;
i64 i64INF = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;
i32 i32INF = 1000 * 1000 * 1000;
const u64 H = 127;
double INF = 1e10;
double mINF = INF + 100.0;
vector<pair<int, int> > v;
int d;
int dp[10100][10100];

bool go(int i, int j) // in hold
{
	if(dp[i][j] == -1)
	{
		int mx = v[j].first + min(v[j].first-v[i].first, v[j].second);
		if(mx >= d) return true;
		for(int ii = j+1; ii < v.size() && v[ii].first <= mx ; ii++)
			if(go(j, ii))
			{
				dp[i][j] = 1;
				return 1;
			}
		dp[i][j] = 0;
	}

	return dp[i][j];
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int t;
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		memset(dp, -1, sizeof dp);
		int n;
		cin >> n;
		v.resize(n+1);
		v[0] = make_pair(0, 0);
		for(int i = 1; i <= n; i++)
			cin >> v[i].first >> v[i].second;
		cin >> d;
		if(go(0, 1))
			cout << "Case #" << test << ": " << "YES" << endl;
		else
			cout << "Case #" << test << ": " << "NO"  << endl;
	}

	return 0;
}