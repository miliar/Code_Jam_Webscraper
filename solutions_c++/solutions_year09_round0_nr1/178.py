#include <cstdio>
#include <vector>
#include <string>

using namespace std;

#define LMAX 15
#define ALPHABET 26

bool match(int l, const char* pattern, const string& word)
{
	// fprintf(stderr, "pattern: %s, word: %s\n", pattern, word.c_str());
	const char* p = pattern;
	for (int i = 0; i < l; ++i)
	{
		char chw = word[i];
		char chp = *p++;
		if (chp == '\0')
		{
			fprintf(stderr, "Illegal pattern: %s\n", pattern);
			return false;
		}
		bool good;
		if (chp != '(')
			good = (chp == chw);
		else
		{
			good = false;
			while (true)
			{
				chp = *p++;
				if (chp == '\0')
				{
					fprintf(stderr, "Illegal pattern: %s\n", pattern);
					return false;
				}
				if (chp == ')')
					break;
				else if (chp == chw)
					good = true;
			}
		}
		if (!good)
		{
			// fprintf(stderr, "Failed at character %d\n", i);
			return false;
		}
	}
	if (*p != '\0')
	{
		fprintf(stderr, "Illegal pattern: %s\n", pattern);
		return false;
	}
	return true;
}

int main()
{
	int l, d, n;
	scanf("%d%d%d", &l, &d, &n);
	vector<string> words(d);
	for (int i = 0; i < d; ++i)
	{
		char word[LMAX + 1];
		scanf("%s", word);
		words[i] = word;
	}
	for (int idx = 0; idx < n; ++idx)
	{
		char pattern[LMAX * (ALPHABET + 2) + 1];
		scanf("%s", pattern);
		int count = 0;
		for (int i = 0; i < d; ++i)
		{
			if (match(l, pattern, words[i]))
				++count;
		}
		printf("Case #%d: %d\n", idx + 1, count);
	}
	return 0;
}
