#pragma comment (linker, "/STACK:200000000")
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
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
#define pb  push_back
#define mp  make_pair
#define fs  first
#define sc  second


int64 n;


void read() {
	cin >> n;
}


vector<int> p;


void solve() {
	if (n == 1) {
		puts ("0");
		return;
	}
	int ans = 1;
	forn(i,p.size()) {
		long long j = p[i] * 1ll * p[i];
		if (j > n)  break;

		double jj = p[i] * 1.0 * p[i];
		for(;;) {
			++ans;
			j *= p[i];
			jj *= p[i];
			if (j < 0 || jj > 1E15 || j > n)  break;
		}
	}

	cout << ans << endl;
}


const int MAXN = 1100000;

bool pr[MAXN];

int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	memset (pr, 1, sizeof pr);
	fore(i,2,MAXN)
		if (pr[i]) {
			p.pb (i);
			for (int j=i*2; j<MAXN; j+=i)
				pr[j] = false;
		}

	int ts;
	cin >> ts;
	forn(tt,ts) {
		read();
		printf ("Case #%d: ", tt+1);
		solve();
	}

}