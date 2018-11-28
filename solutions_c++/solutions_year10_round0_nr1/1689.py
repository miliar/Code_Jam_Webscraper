#include <iostream>
#include <vector>
using namespace std;

bool solve(int n, int k) {
	return (k + 1) % (1 << n) == 0;
}

int main() {
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		int n, k;
		cin >> n >> k;
		string res = solve(n, k) ? "ON" : "OFF";
		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}
