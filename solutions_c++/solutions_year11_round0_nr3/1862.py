#include <iostream>
#include <algorithm>
using namespace std;

int a[1000];

void solve()
{
	int n;
	cin >> n;
	int xor = 0;
	int sum = 0;
	for(int i = 0; i < n; ++i) {
		cin >> a[i];
		xor ^= a[i];
		sum += a[i];
	}
	if (xor) {
		cout << "NO\n";
		return;
	}

	sort(a, a + n);
	cout << sum - a[0] << "\n";
}

int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t; 
	cin >> t;
	for(int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return (0);
}