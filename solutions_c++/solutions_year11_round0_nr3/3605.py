#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int test;
	cin >> test;
	for (int tt = 1; tt <= test; tt++) {
		cout << "Case #" << tt << ": ";
		int n;
		cin >> n;
		int xsum = 0, mini = 1000000000, sum = 0;
		for (int i = 0; i < n; i++) {
			int x;
			cin >> x;
			xsum ^= x;
			sum += x;
			mini = min(x, mini);
		}
		if (xsum != 0) cout << "NO" << endl; else cout << sum - mini << endl;
	}
}

