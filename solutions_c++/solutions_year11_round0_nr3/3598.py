#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <limits.h>


using namespace std;


int sum, sum_xor, m, k, n, tmp;


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> k;
	for (int counter = 1; counter <= k; counter++) {
		cin >> n;
		sum = sum_xor = 0;
		m = INT_MAX;
		for (int i = 0; i < n; i++) {
			cin >> tmp;
			m = min(m, tmp);
			sum += tmp;
			sum_xor ^= tmp;
		}
		if (sum_xor) {
			cout << "Case #" << counter << ": NO"  << endl;
		} else {
			cout << "Case #" << counter << ": " << sum - m  << endl;
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}