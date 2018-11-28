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
#define INF 1000000

int t;

void init() {
	freopen("input.txt", "rt", stdin);
	scanf("%d\n", &t);
}

void find() {
	string s;
	getline(cin, s);
	int l = s.length() - 1;
	vector< int > num(10);
	do {
		num[s[l]-'0']++;
		l--;
	} while ((l >= 0) && (s[l] >= s[l+1]));
	if (l < 0) l++;
	else num[s[l]-'0']++;
	REP(i, l) cout << s[i];

	int ind = s.length() - 1;
	while ((ind > l) && (s[ind] <= s[l])) ind--;

	if (ind == l) {
		num[0]++;
		FOR(i, 1, 10) {
			if (num[i] != 0) {
				cout << i;
				num[i]--;
				break;
			}
		}
	} else {
		cout << s[ind];
		num[s[ind]-'0']--;
	}
	REP(i, 10) REP(j, num[i]) cout << i;
	cout << endl;
}

void solve() {
	freopen("output.txt", "wt", stdout);
	REP(i, t) {
		printf("Case #%d: ", i+1);
		find();
	}
}

int main() {
	init();
	solve();
}