#include <algorithm>
#include <iostream>
#include <vector>

typedef unsigned long long UInt64;

UInt64 calc_sub(UInt64 x, UInt64 y)
{
	if (x < y)
		std::swap(x, y);
	if (y == 0)
		return x;

//	std::cerr << "x: " << x << ", y: " << y << std::endl;
	for (UInt64 mod = x % y; mod != 0; mod = x % y)
	{
		x = y;
		y = mod;
	}
	return y;
}

UInt64 calc(const std::vector<UInt64> &events)
{
	std::vector<UInt64> sorted_events(events);
	std::sort(sorted_events.begin(), sorted_events.end());

	std::vector<UInt64> diffs(events.size() - 1);
	for (std::size_t i = 0; i < diffs.size(); ++i)
		diffs[i] = sorted_events[i + 1] - sorted_events[i];

//	std::cerr << "diffs: ";
//	for (std::size_t i = 0; i < diffs.size(); ++i)
//		std::cerr << ' ' << diffs[i];
//	std::cerr << std::endl;

	UInt64 max_value = diffs[0];
	for (std::size_t i = 1; i < diffs.size(); ++i)
		max_value = calc_sub(max_value, diffs[i]);
	std::cerr << "max. value: " << max_value << std::endl;

	UInt64 mod = events[0] % max_value;
	return (mod == 0) ? 0 : (max_value - mod);
}

int main()
{
	int num_cases;
	std::cin >> num_cases;

	for (int i = 0; i < num_cases; ++i)
	{
		int num_events;
		std::cin >> num_events;
		std::cerr << num_events << ':';

		std::vector<UInt64> events(num_events);
		for (int j = 0; j < num_events; ++j)
		{
			std::cin >> events[j];
			std::cerr << ' ' << events[j];
		}
		std::cerr << std::endl;

		std::cout << "Case #" << (i + 1) << ": " << calc(events) << std::endl;
	}

	return 0;
}
