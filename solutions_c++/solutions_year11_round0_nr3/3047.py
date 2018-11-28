#include <iostream>

int main (void) {
	int n;
	std::cin >> n;
	for (int i = 1; i <= n; ++i) {
		int nbC;
		int s = 0;
		int m = 100000;
		int x = 0;
		for (std::cin >> nbC; nbC > 0; --nbC) {
			int t;
			std::cin >> t;
			x ^= t;
			s += t;
			if (t < m)
				m = t;
		}

		std::cout << "Case #" << i << ": ";
		if (x == 0)
			std::cout << s - m << std::endl;
		else
			std::cout << "NO" << std::endl;
	}
	return 0;
}
