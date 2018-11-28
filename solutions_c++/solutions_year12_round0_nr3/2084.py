#include <iostream>
#include <sstream>

int main() {
	int T;
	long A, B, C;
	std::cin >> T;

	for (int i = 0; i < T; ++i) {
		long ans = 0;
		std::cin >> A >> B;
		
		// calculate base and number of digits for A and B
		std::string str; std::stringstream out;
		out << A; str = out.str();
		int digits = str.length();
		long base = 1;
		for (int d = 0; d < digits - 1; ++d) base *= 10;

		// initialize bit_map
		long s_size = B - A + 1;
		long * bit_map = new long[s_size];
		for (long j = 0; j < s_size; ++j) bit_map[j] = 1;

		// calculate answer
		long * local_map = new long[digits];
		for (long k = 0; k < s_size; ++k) {
			if (bit_map[k] == 0) continue;

			int numbers_in_group = 1;
			long num = A + k, rem, idx;

			// reset local_map
			for (int l = 0; l < digits; ++l) local_map[l] = 0;
			local_map[0] = num;

			for (int x = 0; x < digits - 1; ++x) {
				rem = num % 10;
				if (rem == 0) {
					num /= 10;
					continue;
				}

				num = num / 10 + rem * base;
				if ((num > B) || (num < A)) continue;

				idx = num - A;

				if (bit_map[idx] == 0) {
					continue;
				} else {
					bit_map[idx] = 0;

					bool found = false;
					int l_idx = 0;
					for (l_idx = 0; l_idx < digits; ++l_idx) {
						if (local_map[l_idx] == 0) break;
						if (local_map[l_idx] == num) {
							found = true;
							break;
						}
					}

					if (found == false) {
						local_map[l_idx] = num;
						++numbers_in_group;
					}
				}
			}

			if (numbers_in_group > 1) {
				ans += numbers_in_group * (numbers_in_group - 1) / 2;
			}

		}

		delete [] bit_map;

		std::cout << "Case #" << (i + 1) << ": " << ans << std::endl; 
	}

	return 0;
}

