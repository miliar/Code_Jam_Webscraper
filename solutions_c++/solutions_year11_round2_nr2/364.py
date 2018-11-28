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

int n, d;
int pos[205], cnt[205];

bool good(lint t) {
	lint p = -1000000000000000L;
	f(i, 1, n) {
		f(j, 1, cnt[i]) {
			lint des = p + d * 2;
			lint now = pos[i] * 2;
			lint dist = abs(des - now);
			if (now < des) {
				if (dist > t)
					return false;
				p = des;
			} else {
				p = max(des, now - t);
			}
		}
	}
	return true;
}

void solve(int T) {
	printf("Case #%d: ", T);
	scanf("%d%d", &n, &d);
	f(i, 1, n)
		scanf("%d%d", pos + i, cnt + i);
	lint lo = -1, hi = 10000000000000L;
	while (hi - lo > 1) {
		lint me = (hi + lo) >> 1;
		if (good(me))
			hi = me;
		else
			lo = me;
	}
	printf("%.1lf\n", (double)hi * 0.5);
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
