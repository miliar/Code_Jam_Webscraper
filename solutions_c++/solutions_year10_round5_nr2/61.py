#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

int test;
string name = "b";

typedef long long ll;

ll L;

int b[1 << 7];
int n;

const int mm = 100;
const int nn = 10 * mm * mm;

int a[nn];

void solve()
{
	long long ans = -1;

	cin >> L >> n;
	for (int i = 0; i < n; i++) cin >> b[i];

	memset(a, -1, sizeof a);
	a[0] = 0;
	for (int i = 0; i < nn; i++) if (a[i] >= 0)
	{
		for (int j = 0; j < n; j++) if (i + b[j] < nn) 
			a[i + b[j]] = a[i + b[j]] == -1 ? a[i] + 1 : min(a[i + b[j]], a[i] + 1);
	}

	int B = 0;
	for (int i = 0; i < n; i++) B = max(B, b[i]);

	for (int i = 0; i < nn; i++) if (a[i] >= 0 && (L - i) % B == 0)
	{
		long long cur = a[i] + (L - i) / B;
		if (ans == -1 || ans > cur) ans = cur;
	}

	cout << "Case #" << test << ": ";
	if (ans >= 0)
		cout << ans << endl;
	else
		cout << "IMPOSSIBLE" << endl;

	cerr << "Case #" << test << ": ";
	cerr << ans << endl;
}

int main()
{
	freopen((name + ".in").c_str(), "r", stdin);
	freopen((name + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (test = 1; test <= tests; test++)
		solve();

	return 0;
}