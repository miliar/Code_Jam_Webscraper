#include <iostream>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iterator>
#include <utility>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <queue>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forv(i, v) for(int i = 0; i < (int)v.size(); ++i)
#define fors(i, s) for(int i = 0; i < (int)s.length(); ++i)
#define all(c) c.begin(), c.end()
#define pb push_back
#define abs(a) ((a) >= 0 ? (a) : -(a))
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long ll;

int l[5000];

int getL(int v) {
	if (l[v] != v)
		l[v] = getL(l[v]);
	return l[v];
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	vector<int> primes;
	for(int i = 2; i <= 1000; ++i) {
		bool ok = true;
		for(int j = 2; j * j <= i; ++j)
			if (i % j == 0) ok = false;
		if (ok) primes.pb(i);
	}


	int tk;
	scanf("%d\n", &tk);
	int a, b, p;
	for(int tc = 1; tc <= tk; ++tc) {
		cin >> a >> b >> p;
		for(int i = a; i <= b; ++i)
			l[i] = i;
		for(int i = a; i <= b; ++i)
			for(int j = a; j < i; ++j)
				for(int k = primes.size() - 1; k >= 0 && primes[k] >= p; --k)
					if (i % primes[k] == 0 && j % primes[k] == 0) {
						l[getL(i)] = getL(j);
						break;
					}
		set<int> s;
		for(int i = a; i <= b; ++i)
			s.insert(getL(i));
		printf("Case #%d: %d\n", tc, s.size());
	}

	return 0;
}