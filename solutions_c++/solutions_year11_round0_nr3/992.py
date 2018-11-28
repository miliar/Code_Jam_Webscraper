#include <iostream>

#define inf (1000 * 1000 * 1000)

using namespace std;

int n, a[1000];

void solve ()
{
	int all = 0, sum = 0, best = inf;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> a[i],
		all ^= a[i],
		sum += a[i],
		best = min (a[i], best);

	if (all)
	{
		cout << "NO";
		return;
	}

	cout << sum - best;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
