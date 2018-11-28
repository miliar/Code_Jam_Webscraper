#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cassert>
#include <utility>

using namespace std;

#define EPS 1E-8

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, a) for (int i = 0; i < int(a.size()); i++)
#define fors(i, a) for (int i = 0; i < int(a.length()); i++)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>

#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

#define C_IN_FILE "input.txt"
#define C_OUT_FILE "output.txt"

vector<long long> a, b;

void outdata() {
}

void solve() {
	sort(all(a));
	sort(all(b));
	long long res = 0LL;
	reverse(all(b));
	forv(i, a) res += a[i] * b[i];
	cout << res << endl;
}

void readdata() {
	int n;
	cin >> n;
	a.resize(n);
	b.resize(n);
   	forn(i, n) cin >> a[i];
   	forn(i, n) cin >> b[i];
}

int main() {
	int tst;
	cin >> tst;
	forn(i, tst) {
		cout << "Case #" << i + 1 << ": ";
		readdata();
		solve();
		outdata();
	}
	return 0;
}
