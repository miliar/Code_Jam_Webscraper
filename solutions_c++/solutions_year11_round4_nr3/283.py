#pragma comment(linker, "/STACK:512000000")

#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define forv(i, v) forn(i, (v).size())
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef long double ld;

typedef vector<int> VI;
typedef vector<bool> VB;
typedef pair<int, int> Edge;
typedef vector<vector<Edge> > Graph;

void init()
{
	freopen("input.txt", "rt", stdin);
}

vector<pair<int, int> > factorize(int n) {
	vector<pair<int, int> > result;
	for(int i = 2; i <= n; ++i) {
		if (n % i == 0) {
			int cnt = 0;
			while (n % i == 0) {
				cnt++;
				n /= i;
			}
			result.pb(mp(i, cnt));
		}
	}
	if (n > 1) {
		result.pb(mp(n, 1));
	}
	return result;
}

bool prime(int n) {
	for(int i = 2; i * i <= n; ++i) {
		if (n % i == 0) return false;
	}
	return true;
}

bool primes[1000005];

void findPrimes()
{
	for(int i = 2; i <= 1000000; ++i) {
		if (primes[i]) continue;
		for(int j = i + i; j <= 1000000; j += i) primes[j] = true;
	}
}

int main()
{
//	init();
	findPrimes();
	int tc; cin >> tc;
	forn(it, tc) {
		ll n;
		cin >> n;
		map<int, int> used;
		ll ans = 1;
		for(ll i = 2; i * i <= n; ++i) {
			if (!primes[i]) {
				ll t = i * i;
				ll k = n / t;
				while (k > 0) k /= i, ++ans;
			}
		}
		if (n == 1) --ans;
		cout << "Case #" << it + 1 << ": " << ans << endl;
	}

	return 0;
}
