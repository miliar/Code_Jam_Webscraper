/*
 * googleLanguage.cpp
 *
 *  Created on: Apr 13, 2012
 *      Author: Danny
 */

#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int main(int argc, char* argv[])
{
	if(argc < 2)
	{
		cout << "Not enough arguments." << endl;
		return 1;
	}

	ifstream fin;
	fin.open(argv[1]);

	ofstream fout;
	fout.open("Output.txt");

	if(!fin.is_open())
	{
		cout << "File open failed." << endl;
	}


	char alphabet[26];

	alphabet['a'-'a'] = 'y';
	alphabet['b'-'a'] = 'h';
	alphabet['c'-'a'] = 'e';
	alphabet['d'-'a'] = 's';
	alphabet['e'-'a'] = 'o';
	alphabet['f'-'a'] = 'c';
	alphabet['g'-'a'] = 'v';
	alphabet['h'-'a'] = 'x';
	alphabet['i'-'a'] = 'd';
	alphabet['j'-'a'] = 'u';
	alphabet['k'-'a'] = 'i';
	alphabet['l'-'a'] = 'g';
	alphabet['m'-'a'] = 'l';
	alphabet['n'-'a'] = 'b';
	alphabet['o'-'a'] = 'k';
	alphabet['p'-'a'] = 'r';
	alphabet['q'-'a'] = 'z';
	alphabet['r'-'a'] = 't';
	alphabet['s'-'a'] = 'n';
	alphabet['t'-'a'] = 'w';
	alphabet['u'-'a'] = 'j';
	alphabet['v'-'a'] = 'p';
	alphabet['w'-'a'] = 'f';
	alphabet['x'-'a'] = 'm';
	alphabet['y'-'a'] = 'a';
	alphabet['z'-'a'] = 'q';


	int numCases = 0, i, j;

	char line[150];

	fin >> numCases;

	cout << numCases << endl;
	fin.getline(line, 150);
	for(i = 0; i < numCases; i++)
	{
		fout << "Case #" << i+1 << ": ";
		fin.getline(line, 150);
		for(j = 0; j < (int)strlen(line); j++)
		{
			if(line[j] == ' ')
			{
				fout << ' ';
			}
			else
			{
				fout << alphabet[line[j]- 'a'];
			}
		}
		fout << endl;
	}
}


