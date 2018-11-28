#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

void calculate(int n, int & length, int & power) {
	length = 1;
	power = 10;
	while (n /= 10) {
		++length;
		power *= 10;
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int count = 0;
		int A, B;
		cin >> A >> B;
		int len, power;
		calculate(A, len, power);
		for (int n = A; n < B; ++n) {
			vector<int> ms;
			for (int i = 1, d = 10; i < len; ++i, d *= 10) {
				int mright = n % d;
				int mleft = n / d;
				int m = mright * (power / d) + mleft;
				if (n < m && m <= B)
					ms.push_back(m);
			}
			sort(ms.begin(), ms.end());
			count += unique(ms.begin(), ms.end()) - ms.begin();
		}
		cout << "Case #" << t << ": " << count << endl;
	}
}
