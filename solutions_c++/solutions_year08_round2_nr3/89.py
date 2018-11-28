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

#define REP(i, n) for (int i = 0; i < (n); i++)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define SZ(a) a.size()

string i2s(int x) { ostringstream tmp;  tmp << x;  return tmp.str(); }
int s2i(string s) { istringstream i(s);  int x;  i >> x;  return x; } 

int n, k;
int a[6111];
int b[6111];

void process() {
	memset(b, 0, sizeof(b));
	int pos;
	int startat = 1;
	int rem = k;
	FOR(i, 1, k) {
//		cout << i << endl;
		pos = startat;
		int cnt = 0;
		int mt = i % (k - i + 1);
		if (mt == 0) mt = k - i + 1;
//		cout << mt << endl;
		while (true) {
			if (b[pos] == 0) cnt++;
			if (cnt == mt) break;
			else {
				pos = pos + 1;
				if (pos > k) pos = 1;
			}
		}
		b[pos] = i;
		startat = (pos + 1);
		if (startat > k) startat = 1;
	}
	FOR(i, 1, n) cout << " " << b[a[i]];
	cout << endl;
}

int main() {
	int test;
	cin >> test;
	FOR(i, 1, test) {
		cout << "Case #" << i << ":";
		cin >> k >> n;
		FOR(i, 1, n) cin >> a[i];
		process();
	}
	return 0;
}
