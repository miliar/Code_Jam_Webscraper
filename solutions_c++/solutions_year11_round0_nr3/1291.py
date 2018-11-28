#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main(void) {
	int T; cin >> T;
	for(int t = 0; t < T; ++t) {
		int N; cin >> N;
		int sum = 0;
		int elt_least = 2147483647;
		int xsum = 0;
		for(int i = 0; i < N; ++i) {
			int t; cin >> t;
			sum += t;
			xsum ^= t;
			elt_least = min(elt_least, t);
		}
		cout << "Case #" << (t+1) << ": ";
		if(xsum) {
			cout << "NO";
		}
		else {
			cout << (sum - elt_least);
		}
		cout << endl;
	}
	return 0;
}
