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


const int MAXN = 1100;


struct item {
	int fs, sc, id;
};


int n;
item a[MAXN];


void read() {
	cin >> n;
	forn(i,n) {
		cin >> a[i].fs;
		a[i].id = i;
	}
	forn(i,n)
		cin >> a[i].sc;
}


double f (item a, item b) {
	return (a.fs + b.fs - b.fs * a.sc * 0.01) / (1 - a.sc * 0.01 - b.sc * 0.01 + a.sc * b.sc * 0.01 * 0.01);
}


bool operator< (item a, item b) {
	double f1 = f (a, b);
	double f2 = f (b, a);
	return f1 < f2 - EPS;
}


void solve() {
	stable_sort (a, a+n);
	forn(i,n)
		printf (" %d", a[i].id);
	puts("");
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