/*
 * dancers.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: chfast
 */

#include <iostream>
#include <vector>

int main() {

	int T; std::cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N; std::cin >> N;
		int S; std::cin >> S;
		int p; std::cin >> p;
		int min = p + 2 * std::max(p-1, 0);
		int minS = p + 2 * std::max(p-2, 0);
//		std::vector<int> x(N);
		int R = 0;
		for (int i = 0; i < N; ++i) {
			int x; std::cin >> x;
			if (x >= min) {
				++R;
			}
			else if (S > 0 && x >= minS) {
				++R;
				--S;
			}
		}
		std::cout << "Case #" << t << ": " << R << std::endl;
	}

	return 0;
}


