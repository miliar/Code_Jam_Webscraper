#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <float.h>
#include <assert.h>
#include <queue>
#include <iostream>
#include <fstream>

using namespace std;
#define FILENAME "in.txt"
#define FILENAME2 "out.txt"
#define MAXCASELEN 105
char text[122];

void Init()
{
	for (int i = 0; i < 122; i ++)
		text[i] = ' '; //dfault to whitespacw
	text[' '] = ' ';
	text['e'] = 'o';
	text['j'] = 'u';
	text['p'] = 'r';
	text['m'] = 'l';
	text['y'] = 'a';
	text['a'] = 'y';
	text['s'] = 'n';
	text['l'] = 'g';
	text['c'] = 'e';
	text['k'] = 'i';
	text['d'] = 's';
	text['x'] = 'm';
	text['v'] = 'p';
	text['b'] = 'h';
	text['r'] = 't';
	text['i'] = 'd';
	text['t'] = 'w';
	text['w'] = 'f';
	text['f'] = 'c';
	text['o'] = 'k';
	text['g'] = 'v';
	text['q'] = 'z';
	text['n'] = 'b';
	text['u'] = 'j';
	text['h'] = 'x';
	text['z'] = 'q';                                                            
}

void ReadIn( queue<string> * q )
{
	char * T = (char * ) calloc  (MAXCASELEN, sizeof(char));
	ifstream * is = new ifstream();
	is->open(FILENAME);
	while (is->good())
	{
		is->getline(T,MAXCASELEN);
		q->push(string(T));	
	}
	free(T);
}

string DecodeString( string s)
{
	string r;
	for(int i = 0; i < s.size(); i++)
		s[i] = text[s[i]];
	return s;
}

int main( int argc, char **argv )	
{
	int casecntr = 1;
	ofstream out;
	out.open(FILENAME2);
	queue<string> input;
	ReadIn(&input);
	Init();
	int num =  atoi(input.front().c_str());
	input.pop();
	while (!input.empty())
	{
		cout << "Case #" << casecntr << ": " << DecodeString(input.front()).c_str() << endl;
		out << "Case #" << casecntr << ": " << DecodeString(input.front()).c_str() << endl;
		input.pop();
		casecntr++;
	}
	return 0;
}

