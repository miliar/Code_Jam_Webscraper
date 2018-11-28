#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int N;
		cin >> N;
		int total = 0;
		int smallest;
		int sum = 0;
		for (int i = 0; i < N; i++) {
			int value;
			cin >> value;
			total ^= value;
			if (i == 0) smallest = value;
			else if (value < smallest) {
				sum += smallest;
				smallest = value;
			}
			else sum += value;
		}
		cout << "Case #" << t+1 << ": ";
		if (total != 0) cout << "NO\n";
		else cout << sum << '\n';
	}
	return 0;
}
