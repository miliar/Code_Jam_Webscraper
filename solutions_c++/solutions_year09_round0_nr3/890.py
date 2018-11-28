#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>

int main()
{
	std::ifstream in("input.txt");

	int test_count;
	in >> test_count;
	std::string dummy;
	std::getline(in, dummy);

	std::ofstream out("output.txt");
	std::string pattern = "welcome to code jam";
	for (int test_index = 0; test_index < test_count; ++test_index)
	{
		std::string text;
		std::getline(in, text);

		std::vector<int> counts(pattern.size() + 1);
		std::fill(counts.begin(), counts.end(), 0);
		counts[0] = 1;

		for (int pos = 0; pos < int(text.size()); ++pos)
		{
			char c = text[pos];

			for (int stage = int(pattern.size()) - 1; stage >= 0; --stage)
			{
				if (c == pattern[stage])
					counts[stage + 1] = (counts[stage + 1] + counts[stage]) % 10000;
			}
		}

		int count = counts[pattern.size()];

		out << "Case #" << test_index + 1 << ": " << std::setw(4) << std::setfill('0') << count << "\n";
	}
}
