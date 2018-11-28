#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <cassert>
#include <cmath>
#include <deque>
#include <sstream>
using namespace std;
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define only(v) v.erase(unique(all(v)), v.end())
typedef  vector<int> VI;
typedef  pair<int, int> pii;
typedef vector<string> VS;
#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

void solve(int tc)
{
	printf("Case #%d: ", tc);
	int n, k, b, t;
	cin >> n >> k >> b >> t;
	vector<int> x(n);
	vector<int> v(n);
	forn(i, n) cin >> x[i];
	forn(i, n) cin >> v[i];
	int ans = 0;
	for(int i = n-1; i >= 0; i--)
	{
		if (k == 0) break;
		if (v[i] * t >= b - x[i]) k--;
		else ans += k;
	}
	if (k) cout << "IMPOSSIBLE" << endl;
	else cout << ans << endl;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
#endif

	int tc; cin >> tc;
	forn(i, tc) solve(i+1);

	return 0;
}
