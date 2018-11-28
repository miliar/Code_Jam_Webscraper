#include <iostream>
#include <sstream>
#include <string>

int main()
{
	std::string line;
	size_t nlines = 0;

	std::cin >> nlines;
	std::cin.ignore();

	for (size_t l = 1; l <= nlines; ++l)
	{
		getline(std::cin, line);
		std::stringstream* ss = new std::stringstream(line);
		size_t numG;
		int surp;
		int min;
		int res = 0;

		*ss >> numG;

		line = line.substr(line.find(' ') + 1);
		delete ss;
		ss = new std::stringstream(line);
		*ss >> surp;

		line = line.substr(line.find(' ') + 1);
		delete ss;
		ss = new std::stringstream(line);
		*ss >> min;

		for (size_t ng = 0; ng < numG; ++ng)
		{
			int num;
			line = line.substr(line.find(' ') + 1);
			delete ss;
			ss = new std::stringstream(line);
			*ss >> num;

			if (num >= 3 * min - 2)
				++res;
			else if (num >= 3 * min - 4 && num >= 2 && surp > 0)
			{
				++res;
				--surp;
			}
		}

		delete ss;
		std::cout << "Case #" << l << ": " << res << std::endl;
	}
}
