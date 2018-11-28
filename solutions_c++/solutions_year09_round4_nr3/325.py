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

int n, m;
int A[200][200];
int G[200][200];
int dp[1 << 16];
bool Good[1 << 16];

bool Test(int x, int p) { return (x >> p) & 1; }

bool Check(int *a, int *b) {
	for (int i = 0; i + 1 < m; ++i) {
		if (a[i] > b[i] && a[i + 1] > b[i + 1]) continue;
		if (a[i] < b[i] && a[i + 1] < b[i + 1]) continue;
		return false;
	}
	return true;
}

int rec(int use) {
	if (dp[use] != -1) return dp[use];
	if (use == 0) return dp[use] = 0;
	int r = 1 << 30;
	for (int nuse = use; nuse; nuse = (nuse - 1) & use) {
		if (!Good[nuse]) continue;
		int t = rec(nuse ^ use);
		r = min(r, t + 1);
	}
	return dp[use] = r;
}

void Solve(int num) {
	cin >> n >> m;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> A[i][j];
		}
	}
	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j) {
			G[i][j] = G[j][i] = !Check(A[i], A[j]);
		}
	}
	for (int use = 0; use < 1 << n; ++use) {
		Good[use] = true;
		for (int i = 0; Good[use] && i < n; ++i) {
			if (!Test(use, i)) continue;
			for (int j = i + 1; Good[use] && j < n; ++j) {
				if (!Test(use, j)) continue;
				if (G[i][j]) Good[use] = false;
			}
		}
	}
	for (int i = 0; i < 1 << n; ++i)
		dp[i] = -1;
	int ans = rec((1 << n) - 1);
	printf("Case #%d: %d\n", num, ans);
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

