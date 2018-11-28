#include <iostream>


int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
		int res = 0;
		int n, s, p;
		std::cin >> n >> s >> p;
		for (int i = 0 ; i < n ; ++i)
		{
			int k;
			std::cin >> k;
			int a = k / 3;
			switch (k % 3)
			{
			case 0:
				if (a >= p)
				{
					++res;
				}
				else if (a > 0 && a + 1 >= p && s)
				{
					--s;
					++res;
				}
				break;
			case 1:
				if (a < 10 && a + 1 >= p)
					++res;
				break;
			case 2:
				if (a < 10 && a + 1 >= p)
				{
					++res;
				}
				else if (a < 9 && a + 2 >= p && s)
				{
					--s;
					++res;
				}
				break;
			}
		}
		std::cout << "Case #" << t << ": " << res << "\n";
	}
	return 0;
}

