// googlecj2012a.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

inline void transLetter(char* letter)
{
	switch(*letter)
	{
	case 'a':
		*letter = 'y';
		break;
	case 'b':
		*letter = 'h';
		break;
	case 'c':
		*letter = 'e';
		break;
	case 'd':
		*letter = 's';
		break;
	case 'e':
		*letter = 'o';
		break;
	case 'f':
		*letter = 'c';
		break;
	case 'g':
		*letter = 'v';
		break;
	case 'h':
		*letter = 'x';
		break;
	case 'i':
		*letter = 'd';
		break;
	case 'j':
		*letter = 'u';
		break;
	case 'k':
		*letter = 'i';
		break;
	case 'l':
		*letter = 'g';
		break;
	case 'm':
		*letter = 'l';
		break;
	case 'n':
		*letter = 'b';
		break;
	case 'o':
		*letter = 'k';
		break;
	case 'p':
		*letter = 'r';
		break;
	case 'q':
		*letter = 'z';
		break;
	case 'r':
		*letter = 't';
		break;
	case 's':
		*letter = 'n';
		break;
	case 't':
		*letter = 'w';
		break;
	case 'u':
		*letter = 'j';
		break;
	case 'v':
		*letter = 'p';
		break;
	case 'w':
		*letter = 'f';
		break;
	case 'x':
		*letter = 'm';
		break;
	case 'y':
		*letter = 'a';
		break;
	case 'z':
		*letter = 'q';
		break;
	default:
		;
	};
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin( "c:\\A-small-attempt3.in" );
	ofstream fout( "c:\\output.txt" , ios_base::in || ios_base::trunc);
	string temp1, temp2;
	istringstream stream1;
	string temp;
	fin>>temp;
	int times=0;
	stream1.str(temp);
	stream1>>times;
	string stc;
	getline(fin, stc);
	for(int n=0; n<times; ++n)
	{		
		getline(fin, stc);
		for(unsigned int i=0; i<stc.length(); ++i)
		{
			transLetter(&stc[i]);
		}
		if(n<times)
		fout<<"Case #"<<n+1<<": "<<stc<<endl;
	}
	return 0;
}

