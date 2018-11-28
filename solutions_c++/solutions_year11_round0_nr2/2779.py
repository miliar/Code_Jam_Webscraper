#include <fstream>
#include <iostream>
#include <deque>
#include <string>
#include <stdlib.h>


int main(int argc, char* argv[])
{
	std::fstream fin(argv[1]);
	if (!fin.is_open()) return 1;

	int T;
	fin >> T;

	for (int t=0; t<T; t++) {
		std::string result;
		std::string cs_b, cs_e, cs_r, ds_b, ds_e;
		std::string s;

		int C=0, D=0, N=0;
		fin >> C;
		for (int j=0; j<C; j++) {
			fin >> s;
			cs_b += s[0];
			cs_b += s[1];
			cs_e += s[1];
			cs_e += s[0];
			cs_r += s[2];
			cs_r += s[2];
		}
		fin >> D;
		for (int j=0; j<D; j++) {
			fin >> s;
			ds_b += s[0];
			ds_b += s[1];
			ds_e += s[1];
			ds_e += s[0];
		}
		fin >> N;
		if (N) {
			fin >> result;
		}

		for (size_t i=0; i<result.length(); ) {
			if (i>0) {
				// combine
				bool combined = false;
				for (size_t cs = 0; (cs = cs_e.find(result[i], cs)) != std::string::npos; cs++) {
					if (result[i - 1] == cs_b[cs]) {
						result.replace(i-1, 2, 1, cs_r[cs]);
						combined = true;
						break;
					}
				}
				if (combined) continue;

				// opposed
				std::string candidate;
				for (size_t ds = 0; (ds = ds_e.find(result[i], ds)) != std::string::npos; ds++) {
					candidate += ds_b[ds];
				}
				bool opposed = false;
				if (!candidate.empty()) {
					for (size_t j=0; j<i; j++) {
						const int pos = candidate.find(result[j]);
						if (pos != std::string::npos) {
							result.erase(0, i+1);
							i = 0;
							opposed = true;
							break;
						}
					}
				}
				if (opposed) continue;

				i++;
			} else {
				i++;
			}
		}

		std::cout << "Case #" << t + 1 << ": [";
		if (!result.empty()) {
			for (size_t j=0; j<result.length() - 1; j++) {
				std::cout << result[j] << ", ";
			}
			std::cout << result[result.length() - 1];
		}
		std::cout << "]" << std::endl;
	}	
}
