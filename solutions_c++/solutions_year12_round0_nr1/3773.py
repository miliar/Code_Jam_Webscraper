#include <iostream>
#include <map>
#include <set>
#include <vector>

void processLine(int lineNum, char* mapping)
{
	std::cout << "Case #" << lineNum+1 << ": ";

	std::string googleText;
	getline(std::cin, googleText);

	for(int i = 0; i < googleText.length(); ++i) {
		// only translate letters
		if (googleText[i] >= 'a' && googleText[i] <= 'z') {
			googleText[i] = mapping[googleText[i] - 'a'];
		}
	}

	std::cout << googleText << std::endl;
}

int main()
{
	char mapping[] = { 'y',
										 'h',
										 'e',
										 's',
										 'o',
										 'c',
										 'v',
										 'x',
										 'd',
										 'u',
										 'i',
										 'g',
										 'l',
										 'b',
										 'k',
										 'r',
										 'z',
										 't',
										 'n',
										 'w',
										 'j',
										 'p',
										 'f',
										 'm',
										 'a',
										 'q' };


	int numLines = 0;
	std::cin >> numLines;

	// hack
	std::string firstLine;
	getline(std::cin, firstLine);

	for(int i = 0; i < numLines; ++i) {
		processLine(i, mapping);		
	}

	return 0;

/*
	std::cout << numLines << std::endl;

	std::cin >> numLines;
	std::cout << numLines << std::endl;
*/
}
