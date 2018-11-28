#include <iostream>
using namespace std;

long long T, N, K;

int main() {
	cin >> T;
	for (int i=0; i<T; ++i) {
		cin >> N >> K;
		bool ok = ((K) & ((1<<(N))-1)) == ((1<<N)-1); 
		cout << "Case #" << (i+1) << ": " << (ok ? "ON" : "OFF") << endl;
	}
	return 0;
}
