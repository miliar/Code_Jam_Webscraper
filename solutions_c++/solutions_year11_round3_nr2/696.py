// b.exe < int.txt > out.txt

#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <list>
#include <map>
#include <set>

/*
Each contains integers, L, t, N and C, followed by C integers ai, all separated by spaces.
ai is the number of parsecs between star k*C+i and star k*C+i+1, for all integer values of k.
For example, with N=8, C=3, a0=3, a1=5 and a2=4, the distances between stars are [3, 5, 4, 3, 5, 4, 3, 5]. 
*/

int main(int argc, char* argv[])
{
#define int __int64
	int num_of_cases;
	std::cin >> num_of_cases;
	for (int case_num = 1; case_num <= num_of_cases; ++case_num) {
		int boosters, build_time, stars_plus_one, period;
		std::cin >> boosters >> build_time >> stars_plus_one >> period;
		std::vector<int> sh_dists(period);
		for (int i = 0; i != period; ++i) {
			std::cin >> sh_dists[i];
		}
		std::vector<int> dists_x2(stars_plus_one);
		int total_dist_x2 = 0;
		for (int i = 0; i != stars_plus_one; ++i) {
			dists_x2[i] = sh_dists[i % period] * 2;
			total_dist_x2 += dists_x2[i];
		}
		int big_dist_x2 = 0;
		int time_so_far = 0;
		for (int i = 0; i != stars_plus_one; ++i) {
			if (time_so_far >= build_time) {
__LBL:
				std::list<int> left_dists_x2;
				for (int j = i; j != stars_plus_one; ++j)
					left_dists_x2.push_back(dists_x2[j]);
				left_dists_x2.push_back(time_so_far - build_time);
				left_dists_x2.sort();
				left_dists_x2.reverse();
				std::list<int>::iterator it = left_dists_x2.begin();
				for (int j = 0; j != boosters; ++j) {
					if (it == left_dists_x2.end())
						break;
					big_dist_x2 += *it;
					++it;
				}
				break;
			}
			time_so_far += dists_x2[i];
			if (i == stars_plus_one - 1 && time_so_far >= build_time) {
				++i;
				goto __LBL;
			}
		}
		int total_time = total_dist_x2 - (big_dist_x2 / 2);

		std::cout << "Case #" << case_num << ": " << total_time << std::endl;
	}
	return 0;
}

