#include <iostream>
using namespace std;

bool isOn(int N, int K) {
	int m = (1 << N) - 1;
	return (K & m) == m;
}

int main() {
	int TC;
	cin >> TC;
	for (int tc = 1; tc <= TC; tc++) {
		int N,K;
		cin >> N >> K;
		cout << "Case #" << tc << ": " << (isOn(N, K) ? "ON" : "OFF") << endl;
	}
}

