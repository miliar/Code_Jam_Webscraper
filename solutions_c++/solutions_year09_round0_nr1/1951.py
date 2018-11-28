#include <math.h>
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <ctype.h>
#include <hash_set>

using namespace std;
using namespace stdext;

#define FOR(i, a, b) for (int _n(b), i(a); i < _n; i++)
#define REP(i, n) FOR(i, 0, n)
#define ALL(a) a.begin(), a.end()
#define SORT(a) sort(ALL(a))
#define pb push_back

int l, d, n;
hash_set< string > pref;

void init() {
	freopen("input_1.txt", "rt", stdin);
	scanf("%d%d%d\n", &l, &d, &n);
	REP(i, d) {
		string line;
		getline(cin, line);
		REP(j, l+1) {
			pref.insert(line.substr(0, j));
		}
	}
}

int find(const string& preffix, const string& suffix) {
	if (pref.find(preffix) == pref.end()) {
		return 0;
	}
	if (suffix == "") {
		return 1;
	}

	if (suffix[0] == '(') {
		int i = 1;
		while (suffix[i] != ')') i++;
		string var = suffix.substr(1, i-1);
		string newsuf = suffix.substr(i+1);
		int k = 0;
		REP(i, var.length()) {
			k += find(preffix+var[i], newsuf);
		}
		return k;
	} else {
		return find(preffix+suffix[0], suffix.substr(1));
	}
}

void solve() {
	freopen("out_1.txt", "wt", stdout);
	REP(t, n) {
		string line;
		getline(cin, line);
		int k = find("", line);
		printf("Case #%d: %d\n", t+1, k);
	}
}

int main() {
	init();
	solve();
}