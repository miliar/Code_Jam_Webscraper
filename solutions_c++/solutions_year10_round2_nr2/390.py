#include<iostream>
#include<vector>

using namespace std;


int main() {
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test) {
		int count, winners, time, barn;
		cin >> count;
		cin >> winners;
		cin >> barn;
		cin >> time;
		vector<int> x(count);
		vector<int> v(count);
		for (int i = 0; i < count; ++i) {
			cin >> x[i];
		}
		for (int i = 0; i < count; ++i) {
			cin >> v[i];
		}
		int ok = 0;
		int res = 0;
		int current = count - 1;
		while ((current >= 0) && (ok != winners)) {
			if (x[current] + v[current] * time >= barn) {
				++ok;
			} else {
				res += (winners - ok);
			}
			--current;
		}
		if (ok == winners) {
			cout << "Case #" << test + 1 << ": " << res << endl;
		} else {
			cout << "Case #" << test + 1 << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}