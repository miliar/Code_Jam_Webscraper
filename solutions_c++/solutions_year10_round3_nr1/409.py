#include <iostream>
using namespace std;

typedef long long num;
const num max_n = 1000;
num t, n, a[max_n], b[max_n];

num get_result() {
	num res = 0;
	for (num i = 0; i < n-1; i++) {
		for (num j = i+1; j < n; j++) {
			if ((a[i] < a[j] && b[i] > b[j]) || (a[i] > a[j] && b[i] < b[j])) {
				res++;
			}
		}
	}
	return res;
}

int main() {
	cin >> t;
	for (num i = 0; i < t; i++) {
		cin >> n;
		for (num j = 0; j < n; j++) {
			cin >> a[j] >> b[j];
		}
		cout << "Case #" << (i + 1) << ": " << get_result() << "\n";
	}
	cout.flush();
	return 0;
}
