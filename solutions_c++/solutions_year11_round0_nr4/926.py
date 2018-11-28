#include <iostream>
#include <vector>

int main() {
	int T;
	std::cin >> T;
	for (int t = 0; t < T; ++t) {
		int N;
		std::cin >> N;
		std::vector<int> P(N);
		for (int n = 0; n < N; ++n) {
			std::cin >> P[n];
			--P[n];
		}
		std::vector<bool> visited(N);
		int sum = 0;
		for (int n = 0; n < N; ++n) {
			if (visited[n]) {
				continue;
			}
			int cycle = 0;
			int x = n;
			while (!visited[x]) {
				visited[x] = true;
				++cycle;
				x = P[x];
			}
			sum += cycle < 2 ? 0 : cycle;
		}
		std::cout << "Case #" << (t + 1) << ": " << sum << std::endl;
	}
}
