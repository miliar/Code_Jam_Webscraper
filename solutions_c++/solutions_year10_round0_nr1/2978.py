#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		int n, k;
		cin >> n >> k;
		cout << "Case #" << cas << ": ";
		if ((k+1)%(1<<n) == 0) cout << "ON";
		else cout << "OFF";
		cout << endl;
	}
}
