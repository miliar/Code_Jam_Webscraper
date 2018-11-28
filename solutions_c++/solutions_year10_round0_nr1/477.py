#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < n; i++)
#define seta(a, b) memset(a, b, sizeof(a))
#define x first
#define y second
#define y1 botva
#define pb push_back
#define mp make_pair
typedef long long int64;

int n, k;

void solve()
{
	cin >> n >> k;
	int mask = (1 << n) - 1;
	if ((mask & k) == mask) cout << "ON";
	else cout << "OFF";
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int tests;
	cin >> tests;
	forn(t, tests)
	{
		cout << "Case #" << t + 1 << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
