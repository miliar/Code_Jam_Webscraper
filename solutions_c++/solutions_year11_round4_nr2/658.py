#include <string>
#include <iostream>

using std::string;

int board[500][500];

bool check(const int& bi, const int& bj, const int& size)
{
	long long xbal = 0;
	long long ybal = 0;
	
	int midi = bi * 2 + size;
	int midj = bj * 2 + size;
	
	for (int i = bi; i < bi+size; i++)
		for (int j = bj; j < bj+size; j++)
		{
			if ((i == bi && j == bj) || (i == bi+size-1 && j == bj) || (i == bi && j == bj+size-1) || (i == bi+size-1 && j == bj+size-1)) continue;
			xbal += (midi - (i*2) - 1) * board[i][j];
			ybal += (midj - (j*2) - 1) * board[i][j];
		}
		
	return xbal == 0 && ybal == 0;
}

int main()
{
	int ntests;
	std::cin >> ntests;
	for (int ctest = 1; ctest <= ntests; ctest++)
	{
		int r, c, d;
		std::cin >> r >> c >> d;
		
		for (int i = 0; i < r; i++)
		{
			string line;
			std::cin >> line;
			for (int j = 0; j < c; j++)
				board[i][j] = d + line[j] - '0';
		}
		
		int max = 0;
		
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
				for (int sz = (max == 0 ? 3 : max+1); sz + i <= r && sz + j <= c; sz++)
					if (check(i, j, sz))
						max = sz;
		
		if (max > 0)
			std::cout << "Case #" << ctest << ": " << max << "\n";
		else std::cout << "Case #" << ctest << ": " << "IMPOSSIBLE" << "\n";
	}
	
	return 0;
}
