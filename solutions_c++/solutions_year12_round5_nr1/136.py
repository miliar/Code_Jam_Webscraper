#include <fstream>
#include <iostream>
#include <exception>
#include <string>
#include <utility>
#include <algorithm>
#include <vector>

void run(std::ifstream &fi, std::ofstream &fo) {
	int N;
	fi >> N;
	std::vector<std::pair<int, int> > v(N);
	for (int i=0; i<N; i++)
		fi >> v[i].first;
	for (int i=0; i<N; i++) {
		fi >> v[i].first;
		v[i].first = - v[i].first;
		v[i].second = i;
	}
	std::sort(v.begin(), v.end());
	for (int i=0; i<N; i++)
		fo << ' ' << v[i].second;
}

int main(int argc, const char **argv) {
	try {
		unsigned int T;
		std::string inFilename(argc<=1 ? "in" : argv[1]);
		std::string outFilename = inFilename + ".out";
		std::ifstream fi(inFilename);
		fi.exceptions(std::ios::badbit | std::ios::failbit);
		std::ofstream fo(outFilename);
		fo.exceptions(std::ios::badbit | std::ios::failbit);
		fi >> T;
		for (unsigned int t=1; t<=T; t++) {
			fo << "Case #" << t << ":";
			run(fi, fo);
			fo << std::endl;
			std::cout << '\r' << t << '/' << T; std::cout.flush();
		}
		std::cout << std::endl;
	} catch (const std::exception &ex) {
		std::cerr << "\nexception: " << ex.what() << std::endl;
	} catch (...) {
		std::cerr << "\nwhoops\n";
	}
	return 0;
}
