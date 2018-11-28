#include <iostream>
#include <map>

typedef std::map<int, int> M;

int f(int x)
{
	int len = 0;
	int mul = 1;
	int t = x;
	while (t > 0)
	{
		++len;
		mul *= 10;
		t /= 10;
	}
	mul /= 10;
	int min = x;
	for (int i = 0 ; i < len ; ++i)
	{
		x = x / 10 + mul * (x % 10);
		if (x / mul && min > x)
			min = x;
	}
	return min;
}

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
		M m;
		int a, b;
		std::cin >> a >> b;
		for (int i = a ; i <= b ; ++i)
		{
			++m[f(i)];
		}
		long long r = 0;
		for (M::iterator i = m.begin() ; i != m.end() ; ++i)
		{
			r += (long long)i->second * (i->second - 1) / 2LL;
		}
		std::cout << "Case #" << t << ": " << r << "\n";
	}
	return 0;
}

