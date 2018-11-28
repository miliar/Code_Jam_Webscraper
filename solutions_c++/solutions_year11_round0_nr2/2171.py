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

map<int, char> comb;
set<int> opp;
char str[105];
char ans[105];

void solve(int T) {
	comb.clear();
	opp.clear();
	char b[8];
	int n;
	scanf("%d", &n);
	f(i, 1, n) {
		scanf("%s", b);
		int moo = ((int)b[0] << 8) | (int)b[1];
		comb.insert(mp(moo, b[2]));
		moo = ((int)b[1] << 8) | (int)b[0];
		comb.insert(mp(moo, b[2]));
	}
	scanf("%d", &n);
	f(i, 1, n) {
		scanf("%s", b);
		int moo = ((int)b[0] << 8) | (int)b[1];
		opp.insert(moo);
		moo = ((int)b[1] << 8) | (int)b[0];
		opp.insert(moo);
	}
	scanf("%d%s", &n, str);
	int len = 0;
	f(i, 0, n - 1) {
		ans[len++] = str[i];
		if (len > 1) {
			int moo = ((int)ans[len - 2] << 8) | (int)ans[len - 1];
			if (comb.count(moo)) {
				len -= 2;
				ans[len++] = comb[moo];
			} else {
				int moo = (int)ans[len - 1] << 8;
				f(j, 0, len - 2) {
					moo = (moo & 0xFF00) | (int)ans[j];
					if (opp.count(moo))
						len = 0;
				}
			}
		}
	}
	printf("Case #%d: [", T);
	f(i, 0, len - 1) {
		if (i) printf(", %c", ans[i]);
		else printf("%c", ans[i]);
	}
	printf("]\n");
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
