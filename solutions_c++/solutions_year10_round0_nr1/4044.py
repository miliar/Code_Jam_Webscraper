/*

n = 1: 1, 3, 5, 7, 9, 11, ...
n = 2: 3, 7, 11, 15, 19
n = 3: 7, 15, 23, 31
if (k == b * 2 ^ n - 1)

*/

#include <iostream>

using namespace std;

int T, n, k;

int main() {
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> n >> k;
		cout << "Case #" << i << ": " << (((k | ((1 << n) - 1)) == k) ? "ON" : "OFF") << endl;		
	}
	
	return 0;
}