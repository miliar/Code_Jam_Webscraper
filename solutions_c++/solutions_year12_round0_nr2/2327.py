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


int n, s, p, t[MAXN];


void read() {
	cin >> n >> s >> p;
	forn(i,n)
		scanf ("%d", &t[i]);
}


int d[MAXN][MAXN];


int get_d (int idx, int s) {
	if (s < 0)  return -INF;
	if (idx == n)  return s==0 ? 0 : -INF;

	int & my = d[idx][s];
	if (my != -1)  return my;
	my = 0;

	int min_l = max (0, (t[idx] - 4) / 3);
	int min_r = t[idx] / 3;
	for (int a=min_l; a<=min_r && a<=10; ++a)
		for (int b=a; b<=a+2 && b<=10; ++b)
			for (int c=b; c<=a+2 && c<=10; ++c)
				if (a+b+c == t[idx])
					my = max (my, get_d (idx+1, s - (c == a+2)) + (c >= p));

	return my;
}


void solve() {
	memset (d, -1, sizeof d);
	cout << get_d (0, s) << endl;
}



int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	forn(tt,ts) {
		read();
		printf ("Case #%d: ", tt+1);
		solve();
	}

}