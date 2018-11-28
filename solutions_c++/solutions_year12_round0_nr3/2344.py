#include <iostream>
#include <set>

inline int count_pairs(int n, int hi, int head) {
	std::set<int> ms;
	for (int tail = 10; head >= 10; tail *= 10, head /= 10) {
		int x = n % tail;
		if (x * 10 < tail) {
			continue;
		}
		int m = n / tail + x * head;
		if (n < m && m <= hi && ms.find(m) == ms.end()) {
			ms.insert(m);
		}
	}
	return ms.size();
}

int main() {
	int T;
	std::cin >> T;
	for (int t = 0; t < T; ++t) {
		int lo, hi;
		std::cin >> lo >> hi;
		int floor10 = 1;
		while (floor10 <= lo) {
			floor10 *= 10;
		}
		floor10 /= 10;
		int pairs = 0;
		for (int n = lo; n <= hi; ++n) {
			pairs += count_pairs(n, hi, floor10);
		}
		std::cout << "Case #" << (t + 1) << ": " << pairs << std::endl;
	}
}
