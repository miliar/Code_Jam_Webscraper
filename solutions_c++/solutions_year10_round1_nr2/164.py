#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;
template <class A, class B> void CONV(A &x, B &y) { stringstream s; s << x; s >> y; }
int CMP(double a, double b) { return a < b-1e-7 ? -1 : a > b+1e-7 ? 1 : 0; }
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORE(i, v) FOR(i, 0, v.size())
#define SORT(v) sort(v.begin(), v.end())
#define SET(a, n) memset(a, n, sizeof a)

int del, ins, m, n, v[100], dp[100][257];

int go(int pos, int last) {
	if (pos == n) return 0;
	if (dp[pos][last] != -1) return dp[pos][last];
	int res = del+go(pos+1, last); // del
	if (last == 256 || abs(v[pos]-last) <= m) res = min(res, go(pos+1, v[pos])); // skip
	if (m != 0 && last != 256 && abs(v[pos]-last) > m) { // ins
		if (last < v[pos]) res = min(res, ins+go(pos, last+m));
		else res = min(res, ins+go(pos, last-m));
	}
	if (last == 256) { // change
		FOR(i, 0, 256) res = min(res, abs(i-v[pos])+go(pos+1, i));
	}
	else {
		for (int i = max(0, last-m); i <= min(255, last+m); ++i) res = min(res, abs(i-v[pos])+go(pos+1, i));
	}
	return dp[pos][last] = res;
}

int main() {
	int t;
	cin >> t;
	FOR(i, 0, t) {
		cin >> del >> ins >> m >> n;
		FOR(j, 0, n) cin >> v[j];
		SET(dp, -1);
		cout << "Case #" << i+1 << ": " << go(0, 256) << endl;
	}
}
