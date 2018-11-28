#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void add_bits(int can, int * bits) {
	for (int i = 0; i < 32; ++i) {
		bits[i] += can & 1;
		can >>= 1;
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N;
		cin >> N;
		vector<int> candies;
		int bits[32];
		for (int i = 0; i < 32; ++i)
			bits[i] = 0;

		while (N--) {
			int can;
			cin >> can;
			add_bits(can, bits);
			candies.push_back(can);
		}
		bool no = false;
		for (int i = 0; i < 32; ++i) {
			if (bits[i] % 2 != 0) {
				cout << "Case #" << t << ": NO" << endl;
				no = true;
				break;
			}
		}
		if (!no) {
			sort(candies.begin(), candies.end());
			long long sum = 0;
			for (int i = 1; i < candies.size(); ++i) {
				sum += candies[i];
			}
			cout << "Case #" << t << ": " << sum << endl;
		}
	}
	return 0;
}
