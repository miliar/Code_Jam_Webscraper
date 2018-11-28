// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	std::string realLetters = "abcdefghijklmnopqrstuvwxyz";	
	std::string googlereseLetters = "ynficwlbkuomxsevzpdrjgthaq";

	std::map<char, char> letterMap;

	for (size_t i = 0; i < realLetters.length(); i++) {
		letterMap[googlereseLetters[i]] = realLetters[i];
	}
	
	int testNumber = 1;

	std::string input;
	getline(std::cin, input);
	
	while (std::cin.good()) {
		std::string testcase;

		std::string input;
		getline(std::cin, input);

		std::string output;		

		for (size_t i = 0; i < input.length(); i++) {
			if (letterMap[input[i]] != 0)
				output.push_back(letterMap[input[i]]);
			else output.push_back(' ');
		}

		std::cout << "Case #" << testNumber << ": " << output << std::endl;
		testNumber++;
	}
	
	return 0;
}

