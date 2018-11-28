#include <cstdio>
#include <iostream>

using namespace std;

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int t_i = 1; t_i <= t; t_i++) {
		int n;
		cin >> n;
		int xorofall = 0;
		int a;
		int sumofall = 0;
		int minv = 1000001;
		for (int i = 0; i < n; i++) {
			cin >> a;
			xorofall ^= a;
			sumofall += a;
			if (a < minv) minv = a;
		}
		cout << "Case #" << t_i << ": ";
		if (xorofall) {
			cout << "NO";
		} else {
			cout << sumofall - minv;
		}
		cout << "\n";
	}
}
