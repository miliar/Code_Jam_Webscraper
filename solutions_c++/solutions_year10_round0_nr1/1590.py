#include <iostream>


using namespace std;

int main() {
	int t,n,k;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> n >> k;
		n = 1 << n;
		cout << "Case #" << i << ": " << (k%n == n-1 ? "ON" : "OFF") << endl;
	}
}