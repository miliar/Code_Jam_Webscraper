#include <iostream>
#include <map>
#include <string>

int main(int argc, char *argv[])
{
	std::map<char, char> dict;

	dict['a'] = 'y';
	dict['b'] = 'h';
	dict['c'] = 'e';
	dict['d'] = 's';
	dict['e'] = 'o';
	dict['f'] = 'c';
	dict['g'] = 'v';
	dict['h'] = 'x';
	dict['i'] = 'd';
	dict['j'] = 'u';
	dict['k'] = 'i';
	dict['l'] = 'g';
	dict['m'] = 'l';
	dict['n'] = 'b';
	dict['o'] = 'k';
	dict['p'] = 'r';
	dict['q'] = 'z';
	dict['r'] = 't';
	dict['s'] = 'n';
	dict['t'] = 'w';
	dict['u'] = 'j';
	dict['v'] = 'p';
	dict['w'] = 'f';
	dict['x'] = 'm';
	dict['y'] = 'a';
	dict['z'] = 'q';
	dict[' '] = ' ';

	int num_inputs;
	std::cin >> num_inputs;
	std::cin.ignore(1000, '\n');

	for(int cs = 1; cs <= num_inputs; cs++) {
		std::string input;
		std::string output;

		std::getline(std::cin, input);

		for(std::string::size_type i = 0; i < input.length(); i++)
		{
			output += dict[input[i]];
		}

		std::cout << "Case #" << cs << ": " << output << std::endl;
	}

	return 0;
}