#include <iostream>

int main() {
	int T = 0; 
	std::cin >> T;

	for (int i = 0; i < T; ++i) {
		int N, S, p, p3, ti;
		std::cin >> N >> S >> p;
		p3 = 3 * p;

		int ans = 0;
		for (int j = 0; j < N; ++j) {
			std::cin >> ti;
			if (ti >= p3 - 2) ++ans; 
			else if (ti + 4 < p3) continue;
			else if ((S > 0) && (ti > 1)) { 
				++ans; --S;
			} 
		}

		std::cout << "Case #" << (i + 1) << ": " << ans << std::endl;
	}

	return 0;
}
