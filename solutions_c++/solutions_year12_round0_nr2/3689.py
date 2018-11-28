#include <iostream>

using namespace std;


int main() {
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int n, s, p;
		cin >> n >> s >> p;
		//int *ti = new int[n];
		int needSupprise = 0;
		int possible = 0;
		for (int x = 0; x < n; ++x) {
			int y = 0;
			cin >> y;
			if (y >= (3*p - 4) && y < 3*p - 2 && y >= p) {
				++needSupprise;
			} else if (y >= 3*p - 2) {
				++possible;
			}
		}
		cout << "Case #" << i + 1 << ": " << possible + min(needSupprise, s) << endl;
		//delete[] ti;
	}
}