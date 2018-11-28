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

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	FOR(l, 1, t+1) {
		int n, s, p;
		cin >> n >> s >> p;
		int tot = 0, tbd = 0;
		FOR(i, 0, n) {
			int x;
			cin >> x;
			bool sp = false, rp = false;
			FOR(a, 0, 11) FOR(b, 0, 11) FOR(c, 0, 11) if (a+b+c == x && abs(a-b) <= 2 && abs(a-c) <= 2 && abs(b-c) <= 2) {
				bool sur = max(max(a, b), c)-min(min(a, b), c) == 2;
				bool sat = max(max(a, b), c) >= p;
				if (sur) sp |= sat; else rp |= sat;
			}
			if (rp) tot++; else if (sp) tbd++;
		}
		tot += min(s, tbd);
		cout << "Case #" << l << ": " << tot << endl;
	}
	return 0;
}

