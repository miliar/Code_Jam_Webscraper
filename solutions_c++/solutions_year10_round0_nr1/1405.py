#include <iostream>
#include <cstdio>
#include <bitset>

using namespace std;

int main () {
	unsigned int T,N,K;
	cin >> T;
	unsigned int m;
	for (int i=0; i<T; i++) {
		cin >> N >> K;
		m = (1 << N) - 1;
		cout << "Case #" << i+1 << ": ";
		if ( (m & K) == m)
			cout << "ON";
		else
			cout << "OFF";
		cout << endl;
	}

	return 0;
}
