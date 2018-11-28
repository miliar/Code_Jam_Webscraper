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

int n;

string st = "welcome to code jam";
int d[1050][25];

int solve(string s) {
	memset(d, 0, sizeof(d));
	forn(i, s.size()) {
		if (s[i] == 'w') {
			d[i][1] = 1;
		}
	}

	forn(i, s.size()) {
		forn(j, st.size()) {
			for (int k = i + 1;k < (int)s.size();k++) {
				if (s[k] == st[j]) {
					d[k][j + 1] += d[i][j];
					d[k][j + 1] %= 10000;
				}
			}
		}
	}

	int ans = 0;

	forn(i, s.size()) {
		ans += d[i][st.size()];
		ans %= 10000;
	}

	return ans;
}

char buff[10000];

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int t;
	cin >> t;
	gets(buff);
	forn(i, t) {
		string s;
		gets(buff);
		s = string(buff);
		printf("Case #%d: %.4d\n", i + 1, solve(s));
	}
	
    return 0;
}
