#include <string>
#include <vector>
#include <iostream>

using std::string;
using std::vector;

int main()
{
	int tests;
	std::cin >> tests;
	for (int currtest = 1; currtest <= tests; currtest++)
	{
		int m, n;
		std::cin >> m >> n;
		vector<string> board(m);
		for (int i = 0; i < m; i++) std::cin >> board[i];
		
		bool possible = true;
		for (int i = 0; i < m && possible; i++)
			for (int j = 0; j < n && possible; j++)
				if (board[i][j] == '#')
					if (i == m-1 || j == n-1 || board[i+1][j] != '#' || board[i][j+1] != '#' || board[i+1][j+1] != '#')
						possible = false;
					else
					{
						board[i][j] = '/';
						board[i+1][j+1] = '/';
						board[i+1][j] = '\\';
						board[i][j+1] = '\\';
					}
					
		std::cout << "Case #" << currtest << ":\n";
		if (!possible)
			std::cout << "Impossible\n";
		else for (int i = 0; i < m; i++)
			std::cout << board[i] << '\n';
	}

	return 0;
}
