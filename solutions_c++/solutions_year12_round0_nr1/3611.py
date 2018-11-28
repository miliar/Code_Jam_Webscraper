// code01.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

void ch(char *b){
	int i = 0;
	while(i<1000)
	{
		switch(b[i]){
		case 'a':
			b[i] = 'y';
			break;
		case 'b':
			b[i] = 'h';
			break;
		case 'c':
			b[i] = 'e';
			break;
		case 'd':
			b[i] = 's';
			break;
		case 'e':
			b[i] = 'o';
			break;
		case 'f':
			b[i] = 'c';
			break;
		case 'g':
			b[i] = 'v';
			break;
		case 'h':
			b[i] = 'x';
			break;
		case 'i':
			b[i] = 'd';
			break;
		case 'j':
			b[i] = 'u';
			break;
		case 'k':
			b[i] = 'i';
			break;
		case 'l':
			b[i] = 'g';
			break;
		case 'm':
			b[i] = 'l';
			break;
		case 'n':
			b[i] = 'b';
			break;
		case 'o':
			b[i] = 'k';
			break;
		case 'p':
			b[i] = 'r';
			break;
		case 'q':
			b[i] = 'z';
			break;
		case 'r':
			b[i] = 't';
			break;
		case 's':
			b[i] = 'n';
			break;
		case 't':
			b[i] = 'w';
			break;
		case 'u':
			b[i] = 'j';
			break;
		case 'v':
			b[i] = 'p';
			break;
		case 'w':
			b[i] = 'f';
			break;
		case 'x':
			b[i] = 'm';
			break;
		case 'y':
			b[i] = 'a';
			break;
		case 'z':
			b[i] = 'q';
			break;
		default:

			break;

		}
		i++;
	}

}

int _tmain(int argc, _TCHAR* argv[])
{

	char buf[1000];
	int a;
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt0.in");
	fout.open("output.txt");
	
	fin.getline(buf,1000);
	a = atoi(buf);

	for(int c = 0 ; c < a ; c++){
		fin.getline(buf,1000);

		ch(buf);	// 바꾸기함수

		fout<< "Case #"<<c+1<<": "<<buf << endl;
	}

	

	return 0;
}

