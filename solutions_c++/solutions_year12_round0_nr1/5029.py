#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fstream>
#include <string>

using namespace std;

char modify_chars( char str)
{
	switch( str )
	{
	case 'a':
		return 'y';
	case 'b':
		return 'h';
	case 'c'://
		return 'e';
	case 'd':
		return 's';
	case 'e':
		return 'o';
	case 'f'://
		return 'c';
	case 'g':
		return 'v';
	case 'h':
		return 'x';
	case 'i'://
		return 'd';
	case 'j':
		return 'u';
	case 'k':
		return 'i';
	case 'l':
		return 'g';
	case 'm':
		return 'l';
	case 'n'://
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
	case 'w'://
		return 'f';
	case 'x':
		return 'm';
	case 'y'://
		return 'a';
	case 'z':
		return 'q';
	default:
		break;
	}
}

void translation (string &input)
{
	for(int i = 0; i <input.size(); ++i)
	{
		if(input[i] == ' ') continue;
		if(input[i] < 97 && input[i] > 122) continue;
		input[i] = modify_chars(input[i]);
	}
}

int main()
{
	ifstream infile;
	ofstream outfile;

	infile.open("c:\\google\\A-small-attempt0.in");
	outfile.open("c:\\google\\result.txt");

	int case_number;
	int i = 1;
	if(!infile.fail())
	{
			infile>>case_number;
			string str;
			getline(infile,str);
			while(getline(infile,str))
			{
				translation(str);
				outfile<< "Case #"<<i<<": ";
				outfile<<str<<endl;
				i++;
			}
	}
	system("pause");
	return 0;
}
