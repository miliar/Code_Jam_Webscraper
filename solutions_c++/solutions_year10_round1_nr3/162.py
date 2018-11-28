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

int last;

bool check(int a, int b, bool flag) {
	if (a == last || b == last) return flag;
	if (a > b) {
		if (a-b > b) return flag;
		return check(a-b, b, !flag);
	}
	if (b-a > a) return flag;
	return check(a, b-a, !flag);
}

int main() {
	int t;
	cin >> t;
	FOR(i, 0, t) {
		int a1, a2, b1, b2;
		cin >> a1 >> a2 >> b1 >> b2;
		int res = 0;
		FOR(j, a1, a2+1) FOR(k, b1, b2+1) {
			last = __gcd(j, k);
			if (j == last && k == last) continue;
			res += check(j, k, true);
		}
		cout << "Case #" << i+1 << ": " << res << endl;	
	}
}
