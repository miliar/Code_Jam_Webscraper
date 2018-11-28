#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;
template <class A, class B> void CONV(A &x, B &y) { stringstream s; s << x; s >> y; }
int CMP(double a, double b) { return a < b-1e-7 ? -1 : a > b+1e-7 ? 1 : 0; }
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORE(i, v) FOR(i, 0, v.size())
#define SORT(v) sort(v.begin(), v.end())
#define SET(a, n) memset(a, n, sizeof a)

int main() {
	int c;
	cin >> c;
	FOR(i, 0, c) {
		int n;
		cin >> n;
		vector<int> t(n);
		FOR(j, 0, n) cin >> t[j];
		cout << "Case #" << i+1 << ": ";
		int d = abs(t[1]-t[0]);
		FOR(j, 2, n) d = __gcd(d, abs(t[j]-t[j-1]));
		if (d == 1) cout << "0\n";
		else {
			int mod = t[0]%d;
			if (mod == 0) cout << "0\n";
			else cout << d-mod << endl;
		}
	}
}
