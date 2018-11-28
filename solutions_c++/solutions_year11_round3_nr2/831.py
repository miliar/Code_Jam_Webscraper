#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	int testNo;
	cin >> testNo;
	for (int ctest = 1; ctest <= testNo; ctest++) {
		cout << "Case #" << ctest << ": ";
		int L, n, C;
		long long t;
		cin >> L >> t >> n >> C;
		vector<int> a(C);
		for (int i = 0; i < C; i++) {
			cin >> a[i];
		}
		a.resize(n);
		for (int i = C; i < n; i++) {
			a[i] = a[i-C];
		}
		vector<int> q;
		long long res = 0;
		for (int i = 0; i < n; i++) {
			if (t <= 0)
				q.push_back(a[i]);
			else
				q.push_back((2*a[i] - t) / 2);
			t -= 2*a[i];
			res += 2*a[i];
		}
		sort(q.begin(), q.end());
		for (int i = max(0, (int)q.size() - L); i < (int)q.size(); i++) {
			res -= q[i];
		}
		cout << res << endl;
	}
	return 0;
}