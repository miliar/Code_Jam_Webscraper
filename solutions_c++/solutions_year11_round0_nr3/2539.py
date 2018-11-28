#include <iostream>

int main() {
	unsigned int T;
	std::cin >> T;
	for (unsigned int i=0; i<T; i++) {
		unsigned int sum = 0;
		unsigned int xored = 0;
		unsigned int min = (unsigned int)-1;
		unsigned int N;
		std::cin >> N;
		for (unsigned int j=0; j<N; j++) {
			unsigned int x;
			std::cin >> x;
			sum += x;
			xored ^= x;
			if (x<min) min = x;
		}
		std::cout << "Case #" << (i+1) << ": ";
		if (xored==0)
			std::cout << (sum-min) << std::endl;
		else
			std::cout << "NO\n";
	}
	return 0;
}

