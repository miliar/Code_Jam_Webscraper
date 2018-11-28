#include <iostream>

bool world_is_empty(int world[110][110]) {
	for (int row = 0; row < 110; ++row) {
		for (int col = 0; col < 110; ++col) {
			if (world[row][col]) return false;
		}
	}
	return true;
}

int main() {
	int nCases;
	std::cin >> nCases;
	for (int c = 0; c < nCases; ++c) {
		int nRects;
		int left[10000], right[10000], top[10000], bottom[10000];
		int world[110][110] = {{0}};
		std::cin >> nRects;
		for (int i = 0; i < nRects; ++i) {
			std::cin >> left[i];
			std::cin >> top[i];
			std::cin >> right[i];
			std::cin >> bottom[i];
			for (int row = top[i]; row <= bottom[i]; ++row) {
				for (int col = left[i]; col <= right[i]; ++col) {
					world[row][col] = 1;
				}
			}
		}
		int seconds;
		for (seconds = 0; !world_is_empty(world); ++seconds) {
			for (int row = 1; row < 109; ++row) {
				for (int col = 1; col < 109; ++col) {
					if (world[row - 1][col] <= 0 &&
					    world[row][col - 1] <= 0 &&
					    world[row][col] == 1)
					{
						world[row][col] = 2;
					}
					if (world[row - 1][col] > 0 &&
					    world[row][col - 1] > 0 &&
					    world[row][col] != 1)
					{
						world[row][col] = -1;
					}
				}
			}
			for (int row = 0; row < 110; ++row) {
				for (int col = 0; col < 110; ++col) {
					if (world[row][col] == -1) world[row][col] = 1;
					else if (world[row][col] == 2) world[row][col] = 0;
				}
			}
		}
		std::cout << "Case #" << (c + 1) << ": " << seconds << std::endl;
	}
}
