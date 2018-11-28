#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

void solve (int I)
{
	//freopen("input.txt", "r", stdin);
	int sum = 0;
	int mn = 1e9;
	int xr = 0;
	int n, x;
	
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> x;
		sum += x;
		mn = min(mn, x);
		xr ^= x;
	}
	cout << "Case #" << I << ": ";
	if (xr) cout << "NO";
	else cout << sum - mn;
	cout << "\n";
};
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios :: sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) solve(i+1);
	return 0;
};
