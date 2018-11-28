#include <iostream>
using namespace std;		

int main () {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n; cin >> n;
	for (int i = 0; i < n; i ++) {
		int c; cin >> c;
		int a[2000];
		int res = 0,sum = 0,m = 10000000;
		for (int j = 0; j < c; j ++) {
			cin >> a[j];
			res ^= a[j];
			sum += a[j];
			if (a[j] < m) m = a[j];
		}
		cout << "Case #" << i + 1 << ": ";
		if (res) cout << "NO\n"; else cout << sum - m << "\n";
	}
	return 0;
}