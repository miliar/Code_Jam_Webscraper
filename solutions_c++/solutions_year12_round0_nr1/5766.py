#include <iostream>
#include <string>
#include <fstream>
#include <list>
#include <stdlib.h>

using namespace std;

char translate(char letter)
{
	switch(letter)
	{
		case ' ':
			return ' ';
		case 'a':
			return 'y';
		case 'b':
			return 'h';
		case 'c':
			return 'e';
		case 'd':
			return 's';
		case 'e':
			return 'o';
		case 'f':
			return 'c';
		case 'g':
			return 'v';
		case 'h':
			return 'x';
		case 'i':
			return 'd';
		case 'j':
			return 'u';
		case 'k':
			return 'i';
		case 'l':
			return 'g';
		case 'm':
			return 'l';
		case 'n':
			return 'b';
		case 'o':
			return 'k';
		case 'p':
			return 'r';
		case 'q':
			return 'z';
		case 'r':
			return 't';
		case 's':
			return 'n';
		case 't':
			return 'w';
		case 'u':
			return 'j';
		case 'v':
			return 'p';
		case 'w':
			return 'f';
		case 'x':
			return 'm';
		case 'y':
			return 'a';
		case 'z':
			return 'q';
	}
}

int main(int argc, char ** argv)
{
	ifstream myfile(argv[1]);

	string num_inputs;
	getline(myfile, num_inputs);

	int num = atoi(num_inputs.c_str());

	list<string> lines;

	for(int i = 0; i < num; i++)
	{
		string line;
		getline(myfile, line);
		lines.push_back(line);
	}

	int count = 1;
	list<string>::iterator it;
	ofstream result;
	result.open("output.txt");

	for(it = lines.begin(); it != lines.end(); ++it)
	{
		string line = *it;
		for(int i = 0; i < line.size(); i++)
		{
			line[i] = translate(line[i]);
		}

		result << "Case #" << count << ": " << line << endl;
		count++;
	}

	result.close();
}

