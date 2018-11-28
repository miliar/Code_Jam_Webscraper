#include <iostream>
#include <vector>
#include <queue>

long long calc(int times, int size, const std::vector<int> &groups)
{
	std::queue<int> queue;
	for (std::size_t i = 0; i < groups.size(); ++i)
		queue.push(groups[i]);

	long long total = 0;
	for (int i = 0; i < times; ++i)
	{
		int avail = size;
		for (std::size_t j = 0; j < groups.size(); ++j)
		{
			if (queue.front() > avail)
				break;
			avail -= queue.front();
			queue.push(queue.front());
			queue.pop();
		}
		total += size - avail;
	}

	return total;
}

int main()
{
	int num_cases;
	std::cin >> num_cases;

	for (int i = 0; i < num_cases; ++i)
	{
		int times, size, num_groups;
		std::cin >> times >> size >> num_groups;
		std::cerr << "times: " << times << ", size: " << size
			<< ", groups: " << num_groups << std::endl;

		std::vector<int> groups(num_groups);
		for (int j = 0; j < num_groups; ++j)
			std::cin >> groups[j];

		std::cout << "Case #" << (i + 1) << ": "
			<< calc(times, size, groups) << std::endl;
	}

	return 0;
}
