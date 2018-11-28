#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	std::fstream fin(argv[1]);
	if (!fin.is_open()) return 1;

	int T, N;
	fin >> T;

	for (int t=0; t<T; t++) {
		std::vector<std::string> games;

		fin >> N;
		for (int n=0; n<N; n++) {
			std::string s;
			fin >> s;
			games.push_back(s);
		}

		std::vector<int> wp_n_list;
		std::vector<int> wp_d_list;
		for (int n=0; n<N; n++) {
			int wp_n = 0;
			int wp_d = 0;
			const std::string& s = games[n];
			for (size_t i=0; i<s.length(); i++) {
				if (s[i]=='1') wp_n++;
				if (s[i]!='.') wp_d++;
			}
			wp_n_list.push_back(wp_n);
			wp_d_list.push_back(wp_d);
		}

		std::vector<double> owp_list;
		for (int n=0; n<N; n++) {
			double owp_n = 0;
			int owp_d = 0;
			const std::string& s = games[n];
			for (size_t i=0; i<s.length(); i++) {
				if (s[i]!='.') {
					int x = wp_n_list[i];
					if (games[i][n]=='1') x--;
					owp_n += (double) x / (wp_d_list[i] - 1);
					owp_d++;
				}
			}
			if (owp_d)
				owp_list.push_back(owp_n / owp_d);
			else
				owp_list.push_back(0);
		}

		std::vector<double> oowp_list;
		for (int n=0; n<N; n++) {
			double oowp_n = 0;
			int oowp_d = 0;
			const std::string& s = games[n];
			for (size_t i=0; i<s.length(); i++) {
				if (i!=n && s[i]!='.') {
					oowp_n += owp_list[i];
					oowp_d++;
				}
			}
			if (oowp_d)
				oowp_list.push_back(oowp_n / oowp_d);
			else
				oowp_list.push_back(0);
		}

		std::cout << "Case #" << (t + 1) << ":" << "\n";
		for (int n=0; n<N; n++) {
			double rpi = 0.25 * wp_n_list[n] / wp_d_list[n] + 0.50 * owp_list[n] + 0.25 * oowp_list[n];
			std::cout << rpi << "\n";
		}
	}
}
