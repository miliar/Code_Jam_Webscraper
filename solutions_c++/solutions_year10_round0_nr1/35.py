#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int q=1; q<=T; q++) {
		int N, K;
		cin >> N >> K;
		cout << "Case #" << q << ": " << ((K & ((1<<N)-1)) == ((1<<N)-1) ? "ON" : "OFF") << endl;
	}
	return 0;
}