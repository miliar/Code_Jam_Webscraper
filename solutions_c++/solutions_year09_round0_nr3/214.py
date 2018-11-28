#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <cmath>
#include <stack>
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define mp make_pair
#define foreach(T, x, it) for (T::iterator it = x.begin(); it != x.end(); ++it)
using namespace std;
typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;

string T;
string P = "welcome to code jam";
//string P = "a";
vector<vi> dp;

int rec(int i, int j) {
	if (dp[i][j] != -1) return dp[i][j];
	if (i == sz(T) || j == sz(P)) {
		return dp[i][j] = /*i == sz(T) && */j == sz(P);
	}
	int r = rec(i + 1, j);
	if (T[i] == P[j]) {
		r += rec(i + 1, j + 1);
		r %= 10000;
	}
	return dp[i][j] = r % 10000;
}

int main() {	
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int N;
	scanf("%d\n", &N);
	char buf[1000];

	for (int i = 0; i < N; ++i) {
		gets(buf);
		T = string(buf);
		dp.assign(sz(T) + 1, vi(sz(P) + 1, -1));
		int ans = rec(0, 0);
		assert(ans < 10000);
		printf("Case #%d: %04d\n", i + 1, ans);
	}

	return 0;
}

