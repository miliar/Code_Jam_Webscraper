#include <iostream>
#include <vector>
#include <stdlib.h>

long long rnd(long long d)
{
	return (rand() * rand() * d / (RAND_MAX * RAND_MAX));
}

long long sqr(long long x)
{
	return x * x;
}

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
		int n, W, L;
		std::cin >> n >> W >> L;
		std::vector<long long> r(n), x(n), y(n);
		for (int i = 0 ; i < n ; ++i)
			std::cin >> r[i];
		bool res = false;
		while (!res)
		{
			res = true;
			int iter = 1000;
			for (int i = 0 ; iter > 0 && res && i < n ; --iter)
			{
				x[i] = rnd(W);
				y[i] = rnd(L);
				bool res1 = true;
				for (int j = 0 ; res1 && j < i ; ++j)
					if (sqr(x[i]-x[j]) + sqr(y[i]-y[j]) < sqr(r[i] + r[j]))
						res1 = false;
				if (res1)
				{
					++i;
					iter = 1000;
				}
			}
			if (iter <= 0)
				res = false;
		}
		std::cout << "Case #" << t << ":";
		std::cout.setf(std::ios::fixed);
		std::cout.precision(4);
		for (int i = 0 ; i < n ; ++i)
			std::cout << " " << x[i] << " " << y[i];
		std::cout << "\n";
	}
	return 0;
}

