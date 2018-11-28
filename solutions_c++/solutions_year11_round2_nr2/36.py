#pragma comment (linker, "/STACK:200000000")
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
#define double long double
const int INF = (int) 1E9;
const int64 INF64 = (int64) 1E18;
const double EPS = 1E-12;
const double PI = acos((double)0) * 2;

#define forn(i,n)  for (int i=0; i<int(n); ++i)
#define ford(i,n)  for (int i=int(n)-1; i>=0; --i)
#define fore(i,l,n)  for (int i=int(l); i<int(n); ++i)
#define all(a)  a.begin(), a.end()
#define fs  first
#define sc  second
#define pb  push_back
#define mp  make_pair


const int ITER = 200;
const int MAXN = 210;


int n, d, x[MAXN], cnt[MAXN];


void read() {
	cin >> n >> d;
	forn(i,n)
		scanf ("%d%d", &x[i], &cnt[i]);
}


bool can (double t) {
	double prev = -1E20;
	forn(i,n) {
		double first = max (prev+d, x[i] - t);
		if (first > x[i] + t + EPS)  return false;
		double last = first + d * 1ll * (cnt[i] - 1);
		if (last > x[i] + t + EPS)  return false;
		prev = last;
	}
	return true;
}

void solve() {
	double l = 0,  r = 1E13;
	forn(iter,ITER) {
		double mid = (l + r) / 2;
		if (can (mid))
			r = mid;
		else
			l = mid;
	}

	cout.precision (20);
	cout << fixed << l << endl;
}


int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	forn(test,ts) {
		read();
		printf ("Case #%d: ", test+1);
		solve();
	}

}