
#include <iostream>
#include <cstdlib>

main ()
{
	int cases;
	std::cin >> cases;

	for (int x = 1; x <= cases; ++x)
	{
		int N;
		std::cin >> N;

		int num = 0;
		for (int n = 1; n <= N; ++n)
		{
			int a;
			std::cin >> a;
			if (n != a) ++num;
		}

		std::cout << "Case #" << x << ": " << num << std::endl;
	}
}
