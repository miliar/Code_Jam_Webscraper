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
#include <climits>

using namespace std;

#define EPS 1E-8

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>

#define ll long long

#define NMAX 11111

int par[NMAX];

ll gcd(ll a, ll b) {
	if (a == 0) return b;
	return gcd(b % a, a);	
}

ll largest_prime(ll x) {
	ll i = 2;
	ll ans = 1;
	while (i <= x / i) {
		if (x % i == 0) {
			ans = max(ans, i);
			while (x % i == 0) x /= i;
		}
		++i;		
	}
	ans = max(ans, x);
	return ans;
}

int leader(int x) {
	if (par[x] != x) par[x] = leader(par[x]);
	return par[x];
}

void solve(int tst) {
	ll a, b, p;

	cin >> a >> b >> p;

	ll res = b - a + 1;
	
	for (int i = a; i <= b; ++i) par[i] = i;

	for (int i = a; i <= b; ++i)
		for (int j = a; j <= b; ++j) {
			ll k = gcd(i, j);

			if (largest_prime(k) >= p) {
				int x = leader(i);
				int y = leader(j);

				if (x != y) {
					--res;
					if (rand() & 1)
						par[x] = y;
					else
						par[y] = x;
				}
			}
		}

	cout << "Case #" << tst << ": " << res << endl;
}

int main() {

	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tst;
	scanf("%d", &tst);

	forn (i, tst) solve(i + 1);

	return 0;
}

