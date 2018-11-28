#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>

std::vector<int> candies_list;
int N;

int result;
void solve(int index, int s_total, int p_total, int s_real_total, int p_real_total)
{
	if (index == N) {
		if (s_total == p_total && s_real_total && p_real_total && s_real_total > result) {
			result = s_real_total;
		}
		return;
	}

	const int candies = candies_list[index];

	// candies to Sean
	solve(index + 1, s_total ^ candies, p_total, s_real_total + candies, p_real_total);

	// candies to Patrick
	solve(index + 1, s_total, p_total ^ candies, s_real_total, p_real_total + candies);
}

int main(int argc, char* argv[])
{
	std::fstream fin(argv[1]);
	if (!fin.is_open()) return 1;

	int T, C;
	fin >> T;

	for (int t=0; t<T; t++) {
		fin >> N;

		candies_list.clear();
		for (int n=0; n<N; n++) {
			fin >> C;
			candies_list.push_back(C);
		}

		result = -1;
		solve(0, 0, 0, 0, 0);
		if (result == -1) {
			std::cout << "Case #" << t + 1 << ": NO" << std::endl;
		} else {
			std::cout << "Case #" << t + 1 << ": " << result << std::endl;
		}
	}	
}
