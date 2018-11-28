/*
 * FreeCellStatistics
 * May 21, 2011,
 * Another buggy code by Khaled Samy;)
 */
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
using namespace std;
#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))
#define loop(i,n) 		        for(int i=0;i<(int)n;i++)
#define loop2(i,n,m)            for(int i=n;i<(int)(m);i++)

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef long long ll;
typedef stringstream SS;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

const int OO = (int) 2e9;
const double PI = 2 * acos(0.0);
const double EPS = 1e-9;

int dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a > b ? 1 : 2;
}

int DI[] = { -1, 0, 1, 0, 1, -1, -1, 1 };
int DJ[] = { 0, 1, 0, -1, 1, -1, 1, -1 };

int main() {
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.in", "wt", stdout);
#endif

	ll t;
	cin >> t;
	loop(id,t) {
		ll n, pd, pg;
		cin >> n >> pd >> pg;
		printf("Case #%d: ", id + 1);
		bool ok = 1;
		ll a[3], b[3];
		ll x = __gcd(pd, 100ll), y = __gcd(pg, 100ll);
		a[0] = pd / x, b[0] = pg / y;
		a[1] = 100 / x, b[1] = 100 / y;
		a[2] = a[1] - a[0], b[2] = b[1] - b[0];
		if (a[0] && !b[0])
			ok = false;
		if (a[1] && !b[1])
			ok = false;
		if (a[2] && !b[2])
			ok = false;
		if (n / a[1] < 1)
			ok = false;
		if (ok)
			printf("Possible\n");
		else
			printf("Broken\n");
	}
	return 0;
}
