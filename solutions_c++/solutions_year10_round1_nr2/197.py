#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

#define REP(i, n) for(int i = 0; i<(n); i++)
#define abs(a) ((a) >= 0 ? (a) : -(a))
#define inf 2000000001
typedef vector<int> VI;
typedef vector<string> VS;

typedef long long i64;
typedef unsigned long long u64;

int D, I, M, N;
VI v;

int dp[300][110];

int doit(int l, int pos) {
	if (pos == N) return 0;
	if (dp[l][pos] != -1) return dp[l][pos];
	int ret = doit(l, pos + 1) + D;
	if (l == 256) {
		// only change
		for (int k = 0; k <= 255; k++) {
			ret = min(ret, doit(k, pos + 1) + abs(k - v[pos]));
		}
	} else {
		// change
		for (int k = max(0, l - M); k <= min(255, l + M); k++) {
			ret = min(ret, doit(k, pos + 1) + abs(k - v[pos]));
		}
		// insert
		if (M > 0 && abs(l - v[pos]) > M) {
			if (l < v[pos]) {
				ret = min(ret, doit(l + M, pos) + I);
			} else {
				ret = min(ret, doit(l - M, pos) + I);
			}
		}
	}
	return dp[l][pos] = ret;
}

void go(int t) {
	cin>>D>>I>>M>>N;
	v = VI(N);
	REP(i, N) {
		cin>>v[i];
	}
	memset(dp, 0xff, sizeof(dp));
	cout << "Case #" << t << ": " << doit(256, 0) << endl;
}

int main() {
	int t;
	cin>>t;
	for (int _t = 1; _t <= t; _t++) {
		go(_t);
	}
	return 0;
}
