#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#pragma comment (linker, "/STACK:99000111")

#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <ctime>
#include <cassert>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <map>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = (int)a; i < (int)b; ++i)
#define ford(i, n) for(int i = (int)(n - 1); i >= 0; --i)
#define forv(i, v) for(int i = 0; i < (int)(v.size()); ++i)
#define fs first 
#define sc second
#define mp make_pair
#define pb push_back
#define last(a) a[a.size() - 1]
#define all(a) a.begin(), a.end()
#define norm(a) sort(all(a));a.erase(unique(all(a)), a.end())
#define sz(a) a.size()
#define vi vector<int>
#define pii pair<int,int>

#define INF 1000 * 1000 * 1000
#define EPS 1e-9
#define MAXN 1001

using namespace std;

string t = "welcome to code jam";
string s;

int d[600][22];
char buf[1333];

int mod = 10000;

int get(int i, int j) {
	if (j == (int)t.length())
		return 1;
	if (i == (int)s.length())
		return 0;
	if (d[i][j] != -1)
		return d[i][j];
	d[i][j] = get(i + 1, j);
	if (s[i] == t[j])
		d[i][j] = (d[i][j] + get(i + 1, j + 1)) % mod;
	return d[i][j];
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin >> t;
	gets(buf);
	forn(tt, t) {
		gets(buf);
		s = buf;
		memset(d, -1, sizeof(d));
		printf("Case #%d: %04d\n", tt + 1, (int)get(0, 0));
	}

	return 0;
}

