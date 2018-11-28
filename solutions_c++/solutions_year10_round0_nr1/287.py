#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++ i) {
		int N, K;
		cin >> N >> K;
		const int n = (1<<N)-1;
		if ((K & n) == n) {
			cout << "Case #" << i << ": ON" << endl;
		} else {
			cout << "Case #" << i << ": OFF" << endl;
		}
	}
}
