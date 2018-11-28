#include <iostream>
#include <vector>

int solve(int S, int p, const std::vector<int>& V) {
	int min = p + p-1 + p-1;
	if (p == 0) min = 0;
	if (p == 1) min = 1;
	int mins = min - 2;
	if (p == 0) mins = 0;
	if (p == 1) mins = 1;
	int out = 0;
	for (int x : V) {
		if (x >= min) {
			++out;
		}
		else if (x >= mins && S > 0) {
			++out;
			--S;
		}
	}
	return out;
}

int main() {
	int T;
	std::cin >> T;
	for (int t = 0; t < T; ++t) {
		int N;
		int S;
		int p;
		std::cin >> N >> S >> p;
		std::vector<int> V(N);
		for (int i = 0; i < N; ++i) {
			std::cin >> V[i];
		}
		std::cout << "Case #" << (t + 1) << ": " << solve(S, p, V) << std::endl;
	}
}
