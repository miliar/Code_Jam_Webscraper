// a.exe < int.txt > out.txt

#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <list>
#include <map>
#include <set>

int main(int argc, char* argv[])
{
	int num_of_cases;
	std::cin >> num_of_cases;
	for (int case_num = 1; case_num <= num_of_cases; ++case_num) {
		int r, c;
		std::cin >> r >> c;
		std::vector<std::vector<char> > tbl(r, std::vector<char>(c, '.'));
		for (int y = 0; y != r; ++y) {
			for (int x = 0; x != c; ++x) {
				std::cin >> tbl[y][x];
			}
		}
		bool ok = true;
		for (int y = 0; ok && y < r - 1; ++y) {
			for (int x = 0; ok && x < c - 1; ++x) {
				if (tbl[y][x] == '#') {
					if (tbl[y + 1][x] == '#' && tbl[y][x + 1] == '#' && tbl[y + 1][x + 1] == '#') {
						tbl[y][x] = '/';
						tbl[y + 1][x] = '\\';
						tbl[y][x + 1] = '\\';
						tbl[y + 1][x + 1] = '/';
					}
					else {
						ok = false;
					}
				}
			}
		}
		for (int y = 0; ok && y != r; ++y) {
			for (int x = 0; ok && x != c; ++x) {
				ok = (tbl[y][x] != '#');
			}
		}
		if (ok) {
			std::cout << "Case #" << case_num << ":" << std::endl;
			for (int y = 0; y != r; ++y) {
				for (int x = 0; x != c; ++x) {
					std::cout << tbl[y][x];
				}
				std::cout << std::endl;
			}
		}
		else {
			std::cout << "Case #" << case_num << ":" << std::endl << "Impossible" << std::endl;
		}
	}
	return 0;
}

