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
#include <cmath>
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

string toBin(ll x) {
	string ret;
	while (x) {
		ret.pb('0' + (x & 1));
		x >>= 1;
	}
	reverse(all(ret));
	return ret;
}

bool isSquare(ll x)
{
	ll y = sqrt(x*1.0);
	forn(i, 4) {
		if ((y + i - 2) * (y + i - 2) == x) return true;
	}
	return false;
}

int main()
{
//	init();
	int tc; cin >> tc;
	forn(it, tc) {
	string s; cin >> s;
	ll n = 0;
	vector<ll> shifts;
	reverse(all(s));
	forv(i, s) {
		if (s[i] == '1') {
			n += (1LL << (ll(i)));
		}
		else if (s[i] == '?') shifts.pb(i);
	}
	ll ans = 0;
	forn(mask, 1 << shifts.size()) {
		ll cand = n;
		forv(i, shifts) {
			if (mask & (1 << i)) cand += (1LL << shifts[i]);
		}
		if (isSquare(cand)) {
			ans = cand;
			break;
		}
	}
	cout << "Case #" << it + 1 << ": " << toBin(ans) << endl;
	}
	return 0;
}
