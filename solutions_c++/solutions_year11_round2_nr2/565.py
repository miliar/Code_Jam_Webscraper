#include <iostream>
#include <algorithm>
#include <iomanip>

#define maxN (100 + 100)
#define inf (1000 * 1000 * 1000)

using namespace std;

int c, d, n;
int a[maxN];

bool check (int x)
{
	int last = -inf;

	for (int i = 0; i < n; i++)
	{
		int v = max (a[i] - x, last);
		if (v > a[i] + x)
			return 0;

		last = v + d;
	}
 
	return 1;
}

double solve()
{
	int i;
	cin >> c >> d;
	d *= 2;
	for (i = 0, n = 0; i < c; i++)
	{
		int p, v;
		cin >> p >> v;
		p *= 2;
		for (int k = 0; k < v; k++, n++)
			a[n] = p;
	}

	sort (a, a + n);

	for (int i = d * n; i >= 0; i--)
		if (!check (i))
			return i + 1;
	return 0;
}

int main()
{
	int t; cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": " << fixed << setprecision (6) << solve() / 2.0 << endl;
	}

	return 0;
}
