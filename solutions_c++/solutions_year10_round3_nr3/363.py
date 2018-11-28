#include <iostream>


int main ()
{
	int	numberOfCases	= 0;
	int	counter			= 0;
	
	std::cin >> numberOfCases;
	
	while (counter < numberOfCases) {
		int m		= 0;
		int n		= 0;

		std::cin >> m;
		std::cin >> n;

		int		board[m][n];
		int		result[n];
		memset (result, 0, sizeof(int)*n);

		for (int i = 0; i < m; ++i) {
			int nextIndex = 0;
				std::string  input;
				std::cin >> input;
			if (input.length () == 1 && (input == "1" ||input == "0")) {
					if (input == "1")
						for (int ll = 0; ll < n; ++ll)
							board[i][ll] = 1;
					else
						for (int ll = 0; ll < n; ++ll)
							board[i][ll] = 0;
				} else {
				for (int kk = 0; kk < input.length (); ++kk) {
					switch (input[kk]) {
						case '0':
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 0;
							break;
						case '1':
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 1;
							break;
						case '2':
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 0;
							break;
						case '3':
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 1;
							break;
						case '4':
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 0;
							break;
						case '5':
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 1;
							break;
						case '6':
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 0;
							break;
						case '7':
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 1;
							break;
						case '8':
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 0;
							break;
						case '9':
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 1;
							break;
						case 'A':
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 0;
							break;
						case 'B':
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 1;
							break;
						case 'C':
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 0;
							break;
						case 'D':
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 0;
							board[i][nextIndex++] = 1;
							break;
						case 'E':
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 0;
							break;
						case 'F':
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 1;
							board[i][nextIndex++] = 1;
							break;
					}
				}
			}
		}

		// Making squares
		for (int i = 0; i < m; ++i) {
			for (int j = 0; j < n; ++j) {
				int size = 1;
				bool increase = true;
				while (increase) {
					if (i + size >= m || j + size >= n)
						break;

					for (int ii = 0; ii < size; ++ii) {
						if (board[i + ii][j + size - 1] != board[i + ii][j + size])
							continue;

						increase = false;
						break;
					}
					if (board[i + size][j] == board[i + size - 1][j])
						increase = false;
					
					if (!increase)
						break;
					
					for (int jj = 0; jj < size; ++jj) {
						if (board[i + size][j + jj] != board[i + size][j + jj + 1])
							continue;
						
						increase = false;
						break;
					}
					if (!increase)
						break;

					++size;
				}
				board[i][j] = size;
			}
		}

		// Cutting biggest
		bool needed = true;
		while (needed) {
			int posI = -1;
			int posJ = -1;
			int maxValue = -1;
			for (int i = 0; i < m; ++i) {
				for (int j = 0; j < n; ++j) {
					if (board[i][j] <= maxValue)
						continue;

					maxValue = board[i][j];
					posI = i;
					posJ = j;
				}
			}
			if (maxValue == -1)
				break;

			result[maxValue] = result[maxValue] + 1;
			//std::cout << maxValue << " at: " << posI << ", " << posJ << std::endl;

			for (int i = 0; i < maxValue; ++i) {
				for (int j = 0; j < maxValue; ++j) {
					board[posI + i][posJ + j] = -1;
				}
			}

			// Making squares
			for (int i = 0; i < m; ++i) {
				for (int j = 0; j < n; ++j) {
					if (board[i][j] == -1)
						continue;
					int size = 1;
					bool increase = true;
					for (int kk = 1; kk < board[i][j]; ++kk) {
						for (int ii = 0; ii < size; ++ii) {
							if (board[i + ii][j + size] != -1)
								continue;
							
							increase = false;
							break;
						}
						if (board[i + size][j] == -1)
							increase = false;
						
						if (!increase)
							break;
						
						for (int jj = 0; jj < size; ++jj) {
							if (board[i + size][j + jj + 1] != -1)
								continue;
							
							increase = false;
							break;
						}
						if (!increase)
							break;
						
						++size;
					}
					board[i][j] = size;
				}
			}
		}

		int difference = 0;

		for (int i = 0; i < n; ++i) {
			if (result[i] != 0)
				++difference;
		}
		
		std::cout << "Case #" << ++counter << ": " << difference << std::endl;

		for (int i = n-1; i >= 0; --i) {
			if (result[i] == 0)
				continue;

			std::cout << i << " " << result[i] << std::endl;
		}
	}
}