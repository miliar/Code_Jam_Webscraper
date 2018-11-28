#include <iostream>
#include <algorithm>
#include <vector>

struct L
{
	int t, p, i;
	bool operator<(const L&lev) const
	{
		return (p > lev.p) || (p > 0 && p == lev.p && t < lev.t) || (p == 0 && lev.p == 0 && i < lev.i) || (p == lev.p && t == lev.t && i < lev.i);
	}
};

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
		int n;
		std::cin >> n;
		std::vector<L> v(n);
		for (int i = 0 ; i < n ; ++i)
		{
			std::cin >> v[i].t;
			v[i].i = i;
		}
		for (int i = 0 ; i < n ; ++i)
			std::cin >> v[i].p;
		std::sort(v.begin(), v.end());
		std::cout << "Case #" << t << ":";
		for (int i = 0 ; i < n ; ++i)
			std::cout << " " << v[i].i;
		std::cout << "\n";
	}
	return 0;
}

