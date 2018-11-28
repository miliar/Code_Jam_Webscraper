#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>
#include <complex>

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) (int(a.size()) - 1)
#define all(a) a.begin(), a.end()

const double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const double PI = 3.1415926535897932384626433832795;

map<int, int> ma;

void add(string s1, string s2) {
	ma[s1[0] - 'a'] = 26 + s2[0] - '0';
}

string s;
char buf[110000];
int k, in[110], out[110];
set<pair<int, int> > g;

void read() {
	cin >> k;
	scanf("%s", buf);
	s = buf;
}

void add(int v1, int v2) {
	if (!g.count(mp(v1, v2))) {
		out[v1]++;
		in[v2]++;
		g.insert(mp(v1, v2));
	}
}

void solve() {
	g.clear();
	memset(in, 0, sizeof(in));
	memset(out, 0, sizeof(out));
	forn(i, s.size() - 1) {
		int v1 = s[i] - 'a';
		int v2 = s[i + 1] - 'a';

		add(v1, v2);

		if (ma.count(v1)) {
			add(ma[v1], v2);
		}
		if (ma.count(v2)) {
			add(v1, ma[v2]);
		}
		if (ma.count(v2) && ma.count(v1)) {
			add(ma[v1], ma[v2]);
		}
	}

	int d1 = 0, d2 = 0;
	forn(i, 110)
		if (in[i] > out[i])
			d1 += in[i] - out[i];
		else
			d2 += out[i] - in[i];

	int ans = 1 + (int)g.size() + max(0, max(d1, d2) - 1);
	cout << ans << endl;
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

	add("o", "0");
	add("i", "1");
	add("e", "3");
	add("a" , "4");
add( "s" , "5");
add( "t" , "7");
add( "b" , "8");
add( "g" , "9");
	
	int tt;
	cin >> tt;
	forn(ii, tt) {
		cerr << ii << "/" << tt << ' ' << clock() << endl;
		read();
		printf("Case #%d: ", ii + 1);
		solve();
	}

	cerr << tt << "/" << tt << ' ' << clock() << endl;
	
	return 0;
}