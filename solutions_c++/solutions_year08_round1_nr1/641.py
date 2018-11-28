#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		long long n, i, x[800], y[800], r = 0;
		
		cin >> n;
		for (i = 0; i < n; i++) cin >> x[i];
		for (i = 0; i < n; i++) cin >> y[i];
		
		sort(x, x + n);
		sort(y, y + n);
		for (i = 0; i < n; i++) r += x[i] * y[n - i - 1];
		
		cout << "Case #" << it << ": " << r << '\n';
	}
	
	return 0;
}
