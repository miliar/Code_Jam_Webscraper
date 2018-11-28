#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#pragma comment(linker, "/STACK:10000000")
#define For(i,l,h) for (int i = (l); i < (h); ++i)
#define ForU(i,l,h) for (int i = (l); i <= (h); ++i)
#define tr(T, v, it) for (T::iterator it = v.begin(); it != v.end(); ++it) 
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef vector<vs> vvs; 
typedef pair<int,int> pii; 
typedef vector<pii> vpii; 
typedef map<string, int> msi;
typedef long long lint;
const int MAXN = 10000;
const int INF = 1 << 30;
const double eps = 1e-8;
const double pi = acos(-1.0);

int A[MAXN + 10];
int G[MAXN + 10], C[MAXN + 10], I[MAXN + 10];
int N, V;
int dp[MAXN + 10][2];

int rec(int u, int need) {
	if (dp[u][need] != -1) return dp[u][need];
	int l = u * 2;
	int r = u * 2 + 1;
	if (l > N) {
		// leaf
		if (I[u] == need) return dp[u][need] = 0;
		else return INF;		
	}
	int ret = INF;
	// AND
	if (G[u] == 1 || C[u] == 1) {
		int x = 0, t1, t2;
		if (G[u] != 1) x++;
		if (need == 1) {
			t1 = rec(l, 1);
			t2 = rec(r, 1);
			if (t1 != INF && t2 != INF) ret = min(ret, t1 + t2 + x);
		}
		else {
			t1 = rec(l, 0);
			t2 = rec(r, 0);
			if (t1 != INF && t2 != INF) ret = min(ret, t1 + t2 + x);
			t1 = rec(l, 1);
			t2 = rec(r, 0);
			if (t1 != INF && t2 != INF) ret = min(ret, t1 + t2 + x);
			t1 = rec(l, 0);
			t2 = rec(r, 1);
			if (t1 != INF && t2 != INF) ret = min(ret, t1 + t2 + x);
		}
	}
	// OR
	if (G[u] == 0 || C[u] == 1) {
		int x = 0, t1, t2;
		if (G[u] != 0) x++;

		if (need == 1) {
			t1 = rec(l, 1);
			t2 = rec(r, 0);
			if (t1 != INF && t2 != INF) ret = min(ret, t1 + t2 + x);
			t1 = rec(l, 0);
			t2 = rec(r, 1);
			if (t1 != INF && t2 != INF) ret = min(ret, t1 + t2 + x);
			t1 = rec(l, 1);
			t2 = rec(r, 1);
			if (t1 != INF && t2 != INF) ret = min(ret, t1 + t2 + x);
		}
		else {
			t1 = rec(l, 0);
			t2 = rec(r, 0);
			if (t1 != INF && t2 != INF) ret = min(ret, t1 + t2 + x);
		}
	}
	return dp[u][need] = ret;
}

void Solve(int num) {
	scanf("%d %d", &N, &V);
	int hi = (N - 1) / 2;
	for (int i = 1; i <= hi; ++i) {
		scanf("%d %d", &G[i], &C[i]);
	}
	for (int i = hi + 1; i <= N; ++i) {
		scanf("%d", &I[i]);
	}
	for (int i = 0; i <= N; ++i)
		dp[i][0] = dp[i][1] = -1;
	int ans = rec(1, V);
	printf("Case #%d: ", num);
	if (ans == INF) printf("IMPOSSIBLE");
	else printf("%d", ans);
	printf("\n");
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif	
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) Solve(i);
	return 0;
}

