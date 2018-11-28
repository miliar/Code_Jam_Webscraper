#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>

#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <list>

#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) a.size() - 1
#define all(a) a.begin(), a.end()
#define I (int)
#define I64 (long long)
#define LD (long double)
#define VI vector<int>
#define pti pair<int, int>
#define ptd pair<long double, long double>
#define sqr(x) ((x) * (x))

const long double EPS = 1E-9;
const int INF = (int)1E9;
const long long INF64 = (long long)1E18;
const long double PI = 2 * acos(.0);

typedef long double ld;
typedef long long ll;

int l, d, n;

vector<string> v;
string dict[5050];
char buff[10000];

inline vector<string> parse(string s) {
	vector<string> ans;

	int idx = 0;
	while (idx < (int)s.size()) {
		if (s[idx] == '(') {
			idx++;
			string tmp;

			while (s[idx] != ')') {
				tmp += s[idx];
				idx++;
			}

			sort(all(tmp));
			ans.pb(tmp);
		} else {
			ans.pb(string("") + s[idx]);
		}
		idx++;
	}

	return ans;
}

inline bool match(const string& s, const vector<string>& v) {
	forn(i, l)
		if (!binary_search(all(v[i]), s[i]))return false;
	return true;
}

inline int countWords(vector<string>& v) {
	int ans = 0;
	forn(i, d) {
		if (match(dict[i], v))
			ans++;
	}

	return ans;
}

void solve() {
	scanf("%d%d%d", &l, &d, &n);
	gets(buff);
	forn(i, d) {
		gets(buff);
		dict[i] = string(buff);
	}

	forn(i, n) {
		gets(buff);
		string cur = string(buff);
		v = parse(cur);
		printf("Case #%d: %d\n", i + 1, countWords(v));
	}

}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	solve();
    return 0;
}
