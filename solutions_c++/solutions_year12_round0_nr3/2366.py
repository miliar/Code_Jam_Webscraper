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


int a, b, pw10[10];


void read() {
	cin >> a >> b;
}


void solve() {
	int len = 1;
	while (pw10[len] <= b)
		++len;

	int ans = 0;
	for (int n=a; n<=b; ++n) {
		static int vec[10];
		int sz = 0;

		int m = n;
		forn(i,len) {
			if (n < m && m <= b)
				vec[sz++] = m;
			m = m / 10 + m % 10 * pw10[len-1];
		}
		
		sort (vec, vec+sz);
		sz = int (unique (vec, vec+sz) - vec);
		ans += sz;
	}
	cout << ans << endl;
}



int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	pw10[0] = 1;
	fore(i,1,10)
		pw10[i] = pw10[i-1] * 10;

	int ts;
	cin >> ts;
	forn(tt,ts) {
		read();
		printf ("Case #%d: ", tt+1);
		solve();
	}

}