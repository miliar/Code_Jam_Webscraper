#include <iostream>
#include <cmath>
using namespace std;


bool pass(int N, int K) {
	int n = pow(2, (double) N);
	if(!(K & 1)) return false;
	return (K % n == n-1);
}

int main() {
	int T, N, K, i;
	cin >> T;
	i = T;
	while(T--) {
		cin >> N >> K;
		cout << "Case #" << (i-T) <<": " << (pass(N, K)  ? "ON" : "OFF") << endl;
	}
}
