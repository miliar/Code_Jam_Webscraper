#include <iostream>
#include <fstream>
#include <set>
#include <utility>
#include <algorithm>


int cycle(int a, int front) {
	return (a % 10) * front + a / 10;
}

int digitCount(int a) {
	int c = 1;
	
	while (a / 10) { a /= 10; c *= 10; }
	
	return c;
}

int main(void) {
	int count, s, e, t, dc;
	std::set< std::pair<int,int> > found;
	std::ofstream fout("recycleNumbers.txt");
	std::ofstream fout2("where.txt");

	std::cin >> count;

	for (int i = 0; i < count; ++i) {
		std::cin >> s >> e;
		dc = digitCount(s);
		found.clear();
		for (int j = s; j <= e; ++j) {
			fout2 << j << std::endl;
			t = cycle(j, dc);

			for (int k = 1; k < dc; k *= 10) {
				if (t >= s && e >= t && j != t) {
					fout2 << "\t" << t << std::endl;
					found.insert(std::make_pair(std::min(j, t), std::max(j, t)));
				}
				t = cycle(t, dc);
			}
		}
		fout << "Case #" << (i + 1) << ": " << (int)found.size() << std::endl;
	}

	return 0;
}
