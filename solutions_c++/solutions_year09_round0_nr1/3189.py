#include <cassert>
#include <cstdlib>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

using namespace std;

vector<string> parsePattern(const string & _pattern, size_t _patternSize);
bool matchToken(char _letter, const string & _token);

int main()
{
	size_t l, d, n;
	cin >> l >> d >> n;

	vector<string> words(d);
	vector<vector<string> > patterns(n);

	for (size_t i = 0; i < d; i++)
	{
		cin >> words[i];
	}

	for (size_t i = 0; i < n; i++)
	{
		string pattern;
		cin >> pattern;
		patterns[i] = parsePattern(pattern, l);
	}

	for (size_t curPattern = 0; curPattern < patterns.size(); curPattern++)
	{
		size_t wordsMatched = 0;

		// ѕеребираем словарь
		for (size_t word = 0; word < words.size(); word++)
		{
			bool validWord = true;

			// ѕеребираем буквы слова
			for (size_t letter = 0; letter < l; letter++)
			{

				// если токен не совпал, прекращаем
				if (!matchToken(words[word][letter], patterns[curPattern][letter]))
				{
					validWord = false;
					break;
				}
			}
			
			// если слово подошло
			if (validWord)
			{
				wordsMatched++;
			}
		}

		if (curPattern != 0) { cout << endl; }
		cout << "Case #" << curPattern + 1 << ": " << wordsMatched;
	}

	return EXIT_SUCCESS;
}

vector<string> parsePattern(const string & _pattern, size_t _patternSize)
{
	vector<string> parsedPattern(_patternSize);

	size_t curToken = 0;
	
	for (size_t ch = 0; ch < _pattern.size(); /* increment is inside loop */)
	{
		if (_pattern[ch] == '(')
		{
			size_t tokenEnd = _pattern.find_first_of(')', ch);
			parsedPattern[curToken++] = _pattern.substr(ch + 1, tokenEnd - (ch + 1));
			ch = tokenEnd + 1;
		} 
		else
		{
			parsedPattern[curToken++] = string(1, _pattern[ch]);
			ch++;
		}
	}

	assert(curToken == _patternSize);

	return parsedPattern;
}

bool matchToken(char _letter, const string & _token)
{
	for (size_t ch = 0; ch < _token.size(); ch++)
	{
		if (_token[ch] == _letter)
		{
			return true;
		}
	}
	return false;
}