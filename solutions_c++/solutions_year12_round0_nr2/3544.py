#include <iostream>
#include <vector>

using namespace std;

int main() {
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		int count = 0;
		int n, s, p;
		cin >> n >> s >> p;

		for (int j = 0; j < n; j++) {
			int v;
			cin >> v;

			if (v == 0 && p > 0)
				continue;

			int diff = 3*p - v;

			if (diff <= 2) {
				count++;
			} else if (s > 0 && (diff == 3 || diff == 4)) {
				count++;
				s--;
			}
		}

		cout << "Case #" << i+1 << ": " << count << endl;
	}
}
