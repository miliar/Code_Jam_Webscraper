#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i, n) for (LL i = 0; i < (n); i++)
#define FOR(i, a, b) for (LL i = (a); i <= (b); i++)
#define FORD(i, a, b) for (LL i = (a); i >= (b); i--)
#define SZ(a) a.size()
#define LL long long

string i2s(LL x) { ostringstream tmp;  tmp << x;  return tmp.str(); }
LL s2i(string s) { istringstream i(s);  LL x;  i >> x;  return x; } 

LL n;
LL x[111111];
LL y[111111];
LL cnt[3][3];

LL process() {
	LL res = 0;
	REP(x1, 3) REP(x2, 3) REP(x3, 3) if ((x1 + x2 + x3) % 3 == 0)
	REP(y1, 3) REP(y2, 3) REP(y3, 3) if ((y1 + y2 + y3) % 3 == 0) {
		LL u = cnt[x1][y1];
		LL v = cnt[x2][y2];
		LL w = cnt[x3][y3];
		if (x1 == x2 && y1 == y2) v--;
		if (x1 == x3 && y1 == y3) w--;
		if (x2 == x3 && y2 == y3) w--;
		if (u && v && w) {
			res += u * v * w;
		}
	}
//	res -= n;
	return res / 6;
}

void loai_trung() {
	vector<string> a;
	a.clear();
	REP(i, n) {
		string s = i2s(x[i]) + " " + i2s(y[i]);
		a.push_back(s);
	}
	sort(a.begin(), a.end());
	FORD(i, a.size()-1, 1) if (a[i] == a[i - 1]) {
		a.erase(a.begin() + i);
	}
	n = a.size();
//	REP(i, n) cout << a[i] << endl;
	memset(cnt, 0, sizeof(cnt));
	REP(i, n) {
		istringstream ss(a[i]);
		ss >> x[i] >> y[i];
		cnt[x[i]%3][y[i]%3]++;
	}
}

int main() {
	LL test;
	cin >> test;
	FOR(i, 1, test) {
		LL a, b, c, d, M,;
		cin >> n >> a >> b >> c >> d >> x[0] >> y[0] >> M;
		FOR(j, 1, n - 1) {
			x[j] = (a * x[j - 1] + b) % M;
			y[j] = (c * y[j - 1] + d) % M;
//			cout << x[j] << " " << y[j] << endl;
		}
		loai_trung();
		cout << "Case #" << i << ": ";
		cout << process() << endl;
	}
	return 0;	
}
