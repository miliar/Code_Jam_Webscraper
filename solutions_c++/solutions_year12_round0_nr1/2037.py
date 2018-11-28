#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>

int T;

std::map<char,char> mapping;

int main()
{
	std::fstream input;
	std::fstream output;
	input.open( "input.txt", std::istream::in );
	output.open("output.txt", std::ostream::out);

	mapping['a'] = 'y';
	mapping['b'] = 'h';
	mapping['c'] = 'e';
	mapping['d'] = 's';
	mapping['e'] = 'o';
	mapping['f'] = 'c';
	mapping['g'] = 'v';
	mapping['h'] = 'x';
	mapping['i'] = 'd';
	mapping['j'] = 'u';
	mapping['k'] = 'i';
	mapping['l'] = 'g';
	mapping['m'] = 'l';
	mapping['n'] = 'b';
	mapping['o'] = 'k';
	mapping['p'] = 'r';
	mapping['q'] = 'z';
	mapping['r'] = 't';
	mapping['s'] = 'n';
	mapping['t'] = 'w';
	mapping['u'] = 'j';
	mapping['v'] = 'p';
	mapping['w'] = 'f';
	mapping['x'] = 'm';
	mapping['y'] = 'a';
	mapping['z'] = 'q';

	input >> T;
	std::string temp;
	std::getline(input,temp);
	for(int t = 0; t < T; t++)
	{
		std::string in, out;
		
		std::getline(input,in);
		
		for(int i = 0; i < in.length(); i++)
		{
			if(in[i] == ' ')
				out.push_back(' ');
			else
				out.push_back(mapping[in[i]]);
		}
		std::cout << "Case #" << t+1 << ": " << out << std::endl;
		output << "Case #" << t+1 << ": " << out << std::endl;
	}
	getchar();
	return 1;
}