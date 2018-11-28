#include <iostream>
#include <algorithm>

int r(int score) {
	return std::min(std::max(score, 0), 10);
}

int main() {
	int T;
	std::cin >> T;
	for (int t=1; t<=T; t++) {
		int N, S, p;
		std::cin >> N >> S >> p;
		int sum = 2*r(p-1) + r(p);
		int ssum = 2*r(p-2) + r(p);
		int count = 0, scount = 0;
		for (int i=0; i<N; i++) {
			int x;
			std::cin >> x;
			if (x>=sum) count++;
			else if (x>=ssum) scount++;
		}
		std::cout << "Case #" << t << ": " << (count + std::min(scount,S)) << std::endl;
	}
}

