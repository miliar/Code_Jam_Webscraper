#include <iostream>
#include <vector>

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
		int n;
		std::cin >> n;
		std::vector<int> d(n), L(n), h(n, -1);
		for (int i = 0 ; i < n ; ++i)
		{
			std::cin >> d[i] >> L[i];
		}
		int D;
		std::cin >> D;

		h[0] = d[0];
		bool res = false;
		for (int i = 0 ; i < n ; ++i)
		{
			if (h[i] < 0)
				continue;
			if (D - d[i] <= h[i])
				res = true;
			int j = i + 1;
			while (j < n && d[j] - d[i] <= h[i])
			{
				h[j] = std::max(h[j], std::min(d[j] - d[i], L[j]));
				++j;
			}
		}

		std::cout << "Case #" << t << ": " << (res ? "YES" : "NO") << "\n";
	}
	return 0;
}

