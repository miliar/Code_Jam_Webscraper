#include <string>
#include <iostream>

using namespace std;

int main () {
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; ++i) {
		int nums;
		cin >> nums;

		int result = 0,
			minnum = 1000000000,
			sum	   = 0;

		for (int j = 0; j < nums; ++j) {
			int n;
			cin >> n;
			result ^= n;
			sum	   += n;
			minnum  = minnum > n ? n : minnum;
		}

		if (result != 0)
			cout << "Case #" << i << ": " << "NO" << endl;
		else
			cout << "Case #" << i << ": " << sum - minnum << endl; 
	}

	return 0;
}