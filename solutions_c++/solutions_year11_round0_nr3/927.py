#include <iostream>
#include <stdint.h>

int main() {
	int T;
	std::cin >> T;
	for (int t = 0; t < T; ++t) {
		int N;
		std::cin >> N;
		uint32_t sum = 0;
		uint32_t min = 9999999;
		uint32_t xor_sum = 0;
		for (int n = 0; n < N; ++n) {
			unsigned c;
			std::cin >> c;
			sum += c;
			xor_sum ^= c;
			if (c < min) {
				min = c;
			}
		}
		std::cout << "Case #" << (t + 1) << ": ";
		if (xor_sum == 0) {
			std::cout << (sum - min);
		}
		else {
			std::cout << "NO";
		}
		std::cout << std::endl;
	}
}
