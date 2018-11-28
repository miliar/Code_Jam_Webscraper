#include <iostream>
#include <cctype>

int main()
{
	char mappings[] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u',
			'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j',
			'p', 'f', 'm', 'a', 'q' };
	int T;
	std::cin >> T;
	while(!std::isalpha(std::cin.peek()))
	{
		std::cin.ignore();
	}
	for(int i = 0; i < T; ++i)
	{
		std::string sentence;
		std::getline(std::cin, sentence);
		std::cout << "Case #" << i+1 << ": ";
		for(int j = 0; j < int(sentence.size()); ++j)
		{
			if(std::isalpha(sentence[j]))
			{
				std::cout << mappings[sentence[j] - 'a'];
			}
			else
			{
				std::cout << sentence[j];
			}
		}
		std::cout << std::endl;
	}
	return 0;
}

