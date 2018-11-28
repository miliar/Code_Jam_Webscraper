// speaking.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

ifstream in("test.txt");
ofstream out("out.txt");

char translate(char s)
{
	switch(s)
	{
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
}

void runCase(int test)
{
	string G;
	getline( in, G);
	
	out << "Case #" << test << ": ";

	for(int i = 0; i < G.length(); i++)
		out << translate(G.at(i));
	out << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{

	int T;
	in >> T;

	string _t;
	getline( in, _t);

	for(int i = 0; i < T; i++)
		runCase( i+1);

	return 0;
}

