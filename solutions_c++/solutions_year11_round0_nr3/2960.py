
#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

#define forn(i, n) for (i = 0; i < (int)(n); ++i)

const int maxn = 1000 + 66;

int c[maxn];
int n;
int ans;

void f(int x, int p1, int p2, int s1, int s2)
{
	if (x == n) {
		if (p1 == p2 && s1 != 0 && s2 != 0)
			ans = max(ans, max(s1, s2));
		return;
	}
	f(x + 1, p1 ^ c[x], p2, s1 + c[x], s2);
	f(x + 1, p1, p2 ^ c[x], s1, s2 + c[x]);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, i;
	cin >> t;
	forn(i, t) {
		int j;
		cin >> n;
		forn(j, n)
			cin >> c[j];
		ans = -666;
		f(0, 0, 0, 0, 0);
		cout << "Case #" << i + 1 << ": ";
		if (ans == -666)
			cout << "NO" << endl;
		else
			cout << ans << endl;
	}

	return 0;
}