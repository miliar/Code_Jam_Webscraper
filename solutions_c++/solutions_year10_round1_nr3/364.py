#include <iostream>

#define PHI 1.6180339887498948482045868343656

long solve(long a1, long a2, long b1, long b2)
{
	long result = 0;
	for (int i = a1; i <= a2; i++) {
		for (int j = b1; j <= b2; j++) {
			if ((double) PHI * j < i) {
				result++;
			} else if ((double) PHI * i < j) {
				result++;
			}
		}
	}
	return result;
}

int main()
{
	long t;
	std::cin >> t;
	for (int i = 0; i < t; i++) {
		long a1, a2, b1, b2;
		std::cin >> a1 >> a2 >> b1 >> b2;
		std::cout << "Case #" << i+1 << ": " << solve(a1, a2, b1, b2) << std::endl;
	}
	return 0;
}
	
