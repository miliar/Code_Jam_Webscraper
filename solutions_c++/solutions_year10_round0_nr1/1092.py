#include <iostream>

bool solve(int n, long k)
{
	long m = 1;
	for (int i = 0; i < n; i++) {
		m *= 2;
	}
	return ((k+1) % m == 0);
}

int main()
{
	long t, n, k;
	std::cin >> t;
	for (int i = 0; i < t; i++) {
		std::cin >> n >> k;
		std::cout << "Case #" << i+1 << ": " << (solve(n,k)?"ON":"OFF") << std::endl;
	}
	return 0;
}
	
