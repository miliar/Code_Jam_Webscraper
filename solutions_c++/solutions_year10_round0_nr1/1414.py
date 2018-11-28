#include <iostream>

int main() {
	int nCases;
	std::cin >> nCases;
	for (int i = 0; i < nCases; ++i) {
		int n, k;
		std::cin >> n >> k;
		std::cout << "Case #" << (i + 1) << ": "
		          << ( (k & ((1 << n) - 1)) == ((1 << n) - 1) ? "ON" : "OFF") << std::endl;
	}
}
