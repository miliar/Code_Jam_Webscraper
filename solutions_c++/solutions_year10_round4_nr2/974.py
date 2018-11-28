#include <iostream>
#include <utility>
#include <assert.h>
#include <list>


int main() {
	int nCases;
	std::cin >> nCases;
	for (int c = 0; c < nCases; ++c) {
		int nExp;
		std::cin >> nExp;
		int misses[8192];
		const int teams = (1 << nExp);
		for (int i = 0; i < teams; ++i) {
			std::cin >> misses[i];
		}
		for (int i = 0; i < teams - 1; ++i) {
			int dummy;
			std::cin >> dummy;
			assert(dummy == 1);
		}
		std::list< std::pair<int, int> > l; // rank and ticket
		std::list< std::pair<int, int> >::iterator it;
		l.push_back(std::make_pair(1, 0));
		int ticket_count = 0;
		while (1) {
			if (c == 2) {
				int x = 12345;
			}
			int best_score = -123123;
			std::list< std::pair<int, int> >::iterator bestit;
			for (it = l.begin(); it != l.end(); ++it) {
				const int length = teams >> (it->first - 1);
				const int start = it->second * length;
				int score = 0;
				for (int i = start; i < start + length; ++i)
					if (misses[i] < nExp) ++score;
				if (score > best_score) {
					bestit = it;
					best_score = score;
				}
			}
			std::cerr << "best_score is " << best_score << std::endl;
			if (best_score <= 0) break;
			std::pair<int, int> winning_pair = *bestit;
			{	
				const int length = teams >> (bestit->first - 1);
				const int start = bestit->second * length;
				for (int i = start; i < start + length; ++i) ++misses[i];
			}
			l.erase(bestit);
			if (winning_pair.first < nExp) {
				l.push_back(std::make_pair(winning_pair.first + 1,
										   winning_pair.second * 2));
				l.push_back(std::make_pair(winning_pair.first + 1,
										   winning_pair.second * 2 + 1));
			}
			++ticket_count;
		}
		std::cout << "Case #" << (c + 1) << ": " << ticket_count << std::endl;
	}
}
