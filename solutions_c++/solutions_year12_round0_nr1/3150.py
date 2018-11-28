// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "string"
#include "iostream"
#include "fstream"
#include "assert.h"


int _tmain(int argc, _TCHAR* argv[])
{
	// Check there are two arguments.  First argument is input, second is output.
	assert(argc == 3);

	// Open input file.
	std::ifstream infile;
	infile.open(argv[1]);
	assert(infile.is_open());
	assert(infile.good());

	// Open output file.
	std::ofstream outfile(argv[2]);

	// Read in number of testcases.
	int t;
	infile >> t;
	infile.ignore(2000,'\n');

	std::cout << t;

	for (int i=0; i<t; i++)
	{
		// Read next line
		std::string line;
		std::getline(infile, line);

		std::string::iterator it;
		for(it = line.begin(); it != line.end(); it++)
		{
			switch (*it)
			{
			case 'a':
					*it = 'y';
					break;
			case 'b':
				*it = 'h';
				break;
			case 'c':
				*it = 'e';
				break;
			case 'd':
				*it = 's';
				break;
			case 'e':
				*it = 'o';
				break;
			case 'f':
				*it = 'c';
				break;
			case 'g':
				*it = 'v';
				break;
			case 'h':
				*it = 'x';
				break;
			case 'i':
				*it = 'd';
				break;
			case 'j':
				*it = 'u';
				break;
			case 'k':
				*it = 'i';
				break;
			case 'l':
				*it = 'g';
				break;
			case 'm':
				*it = 'l';
				break;
			case 'n':
				*it = 'b';
				break;
			case 'o':
				*it = 'k';
				break;
			case 'p':
				*it = 'r';
				break;
			case 'q':
				*it = 'z';
				break;
			case 'r':
				*it = 't';
				break;
			case 's':
				*it = 'n';
				break;
			case 't':
				*it = 'w';
				break;
			case 'u':
				*it = 'j';
				break;
			case 'v':
				*it = 'p';
				break;
			case 'w':
				*it = 'f';
				break;
			case 'x':
				*it = 'm';
				break;
			case 'y':
				*it = 'a';
				break;
			case 'z':
				*it = 'q';
				break;
			default:
				break;
				// Assume whitespace.
			}
		}

		outfile << "Case #" << i+1 << ": " << line << std::endl;

		std::cout << line;
	}
			
	// Close input and output files.
	infile.close();
	outfile.close();

	system("pause");

	return 0;
}

