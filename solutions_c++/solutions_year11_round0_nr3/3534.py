#include <iostream>

using namespace std;

int main() {
	int T,N;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cin >> N;
		long long int num, sum, rxor, min;
		cin >> num;
		min = num;
		sum = num;
		rxor = num;
		for(int j = 1; j< N; j++) {
			cin >> num;
			sum += num;
			if(num < min) min = num;
			rxor = rxor^num;
		}
		if(rxor != 0) cout << "Case #" << i << ": NO\n";
		else cout << "Case #" << i << ": " << sum-min << "\n";	
	}
}
