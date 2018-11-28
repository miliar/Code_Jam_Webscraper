#include <iostream>
#include <climits>

using namespace std;

void solve()
{
	int n;
	cin >> n;
	int sum = 0;
	int dumbsum = 0;
	int smallest = INT_MAX;
	for (int i = 0; i < n; ++i)
	{
		int t;
		cin >> t;
		sum += t;
		dumbsum ^= t;
		smallest = min(smallest, t);
	}
	if (dumbsum)
		cout << "NO" << endl;
	else
		cout << sum - smallest << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
}
