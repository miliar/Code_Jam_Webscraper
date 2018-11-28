#include <iostream>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iterator>
#include <utility>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <queue>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forv(i, v) for(int i = 0; i < (int)v.size(); ++i)
#define fors(i, s) for(int i = 0; i < (int)s.length(); ++i)
#define all(c) c.begin(), c.end()
#define pb push_back
#define abs(a) ((a) >= 0 ? (a) : -(a))
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long ll;

int calcAns(string s) {
	int ans = 0;
	forn(i, s.length()) {
		int j = i;
		++ans;
		while (j < s.length() && s[i] == s[j]) ++j;
		i = j - 1;
	}
	return ans;
}

int p[10];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	scanf("%d\n", &tk);
	for(int tc = 1; tc <= tk; ++tc) {
		int k;
		string s;
		cin >> k >> s;

		forn(i, k)
			p[i] = i;
		int res = INT_MAX >> 1;
		do {
			int l = 0;
			string c = s;
			while (l < s.length()) {
				forn(j, k)
					c[j + l] = s[l + p[j]];
				l += k;
			}
			res = min(res, calcAns(c));
		} while (next_permutation(p, p + k));

		printf("Case #%d: %d\n", tc, res);
	}

	return 0;
}