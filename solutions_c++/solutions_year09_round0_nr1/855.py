#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
	std::fstream in("input.txt");
	int word_len, word_count, test_count;
	in >> word_len >> word_count >> test_count;

	std::vector<std::string> words;
	for (int word_index = 0; word_index < word_count; ++word_index)
	{
		std::string word;
		in >> word;
		words.push_back(word);
	}

	std::ofstream out("output.txt");
	for (int test_index = 0; test_index < test_count; ++test_index)
	{
		std::string test;
		in >> test;

		std::vector<std::vector<int> > pattern(word_len);
		std::fill(pattern.begin(), pattern.end(), std::vector<int>(256));

		int pos = 0;
		for (int char_index = 0; char_index < word_len; ++char_index)
		{
			char c = test[pos++];
			if (c == '(')
			{
				while ((c = test[pos++]) != ')')
					pattern[char_index][c] = true;
			}
			else
			{
				pattern[char_index][c] = true;
			}
		}

		int match_count = 0;
		for (int word_index = 0; word_index < word_count; ++word_index)
		{
			std::string word = words[word_index];

			bool match = true;
			for (int char_index = 0; char_index < word_len; ++char_index)
			{
				if (!pattern[char_index][word[char_index]])
				{
					match = false;
				}
			}

			if (match)
				++match_count;
		}

		out << "Case #" << test_index + 1 << ": " << match_count << "\n";
	}
}
