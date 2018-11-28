#include <iostream>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int n, k;
		cin >> n >> k;
		long long need = 0;
		for (int j = 0; j < n; j++) need = need * 2 + 1;
		cout << "Case #" << i << ": ";
		if ((k + 1) % (need + 1) == 0) cout << "ON" << endl; else cout << "OFF" << endl;
	}
}