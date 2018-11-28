#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<iterator>
#include<algorithm>
#include<functional>

class Googlers;

class Googlers{
public:
	/*
	mod 3
	0 single
	0 0 0
	1 single
	0 0 1
	2
	0 0 2 *
	0 1 1
	3
	0 1 2 *
	1 1 1
	4 same
	0 2 2 *
	1 1 2
	5
	1 1 3 *
	1 2 2
	6
	1 2 3 *
	2 2 2
	7 same
	1 3 3 *
	2 2 3
	...
	
	27
	8 9 10 *
	9 9 9
	28
	8 10 10 *
	9 9 10
	29 single
	9 10 10
	30 single
	10 10 10
	*/
	// if n = 1 mod 3, same score
	Googlers() {
		return;
	}
	int calc_best(int score) {
		if(score == 0) {
			return 0;
		}else if(score == 1) {
			return 1;
		}else if(score == 30) {
			return 10;
		}else if(score == 29) {
			return 10;
		}
		return (score + 1) / 3 + 1;
	}
	int calc_ordinary_max(int score) {
		if(score == 0) {
			return 0;
		}else if(score == 1) {
			return 1;
		}else if(score == 30) {
			return 10;
		}else if(score == 29) {
			return 10;
		}
		return (score - 1) / 3 + 1;
	}
	int solve(int num_googlers, int num_surprising_triplets, int p, std::vector<int> n) {
		// std::sort(n.begin(), n.end(), std::greater<int>());
		typedef std::map<int, int, std::greater<int> > score_map_type;
		score_map_type score_map;
		int num_surprising_triplets_remain = num_surprising_triplets, best, ordinary;
		int ans = 0;
		
		for(int i = 0; i < num_googlers; ++i) {
			score_map[n[i]]++;
		}
		
		for(score_map_type::iterator it = score_map.begin(); it != score_map.end(); ++it) {
			best = calc_best(it->first);
			ordinary = calc_ordinary_max(it->first);
			if(ordinary >= p) {
				ans += it->second;
			}else if(best >= p) {
				if(num_surprising_triplets_remain > 0) {
					if(num_surprising_triplets_remain > it->second) {
						ans += it->second;
						num_surprising_triplets_remain -= it->second;
					}else{
						ans += num_surprising_triplets_remain;
						num_surprising_triplets_remain = 0;
						return ans;
					}
				}else{
					return ans;
				}
			}
		}
		return ans;
	}
};

int main(void) {
	int n_probs = 0;
	std::string str_problem;
	Googlers solver;
	
	std::cin >> n_probs;
	std::vector<int> n;
	
	for(int i = 0; i < n_probs; ++i) {
		int num_googlers, num_surprising_triplets, p;
		int ans;
		
		std::cin >> num_googlers >> num_surprising_triplets >> p;
		// std::cout << num_googlers << num_surprising_triplets << p;;
		n.resize(num_googlers);
		for(int j = 0; j < num_googlers; ++j) {
			std::cin >> n[j];
			// std::cout << n[j];
		}
		// std::cout << std::endl;
		ans = solver.solve(num_googlers, num_surprising_triplets, p, n);
		std::cout << "Case #" << (i + 1) << ": ";
		std::cout << ans << std::endl;
	}
	
	return 0;
}

