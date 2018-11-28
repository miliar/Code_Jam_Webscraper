#include "stdafx.h"
#include <iostream>
#include<fstream>
using namespace std;

void main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	char conv(char);
	int t;
	char c[120];
	fin>>t;
	fin.getline(c,120,'\n');
	for(int i=1;i<=t;i++)
	{
		fout<<"Case #"<<i<<": ";
		fin.getline(c,120,'\n');
		for(int j=0;j<strlen(c);j++)
		{
			fout<<conv(c[j]);
		}
	    fout<<'\n';
	}
}
char conv(char a)
{
	switch(a)
	{
	case 'a': return 'y';
		break;
	case 'b': return 'h';
		break;
	case 'c': return 'e';
		break;
	case 'd': return 's';
		break;
	case 'e': return 'o';
		break;
	case 'f': return 'c';
		break;
	case 'g': return 'v';
		break;
	case 'h': return 'x';
		break;
	case 'i': return 'd';
		break;
	case 'j': return 'u';
		break;
	case 'k': return 'i';
		break;
	case 'l': return 'g';
		break;
	case 'm': return 'l';
		break;
	case 'n': return 'b';
		break;
	case 'o': return 'k';
		break;
	case 'p': return 'r';
		break;
	case 'q': return 'z';
		break;
	case 'r': return 't';
		break;
	case 's': return 'n';
		break;
	case 't': return 'w';
		break;
	case 'u': return 'j';
		break;
	case 'v': return 'p';
		break;
	case 'w': return 'f';
		break;
	case 'x': return 'm';
		break;
	case 'y': return 'a';
		break;
	case 'z': return 'q';
		break;
	case ' ': return ' ';
		break;
	}
}