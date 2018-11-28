#include <iostream>
#include <string>
#include <algorithm>

char check(std::string s)
{
	std::sort(s.begin(), s.end());
	int f = 0;
	int l = 3;
	if (s[f] == 'T') ++f;
	if (s[l] == 'T') --l;
	char c = s[f];
	bool ok = true;
	for (int i = f ; i <= l ; ++i)
		if (c != s[i])
			ok = false;
	return ok ? c : '.';
}

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
		std::string s[4];
		std::cin >> s[0] >> s[1] >> s[2] >> s[3];
		bool dots = false;
		char c = '.';
		if (c == '.') c = check(std::string(1, s[0][0]) + s[1][1] + s[2][2] + s[3][3]);
		if (c == '.') c = check(std::string(1, s[3][0]) + s[2][1] + s[1][2] + s[0][3]);
		for (int i = 0 ; i < 4 ; ++i)
		{
			for (int j = 0 ; j < 4 ; ++j)
				if (s[i][j] == '.')
					dots = true;

			if (c == '.') c = check(s[i]);
			if (c == '.') c = check(std::string(1, s[0][i]) + s[1][i] + s[2][i] + s[3][i]);
		}
		std::cout << "Case #" << t << ": ";
		if (c != '.')
			std::cout << c << " won";
		else if (dots)
			std::cout << "Game has not completed";
		else
			std::cout << "Draw";
		std::cout << "\n";
	}
	return 0;
}

