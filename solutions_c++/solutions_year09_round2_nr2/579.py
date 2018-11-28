#include <iostream>
#include <string>
#include <algorithm>


int main(int argc, char* argv[])
{
	char s[25];

	int n = 0;

	std::cin >> n;
	std::string line;
	std::getline(std::cin, line);
	for (int c = 0; c < n; c++) {
		memset(s, '0', 25);
		std::getline(std::cin, line);
		for (size_t i = 0; i < line.size(); i++) {
			s[25-i-1] = line[line.size()-i-1];
		}
		std::next_permutation(s, s+25);
		std::cout << "Case #" << (c+1) << ": ";
		int off = 0;
		while (s[off] == '0' && off < 25) off++;
		for (int i = off; i < 25; i++) std::cout << (s[i]);
		std::cout << std::endl;
	}

	return 0;
}

