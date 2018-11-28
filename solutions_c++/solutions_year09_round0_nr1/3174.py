#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

bool DoEachMatching(const std::string &word, const std::string &pattern)
{
	std::size_t p = 0;
	for (std::size_t i = 0; i < word.length(); ++i)
	{
		if (pattern[p] == '(')
		{
			for (++p; pattern[p] != ')'; ++p)
			{
				if (pattern[p] == word[i])
					break;
			}
			if (pattern[p] == ')')
				return false;
			while (pattern[p] != ')')
				++p;
			++p;
		}
		else if (pattern[p++] != word[i])
			return false;
	}

	return true;
}

void DoMatching(const std::vector<std::string> &words,
	const std::vector<std::string> &patterns)
{
	std::vector<int> results(patterns.size(), 0);
	for (std::size_t i = 0; i < words.size(); ++i)
	{
		for (std::size_t j = 0; j < patterns.size(); ++j)
		{
			if (DoEachMatching(words[i], patterns[j]))
				results[j]++;
		}
	}

	for (std::size_t i = 0; i < patterns.size(); ++i)
		std::cout << "Case #" << (i + 1) << ": " << results[i] << std::endl;
}

int main()
{
	int L, D, N;
	std::cin >> L >> D >> N;

	std::vector<std::string> words;
	std::vector<std::string> patterns;

	std::string line;
	std::getline(std::cin, line);

	for (int i = 0; i < D; ++i)
	{
		std::getline(std::cin, line);
		words.push_back(line);
	}

	for (int i = 0; i < N; ++i)
	{
		std::getline(std::cin, line);
		patterns.push_back(line);
	}

	DoMatching(words, patterns);

	return 0;
}
