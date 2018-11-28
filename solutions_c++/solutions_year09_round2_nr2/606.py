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
#define mset(a, v) memset(a, v, sizeof(a))
#define f(i, lo, hi) for (int i = (lo), Max = (hi); i <= Max; ++i)
#define rf(i, hi, lo) for (int i = (hi), Min = (lo); i >= Min; --i)
#define c(i, c) f(i, 0, s(c) - 1)
#define rc(i, c) rf(i, s(c) - 1, 0)
#define it(type, it, c) for (type::iterator it = (c).begin(); it != (c).end(); ++it)
#define rit(type, it, c) for (type::reverse_iterator it = (c).rbegin(); it != (c).rend(); ++it)
typedef vector<int> vint;
typedef long long lint;

char b[32];

void solve(int t) {
	scanf("%s", b);
	string s = b;
	string moo;
	if (!next_permutation(all(s))) {
		char r;
		c(i, s) if (s[i] != '0') {
			r = s[i];
			s[i] = '0';
			break;
		}
		if (s[0] == '0')
			moo.pb(r);
		moo.append(s);
	} else {
		moo = s;
	}
	printf("Case #%d: %s\n", t, moo.c_str());
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	f(i, 1, t)
	solve(i);
	return 0;
}
