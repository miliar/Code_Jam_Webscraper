#include <fstream>
#include <string>
#include <iostream>
#include <queue>

int main(int argc, char **argv)
{
	std::ifstream file("C-small-attempt0.in");
	std::ofstream out("out.txt");

	while (!file.eof()) {
		unsigned long tests = 0;
		file >> tests;

		unsigned long r, k, n, d = 0;
		for (int i = 0; i < tests; i++) {
			file >> r >> k >> n;
			std::deque<unsigned long> g;
			for (unsigned long j = 0; j < n; j++) {
				unsigned long gi;
				file >> gi;
				g.push_back(gi);
			}

			unsigned long total = 0, at = 0;
			std::deque<unsigned long> temp;
			std::deque<unsigned long>::const_iterator dit;
			for (unsigned long l = 0; l < r; l++) {
				for (dit = g.begin(); dit != g.end(); ++dit) {
					if ((total + *dit) > k) {
						break;
					} else {
						total += *dit;
						d += *dit;
						temp.push_back(*dit);
						at++;
					}
				}
				for (unsigned long m = (n - 1); m >= at; m--) {
					temp.push_front(g.at(m));
				}
				at = 0;
				total = 0;
				g = temp;
				temp.clear();
			}

			out << "Case #" << i + 1 << ": " << d << std::endl;
			d = 0;
		}
	}

	out.close();
}