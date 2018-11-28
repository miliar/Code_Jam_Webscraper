#include <set>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
#define s(c) ((int)((c).size()))
#define f(i, lo, hi) for (int i = (lo), Max = (hi); i <= Max; ++i)
#define c(i, c) f(i, 0, s(c) - 1)

typedef vector<string> vstr;
typedef set<char> schar;
typedef vector<schar> vschar;

int L, d, n;
vstr dict;
vschar pat;

void init(string s) {
	c(i, pat) pat[i].clear();
	int id = 0;
	c(i, pat) {
		if (s[id] == '(') {
			while (s[id + 1] != ')') {
				pat[i].insert(s[id + 1]);
				++id;
			}
			id += 2;
		} else {
			pat[i].insert(s[id]);
			++id;
		}
	}
}

bool eq(string s) {
	c(i, s) if (!pat[i].count(s[i])) return 0;
	return 1;
}

void solve() {
	cin >> L >> d >> n;
	dict.resize(d);
	pat.resize(L);
	c(i, dict) cin >> dict[i];
	string p;
	f(i, 1, n) {
		cin >> p;
		init(p);
		int ans = 0;
		c(j, dict) if (eq(dict[j])) ++ans;
		cout << "Case #" << i << ": " << ans << endl;
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	solve();
	return 0;
}
