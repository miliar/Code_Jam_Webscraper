#include <fstream>
#include <iostream>
#include <deque>
#include <stdlib.h>


int main(int argc, char* argv[])
{
	std::fstream fin(argv[1]);
	if (!fin.is_open()) return 1;

	int T;
	fin >> T;

	for (int t=0; t<T; t++) {
		int N;
		fin >> N;
		
		std::deque<int> r_list;
		std::deque<int> p_list[2];
		for (int n=0; n<N; n++) {
			char R;
			int P;
			fin >> R >> P;
			int r = R == 'O' ? 0 : 1;
			r_list.push_back(r);
			p_list[r].push_back(P);
		}

		int result=0;
		int pos[2] = {1, 1};
		while (!r_list.empty()) {
			int r = r_list.front();
			int s = 1 - r;
			int r_dist = p_list[r].front() - pos[r];
			if (r_dist == 0) {
				result++;

				if (!p_list[s].empty()) {
					int s_dist = p_list[s].front() - pos[s];
					if (s_dist) pos[s] += s_dist / abs(s_dist);
				}

				r_list.pop_front();
				p_list[r].pop_front();
			} else {
				result += abs(r_dist);

				pos[r] = p_list[r].front();

				if (!p_list[s].empty()) {
					int s_dist = p_list[s].front() - pos[s];
					if (s_dist) {
						pos[s] += std::min(abs(r_dist), abs(s_dist)) * (s_dist / abs(s_dist));
					}
				}
			}
		}

		std::cout << "Case #" << t + 1 << ": " << result << std::endl;
	}
	
}
