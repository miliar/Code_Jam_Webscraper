#include <iostream>
#include <algorithm>
#include <string>

bool empty(char c) {
	return c == '.';
}

int N;
int K;
char board[55][55];

void iterate(int row, int col, int dr, int dc, bool & red, bool & blue) {
	int len = 0;
	char c = board[row][col];
	while (row < N && col < N) {
		if (board[row][col] != c) {
			c = board[row][col];
			len = 1;
		} else {
			len++;
		}
		if (len == K) {
			if (c == 'R') red = true;
			if (c == 'B') blue = true;
		}
		row += dr;
		col += dc;
	}
}


int main(int argc, char * argv[])
{
	int T;
	std::cin >> T;

	for (int t = 1; t <= T; t++) {
		std::cin >> N >> K;
		std::string line;
		std::getline(std::cin, line);
		for (int l = 0; l < N; l++) {
			std::getline(std::cin, line);
			
			line.erase( remove_if(line.begin(), line.end(), empty), line.end() );

			for (int c = 0; c < 51; c++) board[l][c] = '.';
			for (int c = 0; c < line.length(); c++) board[l][N-line.length()+c] = line[c];
		}

		bool red = false;
		bool blue = false;
		for (int row = 0; row < N; row++) {
			iterate(row, 0, 0, 1, red, blue);
			iterate(0, row, 1, 0, red, blue);
			iterate(row, 0, 1, 1, red, blue);
			iterate(0, row, 1, 1, red, blue);
			iterate(N-1, row, -1, 1, red, blue);
			iterate(row, N-1, 1, -1, red, blue);
		}
		std::cout << "Case #" << t << ": ";
		if (red && blue) std::cout << "Both";
		if (red && !blue) std::cout << "Red";
		if (!red && blue) std::cout << "Blue";
		if (!red && !blue) std::cout << "Neither";
		std::cout << "\n";
	}

	return 0;
}

