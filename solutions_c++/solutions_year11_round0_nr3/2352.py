#include <iostream>

int main()
{
	int t;
	std::cin >> t;
	for (int currtest = 1; currtest <= t; currtest++)
	{
		int n;
		std::cin >> n;
		int min = 0x7FFFFFFF;
		int sum = 0;
		int xorsum = 0;
		for (int i = 0; i < n; i++)
		{
			int c;
			std::cin >> c;
			if (c < min) min = c;
			sum += c;
			xorsum ^= c;
		}
		
		if (xorsum)
			std::cout << "Case #" << currtest << ": " << "NO" << "\n";
		else std::cout << "Case #" << currtest << ": " << sum-min << "\n";
	}

	return 0;
}
