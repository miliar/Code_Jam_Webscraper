#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

#define inf (-2000*1000*1000)

int n, c[2000], ans, xor;

void solve()
{
	cin >> n;
	for(int i = 0; i < n; i++)
		cin >> c[i];
	sort(c, c + n);
	xor = ans = c[1];
	for(int i = 2; i < n; i++)
	{
		ans += c[i];
		xor ^= c[i];
	}
	if (xor != c[0])
		cout << "NO";
	else
		cout << ans;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}