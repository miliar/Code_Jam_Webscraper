#include <set>
#include <map>
#include <list>
#include <cmath>
#include <queue>
#include <deque>
#include <vector>
#include <bitset>
#include <string>
#include <memory>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <cassert>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define s(c) ((int)((c).size()))
#define all(c) (c).begin(),(c).end()
#define abs(x) ((x) < 0 ? -(x) : (x))
#define f(i, lo, hi) for (int i = (lo), Max = (hi); i <= Max; ++i)
#define rf(i, hi, lo) for (int i = (hi), Min = (lo); i >= Min; --i)
#define c(i, c) f(i, 0, s(c) - 1)
#define rc(i, c) rf(i, s(c) - 1, 0)
typedef vector<int> vint;
typedef long long lint;

int n;

void solve(int T) {
	scanf("%d", &n);
	int d, mn = 0x7FFFFFFF, sum = 0, moo = 0;
	f(i, 1, n) {
		scanf("%d", &d);
		mn = min(mn, d);
		sum += d;
		moo ^= d;
	}
	if (moo)
		printf("Case #%d: NO\n", T);
	else
		printf("Case #%d: %d\n", T, sum - mn);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	f(i, 1, t) solve(i);
	return 0;
}
