#pragma comment (linker, "/STACK:200000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
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


const int MAXN = 110;


int n;
char a[MAXN][MAXN];


void read() {
	cin >> n;
	forn(i,n)
		forn(j,n)
			scanf (" %c", &a[i][j]);
}


double wp[MAXN], owp[MAXN], oowp[MAXN];


double get_wp (int v) {
	int g=0, w=0;
	forn(i,n)
		if (a[v][i] != '.') {
			++g;
			if (a[v][i] == '1')  ++w;
		}
	return w * 1.0 / g;
}

double get_owp (int v) {
	double res = 0;
	int cnt = 0;
	forn(i,n)
		if (a[v][i] != '.') {
			double wp = 0;
			int w=0, g=0;
			forn(j,n)
				if (a[i][j] != '.' && j != v) {
					++g;
					if (a[i][j] == '1')  ++w;
				}
			wp = w * 1.0 / g;

			res += wp;
			++cnt;
		}
	return res / cnt;
}

double get_oowp (int v) {
	double res = 0;
	int cnt = 0;
	forn(i,n)
		if (a[v][i] != '.') {
			res += owp[i];
			++cnt;
		}
	return res / cnt;
}


void solve() {
	forn(i,n) {
		wp[i] = get_wp (i);
		owp[i] = get_owp (i);
	}
	forn(i,n)
		oowp[i] = get_oowp (i);

	forn(i,n) {
		double ans = wp[i]/4 + owp[i]/2 + oowp[i]/4;
		printf ("%.20lf\n", ans);
	}
}


int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	forn(test,ts) {
		read();
		printf ("Case #%d:\n", test+1);
		solve();
	}

}