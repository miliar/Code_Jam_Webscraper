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

LL a, b, p;
LL dad[1111111];
LL dep[1111111];
LL res;

LL getroot(LL u) {
	while (u != dad[u]) u = dad[u];
	return u;
}

void merge(LL u, LL v) {
	u = getroot(u);
	v = getroot(v);
	if (u != v) res--;
	if (dep[u] > dep[v]) dad[v] = u; else
	if (dep[v] > dep[u]) dad[u] = v; else {
		dad[v] = u;
		dep[u]++;
	}
}

bool isprime(LL x) {
	if (x < 2) return false;
	for (LL i = 2; i * i <= x; i++) 
		if (x % i == 0) return false;
	return true;
}

LL solve(LL a, LL b, LL p) {
	res = b - a + 1;
	FOR(i, a, b) {
		dad[i - a] = i - a;
		dep[i - a] = 1;
	}
	for (LL i = p; i <= b - a; i++) if (isprime(i)) {
		LL u = a / i * i;
		if (u < a) u += i;
		LL start = u;
		u += i;
		while (u <= b) {
//			cout << start << " " << u << endl;
			merge(start - a, u - a);
			u += i;
		}
	}
	return res;
}

int main() {
	LL test;
	cin >> test;
	FOR(i, 1, test) {
		cout << "Case #" << i << ": ";
		cin >> a >> b >> p;
		cout << solve(a, b, p) << endl;
	}
	return 0;
}
