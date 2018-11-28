#define _CRT_SECURE_NO_WARNINGS
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
using namespace std;
typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;

int A[1000], N;
int D, I, M;
int dp[101][257];

int rec(int k, int prev) {
	if (dp[k][prev] != -1) return dp[k][prev];
	if (k == N) {
		return dp[k][prev] = 0;
	}

	if (prev == 256) {
		int r = rec(k + 1, prev) + D;

		for (int i = 0; i < 256; ++i) {
			int t = rec(k + 1, i) + abs(A[k] - i);
			r = min(r, t);
		}

		return dp[k][prev] = r;

	} else {
		
		int r = rec(k + 1, prev) + D;

		for (int i = 0; i < 256; ++i) {
			int d = abs(prev - i);
			if (!M && d) continue;

			int t = rec(k + 1, i) + abs(A[k] - i);			
			if (d > 0 && M) t += (d - 1) / M * I;
			
			r = min(r, t);
		}
		return dp[k][prev] = r;
	}

}

void solve(int numTst) {
	cin >> D >> I >> M >> N;
	for (int i = 0; i < N; ++i) {
		cin >> A[i];
	}
	memset(dp, -1, sizeof(dp));

	int ans = rec(0, 256);
	printf("Case #%d: %d\n", numTst, ans);


}

int main() {	
//	freopen("input.txt", "r", stdin);
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) {
		solve(i);
	}
	return 0;
}

