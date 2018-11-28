//
//  main.cpp
//  Googlerese
//
//  Created by Justin Schmidt on 4/14/12.
//  Copyright (c) 2012 Grizzly. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;


void handleString(char *c);
char outputCharacter(char c);


int main(int argc, const char * argv[])
{
	int numLines = 0;
	
	ifstream input ("input.txt");
	
	input >> numLines;
	++numLines;
	
	int caseNum = 1;
	
	while (numLines > 0)
	{
		char c;
		c = input.get();
		if (c == '\n' || c == '\r' || c == '\0')
		{
			--numLines;
			if (numLines > 0)
			{
				cout << "\nCase #" << caseNum << ": ";
				++caseNum;
			}
		}
		
		c = outputCharacter(c);
		if (c != '~')
			cout << c;
	}
	
    return 0;
}

void handleString(char *c)
{
	for (int j = 0; j < 100; ++j)
	{
		if (c[j] == '\n')
			break;
		if (c[j] == '\r')
			break;
		if (c[j] == '\0')
			break;
		
		printf("%c", outputCharacter(c[j]));
	}
}

char outputCharacter(char c)
{
	switch (c)
	{
		case ' ':
			return ' ';
			break;
		case 'a':
			return 'y';
			break;
		case 'b':
			return 'h';
			break;
		case 'c':
			return 'e';
			break;
		case 'd':
			return 's';
			break;
		case 'e':
			return 'o';
			break;
		case 'f':
			return 'c';
			break;
		case 'g':
			return 'v';
			break;
		case 'h':
			return 'x';
			break;
		case 'i':
			return 'd';
			break;
		case 'j':
			return 'u';
			break;
		case 'k':
			return 'i';
			break;
		case 'l':
			return 'g';
			break;
		case 'm':
			return 'l';
			break;
		case 'n':
			return 'b';
			break;
		case 'o':
			return 'k';
			break;
		case 'p':
			return 'r';
			break;
		case 'q':
			return 'z';
			break;
		case 'r':
			return 't';
			break;
		case 's':
			return 'n';
			break;
		case 't':
			return 'w';
			break;
		case 'u':
			return 'j';
			break;
		case 'v':
			return 'p';
			break;
		case 'w':
			return 'f';
			break;
		case 'x':
			return 'm';
			break;
		case 'y':
			return 'a';
			break;
		case 'z':
			return 'q';
			break;
	}
	return '~';
}
