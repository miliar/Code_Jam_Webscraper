#include <iostream>

int main() {
	unsigned int T;
	std::cin >> T;
	
	for (unsigned int i = 0; i < T; i++) {
		unsigned int N;
		std::cin >> N;
		unsigned int candies[N];
		unsigned int smallest = -1;
		unsigned int result = 0;
		unsigned long long sum = 0;

		for (unsigned int j = 0; j < N; j++) {
			std::cin >> candies[j];
			result ^= candies[j];
			sum += candies[j];
			if (candies[j] < smallest) smallest = candies[j];
		}
		
		std::cout << "Case #" << (i+1) << ": ";
		if (result) std::cout << "NO";
		else std::cout << (sum-smallest);
		
		std::cout << std::endl;
	}
}
