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
		std::vector<int> next(n), h(n);
		for (int i = 0 ; i < n - 1 ; ++i)
		{
			std::cin >> next[i];
			--next[i];
		}
		bool res = true;
		for (int i = 0 ; i < n - 1 ; ++i)
			for (int j = i + 1 ; j < next[i] ; ++j)
				if (next[j] > next[i])
					res = false;
		if (res)
		{
			h[n - 1] = 1024 * 1024;
			for (int i = n - 1 ; res && i >= 0 ; --i)
			{
				int t = -1;
				for (int j = 0 ; res && j < i ; ++j)
				{
					if (next[j] == i)
					{
						if (t < 0)
						{
							t = h[i];
							if (next[j] != n - 1)
							{
								int dy = h[next[i]] - h[i];
								int dx = next[i] - i;
								int dy1 = (dy * (i - j) + dx - 1) / dx;
								t = h[i] - dy1;
							}
						}
						else
						{
							--t;
						}
						h[j] = t;
						if (t < 0)
							res = false;
					}
				}
			}
			/*
			for (int i = n - 2 ; res && i >= 0 ; --i)
			{
				h[i] = h[i + 1] - 1024;
				if (next[i] == i + 1)
					;
				else if (next[i] == n - 1)
					++h[i];
				else
				{
					int dy = (h[next[next[i]]] - h[next[i]]);
					int dx = (next[next[i]] - next[i]);
					int dy1 = dy * (next[i] - i) / dx;
					h[i] = h[next[i]] - dy1;
				}
				int dy = (h[next[i]] - h[i]);
				int dx = (next[i] - i);
				for (int j = i + 1 ; res && j < next[i] ; ++j)
				{
					if (dx * (h[j] - h[i]) >= (j - i) * dy)
						res = false;
				}
				if (h[i] < 0)
					res = false;
			}
			*/
		}
		std::cout << "Case #" << t << ":";
		if (res)
			for (int i = 0 ; i < n ; ++i)
				std::cout << " " << h[i];
		else
			std::cout << " Impossible";
		std::cout << "\n";
	}
	return 0;
}

