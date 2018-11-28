#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <deque>
#include <assert.h>
#include <ctime>
#include <bitset>
#include <numeric>
#include <complex>
using namespace std;

#define double long double
#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for (register int i = (a); i < (int)(n); ++i)
#define FORE(i, a, n) for (i = (a); i < (int)(n); ++i)
#define Size(n) ((int)(n).size())
#define all(n) (n).begin(), (n).end()
#define ll long long
#define pb push_back
#define error(x) cout << #x << " = " << x << endl;
#define ull unsigned long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<double, double>
#define point complex<double>
#define X real()
#define Y imag()
//#define X first
//#define Y second
#define EPS 1e-20
#define endl "\n"
#define pdd pair<double, double>
bool gt(double a, double b) { return a > b+EPS; }

bool ok(string a, string b) {
	if (a[0] == '0' || b[0] == '0' || Size(a) != Size(b) || a >= b) return false;
	FOR(i, 1, Size(a)) if (a.substr(i)+a.substr(0, i) == b) return true;
	return false;
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	FOR(l, 1, t+1) {
		ll a, b, tot = 0, len = 1, p10 = 1;
		cin >> a >> b;
		while (p10*10 < b) len++, p10 *= 10;
		FOR(i, a, b) {
			ll num = i;
			FOR(rep, 1, len) {
				num = num/10 + p10*(num%10);
				if (num == i) break;
				if (num > i && num <= b) tot++;
			}
		}
		cout << "Case #" << l << ": " << tot << endl;
	}
	return 0;
}

