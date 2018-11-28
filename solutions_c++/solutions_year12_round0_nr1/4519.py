#include <iostream>
#include <string>

const int MAX = 26;

int main()
{
	char matching[MAX] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u',
		'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

	int t;
	scanf("%d", &t);

	std::string input;
	getline(std::cin, input);

	int caseNum = 1;
	while (t-- > 0)
	{
		getline(std::cin, input);

		std::string result;
		for (std::string::iterator i = input.begin(); i != input.end(); ++i)
		{
			if ((*i) == ' ')
			{
				result += ' ';
				continue;
			}

			int idx = *i - 'a';
			result += matching[idx];
		}

		printf("Case #%d: %s\n", caseNum++, result.c_str());
	}

	return 0;
}