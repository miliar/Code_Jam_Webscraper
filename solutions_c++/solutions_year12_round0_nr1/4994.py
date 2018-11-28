#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <fstream>
#include <string>
#include <map>

using namespace std;

map<char,char> dictionary;

string translate (string str)
{
	string output;
	for (int i = 0; i < str.length(); i++)
	{
		output.push_back(dictionary[str[i]]);
	}
	output.push_back('\n');
	return output;
}

int main(int argc, char *argv[])
{

	
	dictionary['a'] = 'y';
	dictionary['b'] = 'h';
	dictionary['c'] = 'e';
	dictionary['d'] = 's';
	dictionary['e'] = 'o';
	dictionary['f'] = 'c';
	dictionary['g'] = 'v';
	dictionary['h'] = 'x';
	dictionary['i'] = 'd';
	dictionary['j'] = 'u';
	dictionary['k'] = 'i';
	dictionary['l'] = 'g';
	dictionary['m'] = 'l';
	dictionary['n'] = 'b';
	dictionary['o'] = 'k';
	dictionary['p'] = 'r';
	dictionary['q'] = 'z';
	dictionary['r'] = 't';
	dictionary['s'] = 'n';
	dictionary['t'] = 'w';
	dictionary['u'] = 'j';
	dictionary['v'] = 'p';
	dictionary['w'] = 'f';
	dictionary['x'] = 'm';
	dictionary['y'] = 'a';
	dictionary['z'] = 'q';
	dictionary[' '] = ' ';

	ifstream inFile ("input.txt");
	ofstream  outFile ("output.txt");
	if (inFile.is_open() && outFile.is_open())
	{
		string line;
		getline (inFile,line);
		int inputSize = atoi(line.c_str());
		for (int i = 1; i <= inputSize; i++)
		{
			getline (inFile,line);
			
			string output = translate(line);
			outFile << "Case #"<< i <<": " << output.c_str();
		}
		inFile.close();
	}



    return 0;
}