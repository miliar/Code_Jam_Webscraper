#include <iostream>
#include <vector>

struct group_info {
    int g;
    int next_group;
    int ride_size;
    bool checked;
    group_info()
	: g(0),
	  next_group(0),
	  ride_size(0),
	  checked(false)
    {
    }
};

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
	unsigned R, k, N;
	std::cin >> R >> k >> N;
	std::vector<group_info> group(N);
	for (int n = 0; n < N; ++n)
	    std::cin >> group[n].g;
	int cur = 0;
	while (!group[cur].checked) {
	    group[cur].checked = true;
	    int rem = k - group[cur].g;
	    int next = (cur + 1) % N;
	    while (rem >= group[next].g && next != cur) {
		rem -= group[next].g;
		next = (next + 1) % N;
	    }
	    group[cur].next_group = next;
	    group[cur].ride_size = k - rem;
	    cur = next;
	}
	int cycle_group = cur;
	int cycle_rides = 0;
	long long cycle_total = 0;
	do {
	    ++cycle_rides;
	    cycle_total += group[cur].ride_size;
	    cur = group[cur].next_group;
	} while (cur != cycle_group);

	cur = 0;
	long long total = 0;
	while (R > 0 && cur != cycle_group) {
	    total += group[cur].ride_size;
	    cur = group[cur].next_group;
	    --R;
	}
	int cycles = R / cycle_rides;
	total += cycle_total * cycles;
	R -= cycles * cycle_rides;
	while (R > 0) {
	    total += group[cur].ride_size;
	    cur = group[cur].next_group;
	    --R;
	}
	std::cout << "Case #" << t << ": " << total << std::endl;
    }
}
