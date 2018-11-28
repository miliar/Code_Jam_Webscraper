// c.exe < int.txt > out.txt

#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <list>
#include <map>
#include <set>

/*
The first line of the input gives the number of test cases, T.
T test cases follow.
Each test case is described by two lines.
The first contains three numbers: N, L and H, denoting the number of other players, the lowest and the highest note Jeff's instrument can play.
The second line contains N integers denoting the frequencies of notes played by the other players.
*/

int main(int argc, char* argv[])
{
	int num_of_cases;
	std::cin >> num_of_cases;
	for (int case_num = 1; case_num <= num_of_cases; ++case_num) {
		__int64 N, L, H;
		std::cin >> N >> L >> H;
		std::vector<__int64> freq(N);
		for (__int64 i = 0; i != N; ++i) {
			std::cin >> freq[i];
		}
		std::sort(freq.begin(), freq.end());
		__int64 f = L;
		bool ok;
		for (; f <= H; ++f) {
			ok = true;
			std::vector<__int64>::iterator lo_it = std::lower_bound(freq.begin(), freq.end(), f);
			std::vector<__int64>::iterator up_it = std::upper_bound(freq.begin(), freq.end(), f);

			for (__int64 j = lo_it - freq.begin(); j > 0; --j) {
				if (f % freq[j - 1] != 0) {
					ok = false;
				}
			}
			for (std::vector<__int64>::iterator jt = up_it; ok && jt != freq.end(); ++jt) {
				if (*jt % f != 0) {
					ok = false;
				}
			}
			if (ok)
				break;
		}
		if (ok) {
			std::cout << "Case #" << case_num << ": " << f << std::endl;
		}
		else {
			std::cout << "Case #" << case_num << ": NO" << std::endl;
		}
	}
	return 0;
}

