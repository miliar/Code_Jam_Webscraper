#include <iostream>
#include <vector>

#define CHARS 26

int main() {
	int T;
	std::cin >> T;
	for (int t = 0; t < T; ++t) {
		int C;
		std::cin >> C;
		bool can_combine[CHARS][CHARS] = {{false}};
		int combination[CHARS][CHARS];
		for (int c = 0; c < C; ++c) {
			char c;
			std::cin >> c;
			int b1 = c - 'A';
			std::cin >> c;
			int b2 = c - 'A';
			std::cin >> c;
			int e = c - 'A';
			can_combine[b1][b2] = true;
			can_combine[b2][b1] = true;
			combination[b1][b2] = e;
			combination[b2][b1] = e;
		}
		int D;
		std::cin >> D;
		bool opposed[CHARS][CHARS] = {{false}};
		for (int d = 0; d < D; ++d) {
			char c;
			std::cin >> c;
			int b1 = c - 'A';
			std::cin >> c;
			int b2 = c - 'A';
			opposed[b1][b2] = true;
			opposed[b2][b1] = true;
		}
		int N;
		std::cin >> N;
		std::vector<int> invocations(N);
		for (int i = 0; i < N; ++i) {
			char c;
			std::cin >> c;
			invocations[i] = c - 'A';
		}
		std::vector<int> stack;
		for (int n = 0; n < N; ++n) {
			//std::cout << "[";
			//for (int i = 0; i < static_cast<int>(stack.size()); ++i) {
			//	if (i > 0) {
			//		std::cout << ", ";
			//	}
			//	std::cout << static_cast<char>(stack[i] + 'A');
			//}
			//std::cout << "]" << std::endl;
			int element = invocations[n];
			stack.push_back(element);
			int size = stack.size();
			if (size >= 2 && can_combine[stack[size - 2]][stack[size - 1]]) {
				int new_element = combination[stack[size - 2]][stack[size - 1]];
				//std::cerr << stack[size - 2] << " + " << stack[size - 1] << " -> " << new_element << std::endl;
				stack.pop_back();
				stack.pop_back();
				stack.push_back(new_element);
			}
			else {
				for (int i = 0; i < size - 1; ++i) {
					if (opposed[stack[i]][stack[size - 1]]) {
						stack.clear();
						break;
					}
				}
			}
		}
		std::cout << "Case #" << (t + 1) << ": [";
		for (int i = 0; i < static_cast<int>(stack.size()); ++i) {
			if (i > 0) {
				std::cout << ", ";
			}
			std::cout << static_cast<char>(stack[i] + 'A');
		}
		std::cout << "]" << std::endl;
	}
}
