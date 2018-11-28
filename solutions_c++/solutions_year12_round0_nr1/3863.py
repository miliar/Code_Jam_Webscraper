#include <iostream>
#include <string>
#include <sstream>

char map[] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
	/* 'n' -> */ 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a',
	'q' };

int main()
{
	std::string line;
	size_t nlines = 0;

	std::cin >> nlines;
	std::cin.ignore();

	for (size_t i = 1; i <= nlines; ++i)
	{
		getline(std::cin, line);
		for (size_t i = 0; i < line.size(); ++i)
			if (line[i] >= 'a' && line[i] <= 'z')
				line[i] = map[line[i] - 'a'];
		std::cout << "Case #" << i << ": " << line << std::endl;
	}
}
