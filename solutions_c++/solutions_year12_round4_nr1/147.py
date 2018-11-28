#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#pragma comment (linker, "/STACK:200000000")
#include <algorithm>
#include <bitset>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <stack>
#include <sstream>
#include <vector>

using namespace std;

typedef long long int64;
//typedef double old_double;
//#define double long double
const int INF = (int) 1E9;
const int64 INF64 = (int64) 1E18;
const double EPS = 1E-9;
const double PI = acos((double)0) * 2;

#define forn(i,n)  for (int i=0; i<int(n); ++i)
#define ford(i,n)  for (int i=int(n)-1; i>=0; --i)
#define fore(i,l,n)  for (int i=int(l); i<int(n); ++i)
#define all(a)  a.begin(), a.end()
#define fs  first
#define sc  second
#define pb  push_back
#define mp  make_pair


const int MAXN = 110000;


int n, x[MAXN], X, len[MAXN];


void read() {
	cin >> n;
	forn(i,n)
		scanf ("%d%d", &x[i], &len[i]);
	cin >> X;
}


int d[MAXN];


void solve() {
	forn(i,n)
		d[i] = i==0 ? x[0] : 0;

	bool ans = false;
	forn(i,n) {
		int mx = x[i] + d[i];
		if (mx >= X)
			ans = true;
		for (int j=i+1; j<n; ++j)
			if (x[j] <= mx) {
				int cur = min (x[j] - x[i], len[j]);
				d[j] = max (d[j], cur);
			}
	}
	puts (ans ? "YES" : "NO");
}


int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	forn(tt,ts) {
		read();
		if (! cin)  throw;
		printf ("Case #%d: ", tt+1);
		solve();
	}
}