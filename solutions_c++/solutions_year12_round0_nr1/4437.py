/***************************************************

Name:			Justin McCandless
Compiler Name:	g++
Filename:		qa.cpp
Problem:		Google Code Jam 2012 Qualification Question A

****************************************************/

#include<iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

string stringGToE (string);
char charGToE (char);

int main(void)
{
	int cases = 0;
	string casesS;	
	getline (cin, casesS);
	stringstream(casesS) >> cases;

	for (int i = 0; i < cases; i++)
	{
		string input;
		getline (cin, input);
		cout << "Case #" << (i + 1) << ": " << stringGToE(input) << endl;
	}

    return 1;
}

string stringGToE (string S)
{
	for (int i = 0; i < S.length(); i++)
	{
		S[i] = charGToE(S[i]);
	}
	return S;
}

char charGToE (char c)
{
	if (c == ' ')
		return ' ';
	if (c == 'a')
		return 'y';
	else if (c == 'b')
		return 'h';
	else if (c == 'c')
		return 'e';
	else if (c == 'd')
		return 's';
	else if (c == 'e')
		return 'o';
	else if (c == 'f')
		return 'c';
	else if (c == 'g')
		return 'v';
	else if (c == 'h')
		return 'x';
	else if (c == 'i')
		return 'd';
	else if (c == 'j')
		return 'u';
	else if (c == 'k')
		return 'i';
	else if (c == 'l')
		return 'g';
	else if (c == 'm')
		return 'l';
	else if (c == 'n')
		return 'b';
	else if (c == 'o')
		return 'k';
	else if (c == 'p')
		return 'r';
	else if (c == 'q')
		return 'z';
	else if (c == 'r')
		return 't';
	else if (c == 's')
		return 'n';
	else if (c == 't')
		return 'w';
	else if (c == 'u')
		return 'j';
	else if (c == 'v')
		return 'p';
	else if (c == 'w')
		return 'f';
	else if (c == 'x')
		return 'm';
	else if (c == 'y')
		return 'a';
	else if (c == 'z')
		return 'q';
	else
		return '?';
}





