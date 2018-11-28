#include <iostream>
#include <vector>
#include <cmath>

typedef long long int lli;


lli solve_small_int(lli p, lli players, std::vector<lli>& misses, lli from, lli to)
{
	assert(players == to - from + 1);
	//std::cout << "to:" << to << " from:" << from << std::endl;
	if (to - from == 0) return 0;
	lli min = p;
	for (lli i = from; i <= to; i++) {
		if (misses[i] < min) min = misses[i];
	}
	if (min >= p) return 0;
	//std::cout << "+1" <<std::endl;
	return (1 + solve_small_int(p-1, players/2, misses, from+0, from+(players/2)-1) + solve_small_int(p-1, players/2, misses, from+players/2, from+players-1));
}

lli solve_small(lli p, std::vector<lli>& misses)
{
	lli players = 1;
	for (lli i = 0; i < p; i++) {
		players *= 2;
	}
	assert(players == misses.size());
	return solve_small_int(p, players, misses, 0, players-1);
}

int main()
{
	lli t;
	std::cin >> t;
	for (lli i = 1; i <= t; i++) {
		lli p;
		std::cin >> p;
		lli players = 1;
		for (lli j = 0; j < p; j++) {
			players *= 2;
		}
		std::vector<lli> misses;
		for (lli j = 0; j < players; j++) {
			lli miss;
			std::cin >> miss;
			misses.push_back(miss);
		}
		std::vector<std::vector<lli> > costs_all;
		do {
			players /= 2;
			std::vector<lli> costs;
			for (lli j = 0; j < players; j++) {
				lli cost;
				std::cin >> cost;
				costs.push_back(cost);
			}
			costs_all.push_back(costs);
		} while (players > 1);
		
		std::cout << "Case #" << i << ": " << solve_small(p, misses) << std::endl;
	}
	return 0;
}
	
