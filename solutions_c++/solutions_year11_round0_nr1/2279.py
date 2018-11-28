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

int n, bp, op, bt, ot;
char ord[4];
int num;

void solve(int T) {
	scanf("%d", &n);
	bp = 1; op = 1; bt = 0; ot = 0;
	int t = 0;
	f(i, 1, n) {
		scanf("%s%d", ord, &num);
		if (ord[0] == 'B') {
			int dist = abs(bp - num);
			int moo = t - bt;
			if (dist > moo)
				t += dist - moo;
			++t;
			bt = t;
			bp = num;
		} else {
			int dist = abs(op - num);
			int moo = t - ot;
			if (dist > moo)
				t += dist - moo;
			++t;
			ot = t;
			op = num;
		}
	}
	printf("Case #%d: %d\n", T, t);	
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
