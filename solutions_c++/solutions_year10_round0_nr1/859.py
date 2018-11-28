#include <iostream>
using namespace std;

int main() {
	int T, N, K;

	cin >> T;

	for(int t = 1; t <= T; ++t) {
		cin >> N >> K;
		bool on = (K&((1<<N)-1)) == (1<<N)-1;
		cout << "Case #" << t << ": " << (on ? "ON" : "OFF") << "\n";
	}

	return 0;
}
