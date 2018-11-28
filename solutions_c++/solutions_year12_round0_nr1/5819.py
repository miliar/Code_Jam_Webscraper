#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;
using std::cin;
using std::cout;
using std::endl;

char compare(char x)
{
	switch(x)
	{
	case'a':return 'y';
		break;
	case'b':return 'h';
		break;
	case'c':return 'e';
		break;
	case'd':return 's';
		break;
	case'e':return 'o';
		break;
	case'f':return 'c';
		break;
	case'g':return 'v';
		break;
	case'h':return 'x';
		break;
	case'i':return 'd';
		break;
	case'j':return 'u';
		break;
	case'k':return 'i';
		break;
	case'l':return 'g';
		break;
	case'm':return 'l';
		break;
	case'n':return 'b';
		break;
	case'o':return 'k';
		break;
	case'p':return 'r';
		break;
	case'q':return 'z';
		break;
	case'r':return 't';
		break;
	case's':return 'n';
		break;
	case't':return 'w';
		break;
	case'u':return 'j';
		break;
	case'v':return 'p';
		break;
	case'w':return 'f';
		break;
	case'x':return 'm';
		break;
	case'y':return 'a';
		break;
	case'z':return 'q';
		break;
	default:
		return ' ';
		break;

	}
}
void main()
{
	ifstream test;
	test.open("A-small-attempt0.in");
	ofstream testo;
	testo.open("testo.txt");

	int T,tempi;
	int count=0;
	char G[10000];

	test>>T;
	test.getline(G,10000);
	while (! test.eof())
	{
		count++;
		test.getline(G,10000);
		if ( count != 31)
		{testo<<"Case #"<<count<<": ";}
		for (int i=0;i<strlen(G);i++)
		{
			testo<<compare(G[i]);
		}
		testo<<endl;
	}
}
