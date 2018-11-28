#include <iostream>

using namespace std;

int main() {
	int test;
	cin >> test;
	for (int itest = 1; itest <= test; itest++) {
		int n;
		cin >> n;
		int ans = 0;
		int sum = 0;
		int min = 123456789;
		for (int i = 0; i < n; i++) {
			int p;
			cin >> p;
			ans += p;
			sum = sum ^ p;
			if (p < min) min = p;
		}
		ans -= min;
		if (sum != 0) cout << "Case #" << itest << ": NO" << endl;
		else cout << "Case #" << itest << ": " << ans << endl;
	}	
	return 0;
}
