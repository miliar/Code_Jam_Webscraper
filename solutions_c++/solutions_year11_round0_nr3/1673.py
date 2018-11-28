#include <iostream>
#include <stdlib.h>
#include <stdint.h>
#include <limits.h>

using namespace std;

int main() {
	
	int num_case;
	cin >> num_case;
		
	for (int i = 0; i < num_case; i++) {
		int nums;
		cin >> nums;
		int min = INT_MAX;
		long long sum = 0;
		long long bit_xor = 0;
		
		for (int j = 0; j < nums; j++) {
			int temp;
			cin >> temp;
			sum += temp;
			bit_xor ^= temp;
			if (temp < min) {
				min = temp;
			}
		}
		
		if (bit_xor) {
			cout << "Case #" << i+1 << ": NO" << endl;
		} else {
			cout << "Case #" << i+1 << ": " << sum - min << endl;
		}
	}

	return 0;
}
