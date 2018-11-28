#include <iostream>
#include <cstdio>

int piece[1100];

long long n, pt, pg;

long long gcd(long long a, long long b)
{
	if (a % b == 0) return b;
	return gcd(b, a % b);
}

int main()
{
    int t, n;

    freopen("a.txt", "r", stdin);
	

	std::cin >> t;

	freopen("b.txt", "w", stdout);

	for (int i = 0; i < t; i++) {
		std::cin >> n >> pt >> pg;
		std::cout << "Case #" << (i + 1) << ": ";

		if (pt == 0) 
			if (pg == 100) std::cout << "Broken" << std::endl;
			else std::cout << "Possible" << std::endl;
		else if (pt < 100 && pg == 100) std::cout << "Broken" << std::endl;
		else if (pt != 0 && pg == 0) std::cout << "Broken" << std::endl;
		else if (n >= (100 / gcd(100, pt)))	std::cout << "Possible" << std::endl;
		else std::cout << "Broken" << std::endl;
	}
}