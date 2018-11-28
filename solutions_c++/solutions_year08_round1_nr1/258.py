#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int T;
	int a[1000], b[1000], n;
	cin >> T;
	for(int t = 0; t < T; t++) {
		cin >> n;
		for(int i = 0; i < n; i++)
			cin >> a[i];
		for(int j = 0; j < n; j++)
			cin >> b[j];
		sort(a, a+n);
		sort(b, b+n);
		int ans = 0;
		for(int i = 0, j = n-1; i < n; i++, j--)
			ans += a[i]*b[j];
		cout << "Case #" << t+1 << ": " << ans << endl;
	}
	return 0;
}
